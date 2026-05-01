# Prototipo distribuido com Python 3.10 e Apache Pulsar

Este projeto demonstra comunicacao entre processos distribuidos usando Apache Pulsar como middleware. O servidor implementa tres operacoes:

- resposta a uma mensagem de texto;
- alteracao de um arquivo texto no servidor;
- calculo de funcoes matematicas.

O cliente envia uma solicitacao para um topico de requests e informa um topico de resposta. O servidor consome a solicitacao, executa a operacao e publica a resposta no topico indicado pelo cliente.

## Requisitos

- Docker com suporte a Linux containers.
- Portas liberadas na maquina do broker: `6650` para clientes Pulsar e `8080` para administracao HTTP.
- Pelo menos duas maquinas fisicas na mesma rede para a demonstracao exigida.

## Teste rapido em uma maquina

Suba o Pulsar e o servidor:

```powershell
docker compose --profile server up --build
```

Em outro terminal, execute o cliente de demonstracao:

```powershell
docker compose --profile client run --rm client
```

O cliente executa as tres operacoes obrigatorias automaticamente.

## Demonstracao entre maquinas fisicas

Considere:

- Maquina A: roda o broker Pulsar.
- Maquina B: roda o servidor Python.
- Maquina C ou A: roda o cliente Python.

Na Maquina A, descubra o IP na rede local e crie um arquivo `.env` com:

```env
PULSAR_ADVERTISED_ADDRESS=IP_DA_MAQUINA_A
PULSAR_URL=pulsar://IP_DA_MAQUINA_A:6650
REQUEST_TOPIC=persistent://public/default/prototype-requests
```

Suba apenas o broker:

```powershell
docker compose up pulsar
```

Na Maquina B, copie o projeto, crie o `.env` apontando para a Maquina A e suba somente o servidor:

```powershell
docker compose --profile server up --build server
```

Na maquina do cliente, copie o projeto, use o mesmo `.env` e execute somente o cliente:

```powershell
docker compose --profile client run --rm client
```

Se o servidor estiver na Maquina B e o cliente em outra maquina, a comunicacao passa pelo Pulsar na Maquina A, atendendo ao requisito de processos distribuidos em equipamentos fisicos diferentes.

## Comandos do cliente

Mensagem de texto:

```powershell
docker compose --profile client run --rm client python -m prototype.client echo --text "Ola servidor"
```

Alteracao de arquivo no servidor:

```powershell
docker compose --profile client run --rm client python -m prototype.client write_file --filename registro.txt --content "Nova linha remota" --mode append
```

Calculo:

```powershell
docker compose --profile client run --rm client python -m prototype.client calculate --function multiply --args 6 7
```

Funcoes disponiveis: `add`, `subtract`, `multiply`, `divide`, `power`, `sqrt`, `factorial` e `fibonacci`.

## Estrutura

- `docker-compose.yml`: broker Pulsar, servidor e cliente.
- `Dockerfile`: imagem Python 3.10 para cliente e servidor.
- `src/prototype/server.py`: processo servidor.
- `src/prototype/client.py`: processo cliente.
- `src/prototype/operations.py`: regras das tres operacoes.
- `server_data/`: pasta montada no servidor para armazenar arquivos alterados.

## Fontes oficiais consultadas

- [Apache Pulsar: standalone em Docker](https://pulsar.apache.org/docs/en/standalone-docker/)
- [Apache Pulsar: Python client](https://pulsar.apache.org/docs/client-libraries/python/)
- [PyPI: pulsar-client 3.10.0](https://pypi.org/project/pulsar-client/)
