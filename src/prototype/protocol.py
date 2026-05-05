from __future__ import annotations

import json
from dataclasses import dataclass
from typing import Any


@dataclass(frozen=True)
class Request:
    # Mensagem enviada pelo cliente para pedir uma operação ao servidor.
    request_id: str
    operation: str
    payload: dict[str, Any]
    reply_to: str

    def to_bytes(self) -> bytes:
        # Serializa a requisição em JSON para trafegar pelo Apache Pulsar.
        # O Pulsar transporta bytes; por isso o objeto Python precisa virar JSON codificado.
        return json.dumps(
            {
                "request_id": self.request_id,
                "operation": self.operation,
                "payload": self.payload,
                "reply_to": self.reply_to,
            },
            ensure_ascii=True,
        ).encode("utf-8")

    @classmethod
    def from_bytes(cls, raw: bytes) -> "Request":
        # Reconstrui a requisição recebida pelo servidor a partir dos bytes da mensagem.
        # Esta conversão separa a camada de mensageria da regra de negócio.
        data = json.loads(raw.decode("utf-8"))
        return cls(
            request_id=str(data["request_id"]),
            operation=str(data["operation"]),
            payload=dict(data.get("payload") or {}),
            reply_to=str(data["reply_to"]),
        )


@dataclass(frozen=True)
class Response:
    # Mensagem devolvida pelo servidor com sucesso, resultado ou erro.
    request_id: str
    ok: bool
    result: Any = None
    error: str | None = None

    def to_bytes(self) -> bytes:
        # Serializa a resposta para publicar no tópico reply_to do cliente.
        # Assim a resposta usa o mesmo padrão de mensagem da requisição.
        return json.dumps(
            {
                "request_id": self.request_id,
                "ok": self.ok,
                "result": self.result,
                "error": self.error,
            },
            ensure_ascii=True,
        ).encode("utf-8")

    @classmethod
    def from_bytes(cls, raw: bytes) -> "Response":
        # Reconstrui a resposta recebida pelo cliente.
        data = json.loads(raw.decode("utf-8"))
        return cls(
            request_id=str(data["request_id"]),
            ok=bool(data["ok"]),
            result=data.get("result"),
            error=data.get("error"),
        )
