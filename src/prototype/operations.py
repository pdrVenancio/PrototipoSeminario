from __future__ import annotations

import math
from pathlib import Path
from typing import Any


def execute_operation(operation: str, payload: dict[str, Any], file_dir: Path) -> Any:
    # Ponto central que decide qual operação remota o servidor deve executar.
    if operation == "echo":
        return echo(payload)
    if operation == "write_file":
        return write_file(payload, file_dir)
    if operation == "calculate":
        return calculate(payload)
    raise ValueError(f"Operacao desconhecida: {operation}")


def echo(payload: dict[str, Any]) -> dict[str, str]:
    text = str(payload.get("text", ""))
    return {"message": f"Servidor recebeu: {text}"}


def write_file(payload: dict[str, Any], file_dir: Path) -> dict[str, Any]:
    # Operação que altera um arquivo no servidor a partir de uma mensagem remota.
    filename = str(payload.get("filename", "server.txt")).strip() or "server.txt"
    content = str(payload.get("content", ""))
    mode = str(payload.get("mode", "append")).lower()

    # Valida o caminho para evitar escrita fora da pasta controlada pelo servidor.
    path = _safe_text_path(file_dir, filename)
    path.parent.mkdir(parents=True, exist_ok=True)

    if mode == "replace":
        path.write_text(content, encoding="utf-8")
    elif mode == "append":
        with path.open("a", encoding="utf-8") as handle:
            handle.write(content)
            if not content.endswith("\n"):
                handle.write("\n")
    else:
        raise ValueError("Modo invalido para arquivo. Use 'append' ou 'replace'.")

    return {
        "filename": path.name,
        "path": str(path),
        "bytes": path.stat().st_size,
        "preview": path.read_text(encoding="utf-8")[-500:],
    }


def calculate(payload: dict[str, Any]) -> dict[str, Any]:
    # Operação de cálculo remoto: o cliente envia a função e os argumentos.
    function = str(payload.get("function", "add")).lower()
    args = payload.get("args", [])
    if not isinstance(args, list):
        raise ValueError("'args' deve ser uma lista de numeros.")

    numbers = [_as_number(value) for value in args]
    result: int | float

    if function == "add":
        result = sum(numbers)
    elif function == "subtract":
        _require_count(numbers, 2, function)
        result = numbers[0] - numbers[1]
    elif function == "multiply":
        result = math.prod(numbers)
    elif function == "divide":
        _require_count(numbers, 2, function)
        if numbers[1] == 0:
            raise ValueError("Divisao por zero.")
        result = numbers[0] / numbers[1]
    elif function == "power":
        _require_count(numbers, 2, function)
        result = numbers[0] ** numbers[1]
    elif function == "sqrt":
        _require_count(numbers, 1, function)
        if numbers[0] < 0:
            raise ValueError("Raiz quadrada exige numero nao negativo.")
        result = math.sqrt(numbers[0])
    elif function == "factorial":
        _require_count(numbers, 1, function)
        n = _as_non_negative_int(numbers[0], function)
        result = math.factorial(n)
    elif function == "fibonacci":
        _require_count(numbers, 1, function)
        n = _as_non_negative_int(numbers[0], function)
        result = _fibonacci(n)
    else:
        raise ValueError(
            "Funcao desconhecida. Use add, subtract, multiply, divide, power, "
            "sqrt, factorial ou fibonacci."
        )

    return {"function": function, "args": numbers, "result": result}


def _safe_text_path(file_dir: Path, filename: str) -> Path:
    # Proteção básica: aceita apenas arquivos .txt dentro do diretório do servidor.
    file_dir = file_dir.resolve()
    candidate = (file_dir / filename).resolve()
    if file_dir not in candidate.parents and candidate != file_dir:
        raise ValueError("Nome de arquivo invalido: caminho fora do diretorio do servidor.")
    if candidate.suffix and candidate.suffix.lower() != ".txt":
        raise ValueError("Apenas arquivos .txt sao permitidos.")
    if not candidate.suffix:
        candidate = candidate.with_suffix(".txt")
    return candidate


def _as_number(value: Any) -> int | float:
    # Normaliza argumentos vindos do JSON para int ou float.
    if isinstance(value, bool):
        raise ValueError("Booleanos nao sao numeros validos para calculo.")
    if isinstance(value, (int, float)):
        return value
    try:
        text = str(value)
        return int(text) if text.isdigit() or text.startswith("-") and text[1:].isdigit() else float(text)
    except ValueError as exc:
        raise ValueError(f"Valor numerico invalido: {value!r}") from exc


def _require_count(numbers: list[int | float], count: int, function: str) -> None:
    if len(numbers) != count:
        raise ValueError(f"A funcao {function} exige {count} argumento(s).")


def _as_non_negative_int(value: int | float, function: str) -> int:
    if int(value) != value or value < 0:
        raise ValueError(f"A funcao {function} exige inteiro nao negativo.")
    return int(value)


def _fibonacci(n: int) -> int:
    previous, current = 0, 1
    for _ in range(n):
        previous, current = current, previous + current
    return previous
