from __future__ import annotations

import os
import signal
from pathlib import Path

import pulsar

from prototype.operations import execute_operation
from prototype.protocol import Request, Response


PULSAR_URL = os.getenv("PULSAR_URL", "pulsar://localhost:6650")
# Topico central do Apache Pulsar onde chegam todas as requisicoes dos clientes.
REQUEST_TOPIC = os.getenv("REQUEST_TOPIC", "persistent://public/default/prototype-requests")
SERVER_FILE_DIR = Path(os.getenv("SERVER_FILE_DIR", "server_data"))


def main() -> None:
    # Flag usada para encerrar o loop principal de forma controlada.
    stop = False

    def handle_signal(signum: int, _frame: object) -> None:
        nonlocal stop
        print(f"Encerrando servidor. Sinal recebido: {signum}", flush=True)
        stop = True

    signal.signal(signal.SIGINT, handle_signal)
    signal.signal(signal.SIGTERM, handle_signal)

    # Garante que a pasta onde o servidor grava arquivos exista antes de atender clientes.
    SERVER_FILE_DIR.mkdir(parents=True, exist_ok=True)
    # Cliente Pulsar usado pelo servidor para conversar com o broker.
    client = pulsar.Client(PULSAR_URL)
    # O servidor assina o tópico de requisicoes. Shared permite escalar com mais servidores.
    # Em modo Shared, o Pulsar distribui as mensagens entre consumidores da mesma assinatura.
    consumer = client.subscribe(
        REQUEST_TOPIC,
        subscription_name="prototype-server",
        consumer_type=pulsar.ConsumerType.Shared,
    )
    # Cache de produtores para reutilizar conexões com os tópicos de resposta dos clientes.
    producers: dict[str, pulsar.Producer] = {}

    print(f"Servidor conectado em {PULSAR_URL}", flush=True)
    print(f"Aguardando solicitacoes no topico {REQUEST_TOPIC}", flush=True)

    try:
        while not stop:
            try:
                msg = consumer.receive(timeout_millis=1000)
            except pulsar.Timeout:
                continue

            try:
                # Converte a mensagem recebida do Pulsar para o objeto de protocolo do projeto.
                request = Request.from_bytes(msg.data())
                print(
                    f"Recebido {request.operation} id={request.request_id} "
                    f"reply_to={request.reply_to}",
                    flush=True,
                )
                # Executa a regra de negocio solicitada pelo cliente.
                result = execute_operation(request.operation, request.payload, SERVER_FILE_DIR)
                response = Response(request_id=request.request_id, ok=True, result=result)
            except Exception as exc:
                # Se algo falhar, o servidor devolve uma resposta de erro em vez de travar.
                request_id = "desconhecido"
                reply_to = None
                try:
                    parsed = Request.from_bytes(msg.data())
                    request_id = parsed.request_id
                    reply_to = parsed.reply_to
                except Exception:
                    pass
                response = Response(request_id=request_id, ok=False, error=str(exc))
                if reply_to is None:
                    print(f"Mensagem invalida sem topico de resposta: {exc}", flush=True)
                    consumer.acknowledge(msg)
                    continue
            else:
                reply_to = request.reply_to

            # Envia a resposta para o tópico informado pelo cliente no campo reply_to.
            producer = producers.get(reply_to)
            if producer is None:
                # Cria um producer dinâmico para o tópico de resposta criado pelo cliente.
                producer = client.create_producer(reply_to)
                producers[reply_to] = producer
            # A resposta tambem trafega pelo Pulsar, mantendo cliente e servidor desacoplados.
            producer.send(response.to_bytes())
            # acknowledge confirma ao Pulsar que a requisição foi processada com sucesso.
            consumer.acknowledge(msg)
    finally:
        for producer in producers.values():
            producer.close()
        consumer.close()
        client.close()


if __name__ == "__main__":
    main()
