# Sistema de Inventário de Segurança

Projeto acadêmico desenvolvido em Python para gerenciamento de ativos de TI e vulnerabilidades associadas.

A aplicação funciona por linha de comando, utiliza arquivos JSON como persistência e foi estruturada com orientação a objetos. Também pode ser executada em container Docker, com persistência dos dados fora do container.

---

## Sumário

- [Objetivo](#objetivo)
- [Funcionalidades](#funcionalidades)
- [Tecnologias utilizadas](#tecnologias-utilizadas)
- [Conceitos aplicados](#conceitos-aplicados)
- [Arquitetura do projeto](#arquitetura-do-projeto)
- [Estrutura de pastas](#estrutura-de-pastas)
- [Como os dados são armazenados](#como-os-dados-são-armazenados)
- [Como executar localmente](#como-executar-localmente)
- [Como executar com Docker Compose](#como-executar-com-docker-compose)
- [Como acessar o menu do container](#como-acessar-o-menu-do-container)
- [Persistência com Docker](#persistência-com-docker)
- [Como executar no servidor](#como-executar-no-servidor)
- [Testes](#testes)
- [Fluxo de uso](#fluxo-de-uso)
- [Regras de negócio](#regras-de-negócio)
- [Possíveis melhorias futuras](#possíveis-melhorias-futuras)

---

## Objetivo

O objetivo do projeto é disponibilizar um sistema simples de inventário de segurança capaz de:

- cadastrar ativos de TI;
- consultar ativos;
- atualizar ativos;
- remover ativos;
- cadastrar vulnerabilidades;
- relacionar vulnerabilidades a ativos existentes;
- atualizar o tratamento das vulnerabilidades;
- persistir os dados em arquivos JSON;
- executar localmente ou em container Docker.

O sistema foi desenvolvido para praticar conceitos de Python, CRUD, orientação a objetos, persistência em arquivos, separação de responsabilidades e containerização.

---

## Funcionalidades

### Gerenciamento de ativos

A aplicação permite:

- cadastrar um novo ativo;
- listar todos os ativos cadastrados;
- consultar um ativo pelo ID;
- consultar um ativo pelo nome;
- atualizar o nome do ativo;
- atualizar a descrição;
- atualizar o responsável;
- atualizar a localização;
- atualizar o tipo do ativo;
- remover um ativo;
- gerar IDs automaticamente;
- remover automaticamente as vulnerabilidades ligadas ao ativo removido.

### Tipos de ativos disponíveis

O sistema trabalha com os seguintes tipos:

- `NOTEBOOK`
- `SERVIDOR`
- `ROTEADOR`
- `IMPRESSORA`

Cada tipo é representado por uma subclasse específica de `Equipamento`.

### Gerenciamento de vulnerabilidades

A aplicação permite:

- cadastrar vulnerabilidade associada a um ativo existente;
- listar todas as vulnerabilidades;
- consultar uma vulnerabilidade por ID;
- consultar vulnerabilidades por ID do ativo;
- atualizar o tipo da vulnerabilidade;
- atualizar a descrição;
- atualizar a severidade;
- atualizar o status de tratamento;
- gerar IDs automaticamente;
- impedir o cadastro de vulnerabilidade para ativo inexistente.

### Níveis de severidade

- `BAIXA`
- `MEDIA`
- `ALTA`
- `CRITICA`

### Status de tratamento

- `ABERTA`
- `EM_ANALISE`
- `RESOLVIDA`
- `ACEITA_COMO_RISCO`

---

## Tecnologias utilizadas

- Python 3
- Programação orientada a objetos
- JSON
- Enum
- pathlib
- Docker
- Docker Compose
- Git
- GitHub
- Linux/Fedora
- SSH
- SCP

O projeto utiliza apenas recursos da biblioteca padrão do Python e não depende de bibliotecas externas.

---

## Conceitos aplicados

### Orientação a objetos

O projeto utiliza:

- classes;
- objetos;
- atributos;
- métodos;
- herança;
- polimorfismo;
- associação entre entidades;
- serialização e desserialização.

### Herança

`Equipamento` é a classe-base.

As subclasses são:

```python
Notebook(Equipamento)
Servidor(Equipamento)
Roteador(Equipamento)
Impressora(Equipamento)
```

Essas subclasses reutilizam os atributos e os métodos definidos em `Equipamento`.

### Polimorfismo

Todas as subclasses utilizam os mesmos métodos herdados, como:

```python
atualizar()
to_dict()
```

O método `to_dict()` funciona para qualquer tipo de equipamento e registra automaticamente o tipo correto.

### Associação

A classe `Vulnerabilidade` possui o atributo:

```python
ativo_id
```

Esse atributo relaciona uma vulnerabilidade a um ativo existente.

### Serialização

Antes de salvar, os objetos são convertidos em dicionários:

```text
objeto -> to_dict() -> JSON
```

### Desserialização

Ao carregar os dados:

```text
JSON -> dicionário -> função from_dict() -> objeto
```

Isso permite que o sistema reconstrua corretamente objetos como `Notebook`, `Servidor`, `Roteador` e `Impressora`.

---

## Arquitetura do projeto

O projeto segue uma separação simples de responsabilidades.

### `models.py`

Contém:

- Enums;
- classe `Equipamento`;
- subclasses dos equipamentos;
- classe `Vulnerabilidade`;
- métodos de atualização;
- métodos de conversão para dicionário;
- funções de reconstrução de objetos.

### `database.py`

Responsável por:

- carregar JSON;
- salvar JSON;
- carregar ativos;
- salvar ativos;
- carregar vulnerabilidades;
- salvar vulnerabilidades.

### `services.py`

Contém as regras de negócio:

- cadastro;
- consulta;
- atualização;
- remoção;
- geração de ID;
- busca por campo;
- filtro por campo;
- remoção em cascata.

### `main.py`

Responsável por:

- exibir o menu;
- receber entradas do usuário;
- chamar os serviços;
- exibir os resultados;
- controlar o fluxo principal da aplicação.

### `utils.py`

Contém funções auxiliares para:

- ler números inteiros;
- validar entradas;
- impedir texto vazio;
- exibir e selecionar opções de Enum.

---

## Estrutura de pastas

```text
projeto_crud/
├── main.py
├── models.py
├── services.py
├── database.py
├── utils.py
├── README.md
├── Dockerfile
├── compose.yaml
├── .dockerignore
├── data/
│   ├── ativos.json
│   └── vulnerabilidades.json
└── testes/
```

---

## Como os dados são armazenados

Os dados ficam nos arquivos:

```text
data/ativos.json
data/vulnerabilidades.json
```

### Exemplo de ativo

```json
[
    {
        "id": 1,
        "nome": "Notebook do setor financeiro",
        "tipo": "NOTEBOOK",
        "descricao": "Equipamento utilizado pela equipe financeira",
        "responsavel": "Maria",
        "localizacao": "Sala 10"
    }
]
```

### Exemplo de vulnerabilidade

```json
[
    {
        "id": 1,
        "ativo_id": 1,
        "tipo": "Sistema desatualizado",
        "descricao": "O sistema operacional está sem atualizações recentes",
        "severidade": "ALTA",
        "status_tratamento": "ABERTA"
    }
]
```

---

## Como executar localmente

### Pré-requisitos

- Python 3 instalado;
- terminal;
- arquivos JSON dentro da pasta `data`.

### Execução

Na raiz do projeto:

```bash
python main.py
```

Em alguns sistemas:

```bash
python3 main.py
```

---

## Menu da aplicação

Ao iniciar, será exibido:

```text
=== SISTEMA DE INVENTÁRIO ===
1. Cadastrar ativo
2. Listar ativos
3. Consultar ativo por ID
4. Consultar ativo por nome
5. Atualizar ativo
6. Remover ativo
7. Cadastrar vulnerabilidade
8. Listar vulnerabilidades
9. Consultar vulnerabilidades por ativo
10. Atualizar vulnerabilidade
0. Sair
```

---

## Como executar com Docker Compose

### Pré-requisitos

- Docker instalado;
- Docker Compose disponível.

Verifique:

```bash
docker --version
docker compose version
```

### Validar a configuração

```bash
docker compose config
```

### Construir a imagem

```bash
docker compose build
```

### Iniciar o container

```bash
docker compose up -d
```

### Verificar o estado

```bash
docker compose ps
```

### Ver os logs

```bash
docker compose logs
```

### Encerrar o container

```bash
docker compose down
```

---

## Dockerfile

Exemplo utilizado no projeto:

```dockerfile
FROM python:3.13-slim

WORKDIR /app

COPY . .

CMD ["python", "main.py"]
```

### Explicação

- `FROM`: define a imagem-base;
- `WORKDIR`: define a pasta de trabalho;
- `COPY`: copia o projeto;
- `CMD`: inicia a aplicação.

---

## compose.yaml

Exemplo:

```yaml
services:
  projeto-crud:
    build: .
    image: projeto-crud:1.0
    container_name: projeto-crud
    stdin_open: true
    tty: true
    restart: unless-stopped
    volumes:
      - ./data:/app/data
```

### Explicação

- `build: .`: usa o Dockerfile da raiz;
- `image`: define o nome da imagem;
- `container_name`: define o nome do container;
- `stdin_open`: mantém a entrada aberta;
- `tty`: cria um terminal interativo;
- `restart`: reinicia automaticamente;
- `volumes`: conecta a pasta local de dados à pasta interna do container.

---

## Como acessar o menu do container

Com o container em execução:

```bash
docker attach projeto-crud
```

Para desconectar sem encerrar:

```text
Ctrl + P
Ctrl + Q
```

Não selecione a opção `0` se o objetivo for manter o container em execução, pois essa opção encerra o processo principal.

---

## Persistência com Docker

O volume:

```yaml
volumes:
  - ./data:/app/data
```

faz a ligação:

```text
computador ou servidor            container
./data                     <->    /app/data
```

Assim, os dados permanecem fora do container.

Mesmo que o container seja removido, os arquivos JSON continuam armazenados na pasta `data`.

---

## Como executar no servidor

A imagem pode ser construída localmente, exportada e enviada ao servidor.

### Exportar a imagem

```bash
docker image save projeto-crud:1.0 \
  | gzip > projeto-crud-1.0.tar.gz
```

### Gerar hash

```bash
sha256sum projeto-crud-1.0.tar.gz \
  > projeto-crud-1.0.tar.gz.sha256
```

### Enviar ao servidor

```bash
scp projeto-crud-1.0.tar.gz \
    projeto-crud-1.0.tar.gz.sha256 \
    USUARIO@SERVIDOR:~/projeto-crud-deploy/
```

### Enviar os JSONs

```bash
scp data/ativos.json \
    data/vulnerabilidades.json \
    USUARIO@SERVIDOR:~/projeto-crud-deploy/data/
```

### Carregar a imagem no servidor

```bash
docker image load -i projeto-crud-1.0.tar.gz
```

### Criar o container no servidor

```bash
docker run -dit \
  --name projeto-crud \
  --restart unless-stopped \
  --mount type=bind,src="$HOME/projeto-crud-deploy/data",dst=/app/data \
  projeto-crud:1.0
```

### Verificar

```bash
docker ps --filter name=projeto-crud
```

```bash
docker inspect projeto-crud \
  --format='Status={{.State.Status}} | Início={{.State.StartedAt}} | Reinícios={{.RestartCount}}'
```

---

## Testes

### Compilação

```bash
python -m compileall .
```

### Testes automatizados

```bash
python -m unittest discover -s testes -v
```

### Testes recomendados

#### Ativos

- cadastrar;
- listar;
- consultar por ID;
- consultar por nome;
- atualizar cada campo;
- atualizar o tipo;
- remover;
- validar geração automática de ID.

#### Vulnerabilidades

- cadastrar;
- impedir cadastro em ativo inexistente;
- listar;
- consultar por ativo;
- atualizar tipo;
- atualizar descrição;
- atualizar severidade;
- atualizar status.

#### Persistência

- cadastrar dados;
- fechar a aplicação;
- abrir novamente;
- verificar se os dados continuam disponíveis.

#### Remoção em cascata

Ao remover um ativo, todas as vulnerabilidades vinculadas a ele também devem ser removidas.

---

## Fluxo de uso

### Cadastro de ativo

```text
usuário informa os dados
-> main.py recebe
-> AtivoServicos valida e cria
-> models.py gera o objeto
-> database.py salva no JSON
```

### Consulta

```text
usuário informa ID ou nome
-> serviço carrega os objetos
-> busca o ativo
-> main.py exibe o resultado
```

### Atualização do tipo

A mudança de tipo não altera apenas o Enum.

O sistema cria um novo objeto da subclasse correta, preservando:

- ID;
- nome;
- descrição;
- responsável;
- localização.

Exemplo:

```text
Notebook -> Servidor
```

O objeto passa realmente a ser uma instância de `Servidor`.

### Remoção em cascata

```text
ativo removido
-> vulnerabilidades carregadas
-> vulnerabilidades ligadas ao ativo são removidas
-> os dois arquivos JSON são atualizados
```

---

## Regras de negócio

- todo ativo possui ID único;
- toda vulnerabilidade possui ID único;
- vulnerabilidade só pode ser cadastrada em ativo existente;
- remover um ativo remove suas vulnerabilidades;
- o tipo do ativo deve corresponder à sua subclasse;
- entradas vazias não são aceitas;
- opções inválidas não encerram a aplicação;
- os dados devem permanecer válidos após reinicialização.

---

## Possíveis melhorias futuras

- interface web;
- API REST com FastAPI;
- banco de dados relacional;
- autenticação de usuários;
- controle de permissões;
- histórico de alterações;
- filtros avançados;
- relatórios;
- exportação para CSV;
- dashboard;
- testes automatizados mais abrangentes;
- logging;
- validação de esquema JSON;
- deploy automatizado.

---

