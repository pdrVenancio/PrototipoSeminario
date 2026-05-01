from __future__ import annotations

import json
from dataclasses import dataclass
from typing import Any


@dataclass(frozen=True)
class Request:
    request_id: str
    operation: str
    payload: dict[str, Any]
    reply_to: str

    def to_bytes(self) -> bytes:
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
        data = json.loads(raw.decode("utf-8"))
        return cls(
            request_id=str(data["request_id"]),
            operation=str(data["operation"]),
            payload=dict(data.get("payload") or {}),
            reply_to=str(data["reply_to"]),
        )


@dataclass(frozen=True)
class Response:
    request_id: str
    ok: bool
    result: Any = None
    error: str | None = None

    def to_bytes(self) -> bytes:
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
        data = json.loads(raw.decode("utf-8"))
        return cls(
            request_id=str(data["request_id"]),
            ok=bool(data["ok"]),
            result=data.get("result"),
            error=data.get("error"),
        )
