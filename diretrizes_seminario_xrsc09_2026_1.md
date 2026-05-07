# XRSC09 – Sistemas Distribuídos

## Diretrizes para o Seminário – 1º Semestre de 2026

**Universidade Federal de Itajubá**  
**Instituto de Matemática e Computação**  
**Disciplina:** XRSC09 – Sistemas Distribuídos  
**Professor:** Rafael Frinhani

---

## 1. Objetivo dos Seminários

Seminários são atividades acadêmicas de curta duração cujo objetivo é apresentar de forma didática e estruturada um tópico de pesquisa ou tecnologia, permitindo aos estudantes explorar e compartilhar conhecimentos sobre um novo tema.

Cada grupo deverá realizar um seminário sobre um método de comunicação ou coordenação em sistemas distribuídos. O objetivo é proporcionar aos alunos o contato teórico e prático com tecnologias de middleware e paradigmas de comunicação distribuída, que poderão ser utilizados no desenvolvimento do projeto da disciplina.

A turma será organizada em **6 grupos**:

- 3 grupos com 4 integrantes;
- 3 grupos com 5 integrantes.

Cada grupo apresentará uma tecnologia específica, definida por sorteio, abordando seus fundamentos, arquitetura, funcionamento e aplicações.

---

## 2. Temas dos Seminários

| Tema | Tecnologia | Paradigma |
|---|---|---|
| 1 | Protocol Buffers + gRPC | Remote Procedure Call |
| 2 | RabbitMQ (AMQP) | Message Queue |
| 3 | Apache Pulsar | Mensageria / Streaming |
| 4 | NATS | Cloud-Native Messaging |
| 5 | Redis | Data Sharing / PubSub |
| 6 | ZeroMQ | Brokerless Messaging |

Cada tema corresponde a uma tecnologia de comunicação distribuída, sendo uma oportunidade para os alunos conhecerem abordagens distintas usadas em sistemas distribuídos modernos.

Além da tecnologia, o seminário também precisa debater o paradigma de comunicação ao qual ela pertence, destacando vantagens, limitações e cenários de uso.

---

## 3. Conteúdo Mínimo da Documentação

A documentação deverá explorar, no mínimo, os itens a seguir, não se restringindo a eles.

### 3.1 Fundamentação Conceitual

- Paradigma de comunicação distribuída;
- Problema que o middleware procura resolver;
- Breve histórico e contexto de uso.

### 3.2 Evidências Técnicas

- Modelagem da solução;
- Diagramas da arquitetura;
- Fluxo de comunicação;
- Trechos relevantes do código fonte;
- Bibliotecas utilizadas;
- Parâmetros e configurações;
- Demonstração do funcionamento;
- Evidências de execução do sistema.

### 3.3 Arquitetura da Tecnologia

- Arquitetura do middleware;
- Principais componentes;
- Modelo de comunicação;
- Padrão de interação;
- Modelo de consistência, se aplicável.

### 3.4 Avaliação Crítica

- Vantagens e limitações;
- Cenários em que a tecnologia é adequada;
- Cenários em que a tecnologia não é recomendada.

### 3.5 Uso Prático

- Bibliotecas e ferramentas disponíveis;
- Linguagens suportadas;
- Exemplos de aplicações reais.

---

## 4. Protótipo Prático

Além da apresentação teórica, como um dos requisitos do protótipo deverá ser demonstrada a comunicação entre processos distribuídos utilizando o middleware.

O protótipo deverá conter pelo menos uma das opções abaixo:

1. Um cliente e um servidor; ou
2. Dois serviços distribuídos que interajam entre si.

A comunicação deverá ocorrer entre os equipamentos, devendo ser máquinas físicas diferentes.

### 4.1 Operações Obrigatórias do Servidor

O servidor deverá implementar três operações básicas:

1. Resposta a uma mensagem de texto;
2. Alteração de um arquivo texto no servidor;
3. Cálculo de uma ou mais funções.

### 4.2 Funcionamento do Cliente

O cliente deverá enviar solicitações ao servidor, que executará a operação e retornará a resposta.

### 4.3 Possibilidades Adicionais

Além das operações obrigatórias, o protótipo pode incluir:

- Múltiplos serviços;
- Filas de mensagens;
- Eventos;
- Processamento assíncrono.

---

## 5. Linguagens Permitidas

As seguintes linguagens são permitidas:

- C;
- C++;
- C#;
- Java;
- Python;
- Go;
- Javascript;
- React;
- React Native;
- Dart.

No tema **“1. Protocol Buffers”**, é obrigatório considerar no mínimo duas linguagens distintas.

O grupo deverá consultar previamente o professor caso deseje utilizar outra linguagem.

---

## 6. Relatório, Slides e Materiais

Deverão ser elaborados o relatório e os slides que abordem o conteúdo sobre a tecnologia e os demais itens descritos anteriormente.

