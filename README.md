# Prototipo distribuído com Python 3.10 e Apache Pulsar

Este projeto demonstra comunicação entre processos distribuídos usando Apache Pulsar como middleware. O servidor implementa tres operações:

- resposta a uma mensagem de texto;
- alteração de um arquivo texto no servidor;
- cálculo de funções matemáticas.

O cliente envia uma solicitação para um tópico de requests e informa um tópico de resposta. O servidor consome a solicitação, executa a operação e publica a resposta no tópico indicado pelo cliente.

## Requisitos

- Docker com suporte a Linux containers.
- Portas liberadas na máquina do broker: `6650` para clientes Pulsar e `8080` para administração HTTP.

## Teste rápido em uma máquina

Suba o Pulsar e o servidor:

```powershell
docker compose --profile server up --build
```

Em outro terminal, execute o cliente de demonstração:

```powershell
docker compose --profile client run --rm client
```

O cliente executa as três operações obrigatorias automaticamente.

## Demonstração entre máquinas físicas

Considere:

- Máquina A: roda o broker Pulsar.
- Máquina B: roda o servidor Python.
- Máquina C ou A: roda o cliente Python.

Na Máquina A, descubra o IP na rede local e crie um arquivo `.env` com:

```env
PULSAR_ADVERTISED_ADDRESS=IP_DA_MAQUINA_A
PULSAR_URL=pulsar://IP_DA_MAQUINA_A:6650
REQUEST_TOPIC=persistent://public/default/prototype-requests
```

Suba apenas o broker:

```powershell
docker compose up pulsar
```

Na Máquina B, copie o projeto, crie o `.env` apontando para a Máquina A e suba somente o servidor:

```powershell
docker compose --profile server up --build server
```

Na máquina do cliente, copie o projeto, use o mesmo `.env` e execute somente o cliente:

```powershell
docker compose --profile client run --rm client
```

Se o servidor estiver na Máquina B e o cliente em outra máquina, a comunicação passa pelo Pulsar na Máquina A, atendendo ao requisito de processos distribuídos em equipamentos físicos diferentes.

## Comandos do cliente

Mensagem de texto:

```powershell
docker compose --profile client run --rm client python -m prototype.client echo --text "Ola servidor"
```

Alteração de arquivo no servidor:

```powershell
docker compose --profile client run --rm client python -m prototype.client write_file --filename registro.txt --content "Nova linha remota" --mode append
```

Cálculo:

```powershell
docker compose --profile client run --rm client python -m prototype.client calculate --function multiply --args 6 7
```

Funções disponíveis: `add`, `subtract`, `multiply`, `divide`, `power`, `sqrt`, `factorial` e `fibonacci`.

## Estrutura

- `docker-compose.yml`: broker Pulsar, servidor e cliente.
- `Dockerfile`: imagem Python 3.10 para cliente e servidor.
- `src/prototype/server.py`: processo servidor.
- `src/prototype/client.py`: processo cliente.
- `src/prototype/operations.py`: regras das tres operações.
- `server_data/`: pasta montada no servidor para armazenar arquivos alterados.

## Mais Informações

Na maquina cliente é possivel acessar:

- Para listar tópicos:
`http://localhost:8080/admin/v2/persistent/public/default`

- Status e mais informações:
`http://localhost:8080/admin/v2/persistent/public/default/prototype-requests/stats`

## Fontes oficiais consultadas

- [Apache Pulsar: standalone em Docker](https://pulsar.apache.org/docs/en/standalone-docker/)
- [Apache Pulsar: Python client](https://pulsar.apache.org/docs/client-libraries/python/)
- [PyPI: pulsar-client 3.10.0](https://pypi.org/project/pulsar-client/)
