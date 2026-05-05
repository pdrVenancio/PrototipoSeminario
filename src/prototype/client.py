from __future__ import annotations

import argparse
import json
import os
import uuid
from typing import Any

import pulsar

from prototype.protocol import Request, Response


PULSAR_URL = os.getenv("PULSAR_URL", "pulsar://localhost:6650")
# Tópico fixo usado como "fila de entrada" das requisições para o servidor.
REQUEST_TOPIC = os.getenv("REQUEST_TOPIC", "persistent://public/default/prototype-requests")


def main() -> None:
    # Entrada principal do cliente: permite escolher a operação pela linha de comando.
    parser = argparse.ArgumentParser(description="Cliente do prototipo Python + Apache Pulsar.")
    parser.add_argument(
        "operation",
        nargs="?",
        choices=["echo", "write_file", "calculate", "demo"],
        default="demo",
        help="Operacao a executar. Padrao: demo.",
    )
    parser.add_argument("--text", default="Ola servidor, tudo certo?")
    parser.add_argument("--filename", default="server.txt")
    parser.add_argument("--content", default="Linha gravada via Apache Pulsar.")
    parser.add_argument("--mode", choices=["append", "replace"], default="append")
    parser.add_argument("--function", default="add")
    parser.add_argument("--args", nargs="*", default=["10", "5"])
    parser.add_argument("--timeout", type=int, default=10)
    args = parser.parse_args()

    # O cliente RPC abre a conexão, envia a requisição e aguarda a resposta do servidor.
    with PulsarRpcClient(PULSAR_URL, REQUEST_TOPIC, timeout_seconds=args.timeout) as rpc:
        if args.operation == "demo":
            responses = run_demo(rpc)
        elif args.operation == "echo":
            responses = [rpc.call("echo", {"text": args.text})]
        elif args.operation == "write_file":
            responses = [
                rpc.call(
                    "write_file",
                    {
                        "filename": args.filename,
                        "content": args.content,
                        "mode": args.mode,
                    },
                )
            ]
        else:
            responses = [
                rpc.call(
                    "calculate",
                    {
                        "function": args.function,
                        "args": [_parse_number(value) for value in args.args],
                    },
                )
            ]

    for response in responses:
        print(json.dumps(response, ensure_ascii=False, indent=2))


class PulsarRpcClient:
    def __init__(self, pulsar_url: str, request_topic: str, timeout_seconds: int) -> None:
        # URL do broker Apache Pulsar. Em uma demo distribuida, aponta para o IP da maquina do broker.
        self.pulsar_url = pulsar_url
        # Tópico onde todos os clientes publicam pedidos para o servidor processar.
        self.request_topic = request_topic
        self.timeout_millis = timeout_seconds * 1000
        # Cada execução do cliente cria um tópico Pulsar único para receber suas respostas.
        # Isso permite que varios clientes usem o mesmo servidor sem misturar retornos.
        self.reply_topic = f"persistent://public/default/replies-{uuid.uuid4().hex}"
        self.client: pulsar.Client | None = None
        self.producer: pulsar.Producer | None = None
        self.consumer: pulsar.Consumer | None = None

    def __enter__(self) -> "PulsarRpcClient":
        # Conecta no broker Pulsar, cria um produtor para requisições e um consumidor para respostas.
        self.client = pulsar.Client(self.pulsar_url)
        # Producer: componente do Pulsar responsável por publicar mensagens em um tópico.
        self.producer = self.client.create_producer(self.request_topic)
        # Consumer: componente do Pulsar responsável por ler mensagens de um tópico.
        self.consumer = self.client.subscribe(
            self.reply_topic,
            subscription_name=f"client-{uuid.uuid4().hex}",
        )
        print(f"Cliente conectado em {self.pulsar_url}")
        print(f"Topico de resposta: {self.reply_topic}")
        return self

    def __exit__(self, _exc_type: object, _exc: object, _tb: object) -> None:
        if self.producer:
            self.producer.close()
        if self.consumer:
            self.consumer.close()
        if self.client:
            self.client.close()

    def call(self, operation: str, payload: dict[str, Any]) -> dict[str, Any]:
        if self.producer is None or self.consumer is None:
            raise RuntimeError("Cliente Pulsar nao inicializado.")

        # O request_id liga a requisição enviada com a resposta recebida depois.
        request_id = uuid.uuid4().hex
        request = Request(
            request_id=request_id,
            operation=operation,
            payload=payload,
            reply_to=self.reply_topic,
        )
        # Publica a requisição no tópico principal consumido pelo servidor.
        # A partition_key ajuda o Pulsar a manter a chave da mensagem associada ao request_id.
        self.producer.send(request.to_bytes(), partition_key=request_id)

        while True:
            # O cliente bloqueia aguardando uma mensagem no seu tópico de resposta.
            msg = self.consumer.receive(timeout_millis=self.timeout_millis)
            try:
                response = Response.from_bytes(msg.data())
                # Ignora mensagens que não pertencem a esta chamada especifica.
                if response.request_id != request_id:
                    self.consumer.acknowledge(msg)
                    continue
                self.consumer.acknowledge(msg)
                return {
                    "request_id": response.request_id,
                    "ok": response.ok,
                    "result": response.result,
                    "error": response.error,
                }
            except Exception:
                # negative_acknowledge avisa ao Pulsar que a mensagem não foi processada corretamente.
                self.consumer.negative_acknowledge(msg)
                raise


def run_demo(rpc: PulsarRpcClient) -> list[dict[str, Any]]:
    # Demonstra as três operacoes principais.
    return [
        rpc.call("echo", {"text": "Mensagem enviada pelo cliente em outra maquina."}),
        rpc.call(
            "write_file",
            {
                "filename": "registro.txt",
                "content": "Alteracao feita pelo cliente via middleware Apache Pulsar.",
                "mode": "append",
            },
        ),
        rpc.call("calculate", {"function": "fibonacci", "args": [12]}),
    ]


def _parse_number(value: str) -> int | float:
    try:
        return int(value)
    except ValueError:
        return float(value)


if __name__ == "__main__":
    main()