Também deverão ser incluídos detalhes da preparação do ambiente de desenvolvimento e uso, por exemplo:

- Parâmetros;
- Configuração das variáveis de ambiente;
- Principais comandos do método.

Como material adicional, são bem-vindos:

- Links de resumos;
- Apostilas;
- Exercícios;
- Modelos;
- Vídeos;
- Outros artefatos que possibilitem o aprendizado da tecnologia apresentada.

Esses materiais poderão ser utilizados pelos demais alunos após o seminário.

---

## 7. Entregas

As entregas previstas são:

- Relatório do Middleware, usando o template LaTeX em PDF, com máximo de 6 páginas, incluindo capa e contracapa;
- Slides da apresentação no formato `.ppt`, `.pptx` ou `.pdf`;
- Código fonte do protótipo implementado;
- Seminário de 15 a 20 minutos;
- Apresentação presencial de todos os integrantes;
- Disponibilização da documentação no repositório GitHub do seminário.

### 7.1 Datas Importantes

| Item | Data / Informação |
|---|---|
| Data da apresentação | 08/05 |
| Ordem das apresentações | Sorteada |
| Data de entrega | Até 07/05 às 23h59 |
| Entrega no SIGAA | Apenas o relatório |
| Documentação completa | Repositório GitHub do seminário |

O link do GitHub deverá ser incluído no relatório.

---

## 8. Organização dos Papéis e Responsabilidades

Conforme a metodologia de Ensino Baseada em Projetos, ou **Project-Based Learning (PjBL)**, é necessária a definição prévia dos papéis e responsabilidades de cada integrante do grupo.

Essa organização busca assegurar:

- Participação ativa e equilibrada de todos;
- Equilíbrio na carga de trabalho;
- Aprendizagem colaborativa;
- Maior robustez técnica da solução desenvolvida.

Cada atividade crítica deverá envolver no mínimo dois integrantes:

- Um responsável principal;
- Um corresponsável.

---

## 9. Papéis dos Integrantes

## Membro 1 – Coordenador do Seminário e Integração

### Responsabilidade Principal

Garantir a organização do trabalho do grupo e a coerência técnica entre os diferentes componentes do seminário.

### Responsabilidades Específicas

- Planejar e atualizar o cronograma do seminário;
- Distribuir tarefas entre os integrantes do grupo;
- Acompanhar o andamento das atividades e prazos;
- Mediar decisões técnicas e organizacionais;
- Centralizar a comunicação com o docente;
- Integrar o conteúdo produzido pelos membros do grupo;
- Organizar a estrutura final da apresentação.

### Responsabilidade Compartilhada

- Revisão técnica dos slides;
- Apoio à preparação da demonstração do protótipo;
- Apoio à organização do material didático entregue.

---

## Membro 2 – Analista da Tecnologia e do Paradigma

### Responsabilidade Principal

Compreender e explicar os fundamentos da tecnologia e do paradigma de comunicação distribuída abordado no seminário.

### Responsabilidades Específicas

- Estudar o funcionamento do middleware selecionado;
- Identificar o paradigma de comunicação associado, como RPC, mensageria, streaming etc.;
- Elaborar o referencial conceitual do seminário;
- Descrever a arquitetura da tecnologia;
- Identificar cenários de uso reais;
- Apresentar vantagens, limitações e aplicações da tecnologia.

### Responsabilidade Compartilhada

- Apoio à modelagem da arquitetura do protótipo;
- Apoio à análise e interpretação dos resultados obtidos na demonstração.

---

## Membro 3 – Arquiteto do Protótipo

### Responsabilidade Principal

Projetar a arquitetura do protótipo demonstrativo e definir a estrutura da comunicação distribuída.

### Responsabilidades Específicas

- Definir a arquitetura do sistema distribuído demonstrado;
- Identificar os componentes do sistema, como cliente, servidor, serviços, filas etc.;
- Modelar o fluxo de comunicação entre os processos;
- Definir bibliotecas, ferramentas e dependências necessárias;
- Elaborar diagramas da arquitetura do sistema.

### Responsabilidade Compartilhada

- Apoio à implementação do protótipo;
- Apoio à documentação técnica do funcionamento do sistema.

---

## Membro 4 – Desenvolvedor do Protótipo

### Responsabilidade Principal

Implementar o protótipo demonstrativo utilizando o middleware estudado.

### Responsabilidades Específicas

- Implementar a aplicação cliente e servidor;
- Configurar o ambiente de execução da tecnologia;
- Implementar as operações exigidas no protótipo;
- Integrar as bibliotecas e dependências necessárias;
- Garantir o funcionamento da comunicação entre os processos distribuídos.

### Responsabilidade Compartilhada

- Apoio à realização de testes do sistema;
- Apoio à preparação da demonstração durante o seminário.

