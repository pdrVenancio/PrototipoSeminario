# Resultado dos Testes E2E do Protótipo (Apache Pulsar)

Data: 2026-05-04  
Projeto: PrototipoSeminario  
Objetivo: Validar o funcionamento fim-a-fim do protótipo cliente/servidor usando Apache Pulsar.

## 1) Ambiente de execução

- Docker Client: `20.10.23`
- Docker Server (Docker Desktop): `20.10.23`
- Compose: `v2.15.1`
- Stack iniciada com:

```powershell
docker compose --profile server up --build
```

## 2) Plano de testes executado

- T1: Operação obrigatória `echo` (mensagem de texto)
- T2: Operação obrigatória `write_file` (alteração de arquivo no servidor)
- T3: Operação obrigatória `calculate` (cálculo de função)
- T4: Cenário de erro controlado (`calculate` com função inválida)
- T5: Evidência de processamento no servidor (logs com `request_id` e `reply_to`)
- T6: Evidência de persistência no servidor (`server_data/registro_e2e.txt`)

## 3) Execução e resultados

### T1 - Echo

Comando:

```powershell
docker compose --profile client run --rm client python -m prototype.client echo --text "Teste E2E: conectividade"
```

Resultado relevante:

```json
{
  "request_id": "1e3c60d0c0834751bebafa4129599f88",
  "ok": true,
  "result": {
    "message": "Servidor recebeu: Teste E2E: conectividade"
  },
  "error": null
}
```

Status: **PASS**

### T2 - Write file

Comando:

```powershell
docker compose --profile client run --rm client python -m prototype.client write_file --filename registro_e2e.txt --content "Linha de validacao E2E" --mode append
```

Resultado relevante:

```json
{
  "request_id": "74590c1196984ed8b0f6d3e624f175d0",
  "ok": true,
  "result": {
    "filename": "registro_e2e.txt",
    "path": "/data/registro_e2e.txt",
    "bytes": 23,
    "preview": "Linha de validacao E2E\n"
  },
  "error": null
}
```

Status: **PASS**

### T3 - Calculate

Comando:

```powershell
docker compose --profile client run --rm client python -m prototype.client calculate --function multiply --args 6 7
```

Resultado relevante:

```json
{
  "request_id": "4d3703fbed624f64a4d546f58b49eba9",
  "ok": true,
  "result": {
    "function": "multiply",
    "args": [6, 7],
    "result": 42
  },
  "error": null
}
```

Status: **PASS**

### T4 - Erro controlado

Comando:

```powershell
docker compose --profile client run --rm client python -m prototype.client calculate --function invalida --args 1 2
```

Resultado relevante:

```json
{
  "request_id": "7da01d2195ca42f8b6c679deeb3233bb",
  "ok": false,
  "result": null,
  "error": "Funcao desconhecida. Use add, subtract, multiply, divide, power, sqrt, factorial ou fibonacci."
}
```

Status: **PASS** (comportamento esperado de falha tratada)

## 4) Evidências de processamento no servidor

Logs do servidor registraram recebimento das requisições:

- `Recebido echo id=1e3c60d0c0834751bebafa4129599f88 ...`
- `Recebido write_file id=74590c1196984ed8b0f6d3e624f175d0 ...`
- `Recebido calculate id=4d3703fbed624f64a4d546f58b49eba9 ...`
- `Recebido calculate id=7da01d2195ca42f8b6c679deeb3233bb ...` (teste de erro)

## 5) Evidências de persistência de arquivo

- Arquivo gerado: `server_data/registro_e2e.txt`
- Conteúdo:

```text
Linha de validacao E2E
```

## 6) Conclusão

O protótipo foi validado fim-a-fim com Apache Pulsar em execução.  
As três operações obrigatórias funcionaram corretamente (`echo`, `write_file`, `calculate`) e o cenário de erro retornou resposta estruturada com `ok=false`.  
Os logs confirmam o fluxo request/reply com `request_id` e `reply_to`, e a escrita em arquivo foi persistida no diretório do servidor.