---

## Membro 5 – Avaliação Experimental e Demonstração

> Aplicável apenas para grupos de 5 integrantes.

### Responsabilidade Principal

Avaliar o funcionamento do protótipo e preparar a demonstração técnica durante o seminário.

### Responsabilidades Específicas

- Executar testes do sistema distribuído implementado;
- Validar o funcionamento da comunicação entre os processos;
- Registrar evidências de execução do protótipo;
- Preparar o roteiro de demonstração do sistema;
- Explicar o fluxo de comunicação durante a apresentação.

### Responsabilidade Compartilhada

- Apoio à análise crítica da tecnologia;
- Apoio à elaboração dos slides e do material didático.

---

## 10. Organização Recomendada do Trabalho

## Etapa 1 – Estudo da Tecnologia e do Paradigma

O grupo deverá estudar a tecnologia atribuída, compreender seu paradigma de comunicação distribuída e identificar seus principais conceitos, arquitetura e aplicações.

**Responsável Principal:** Membro 2  
**Com apoio de:** Membro 1

### Atividades Típicas

- Estudo da documentação da tecnologia;
- Identificação do paradigma de comunicação;
- Levantamento de exemplos de uso;
- Análise da arquitetura do middleware;
- Elaboração do conteúdo conceitual da apresentação.

---

## Etapa 2 – Arquitetura e Modelagem do Protótipo

Deve-se definir a arquitetura do protótipo que demonstrará o funcionamento do middleware.

**Responsável Principal:** Membro 3  
**Com apoio de:** Membro 2

### Atividades Típicas

- Definição dos componentes do sistema;
- Modelagem do fluxo de comunicação entre processos;
- Definição do papel de cliente e servidor;
- Seleção das bibliotecas e ferramentas;
- Elaboração de diagramas da arquitetura.

---

## Etapa 3 – Implementação do Protótipo

Esta etapa visa o desenvolvimento do sistema demonstrativo utilizando a tecnologia estudada.

### Grupos com 4 integrantes

**Responsável Principal:** Membro 4  
**Com apoio de:** Membro 3

### Grupos com 5 integrantes

**Responsáveis Principais:** Membro 3 e Membro 4

### Atividades Típicas

- Configuração do ambiente de desenvolvimento;
- Implementação do cliente e servidor;
- Integração do middleware;
- Implementação das operações do protótipo;
- Execução e testes iniciais.

---

## Etapa 4 – Avaliação e Demonstração

Esta etapa visa validar o funcionamento do protótipo e preparar a demonstração que será realizada no seminário.

### Grupos com 4 integrantes

**Responsável Principal:** Membro 4  
**Com apoio de:** Membro 2

### Grupos com 5 integrantes

**Responsável Principal:** Membro 5  
**Com apoio de:** Membro 2 e Membro 3

### Atividades Típicas

- Execução de testes do sistema;
- Validação da comunicação distribuída;
- Registro de evidências de funcionamento;
- Preparação do roteiro de demonstração;
- Identificação de limitações e observações técnicas.

---

## Etapa 5 – Preparação do Seminário

Esta etapa envolve a consolidação do material e a preparação da apresentação.

**Responsável Principal:** Membro 1  
**Com apoio de:** Todos os demais membros

### Atividades Típicas

- Organização dos slides;
- Revisão técnica do conteúdo;
- Preparação da demonstração;
- Ensaio da apresentação.

---

## 11. Observações Finais

- Toda a documentação, incluindo relatório, slides, código e demais materiais, deverá estar disponível no GitHub do projeto do seminário.
- No relatório deverá constar o link do projeto no GitHub.
- Apenas o relatório deverá ser entregue pelo link disponível no SIGAA.
- É suficiente o envio por apenas um dos integrantes.
- Entregas realizadas fora do prazo estabelecido não serão consideradas, implicando atribuição de nota zero à atividade para todo o grupo.
- O template em LaTeX deverá ser obtido no SIGAA.
- Recomenda-se a utilização da plataforma Overleaf para edição colaborativa do documento.
- Recomenda-se a utilização do modelo de slides apresentado em “Rethinking the Design of Presentation Slides” e “The Craft of the Scientific Presentations”, disponível no SIGAA, por adotar princípios de comunicação visual mais adequados à apresentação técnica e científica.
- Ao final do relatório, deverá constar de forma explícita os papéis e responsabilidades atribuídos a cada integrante do grupo.

Embora existam responsabilidades definidas para cada membro, o trabalho é colaborativo. Todos os integrantes devem:

- Compreender o funcionamento da tecnologia estudada;
- Participar da elaboração do material;
- Estar preparados para apresentar o seminário.

O trabalho é em grupo, mas a avaliação é individual, considerando a contribuição de cada um para o desenvolvimento do trabalho.
