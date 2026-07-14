# Sistema de Inventário de Segurança

Projeto desenvolvido para a disciplina de Cibersegurança.

## Objetivo

Sistema CRUD em Python para gerenciamento de ativos de TI e vulnerabilidades de segurança associadas a esses ativos.

O sistema permite cadastrar, consultar, atualizar e remover ativos, além de cadastrar e visualizar vulnerabilidades vinculadas a um ativo específico.

Os dados são persistidos em arquivos JSON, funcionando como uma base de dados simples em arquivo texto.

---

## Funcionalidades

### Gerenciamento de ativos

- Cadastrar ativo de TI
- Listar ativos cadastrados
- Consultar ativo por ID
- Consultar ativo por nome
- Atualizar informações de um ativo
- Atualizar o tipo do ativo, preservando seu ID e os demais dados
- Remover ativo
- Remover automaticamente as vulnerabilidades associadas ao ativo removido
- Gerar ID automático para cada ativo

### Gerenciamento de vulnerabilidades

- Cadastrar vulnerabilidade associada a um ativo existente
- Gerar ID automático para cada vulnerabilidade
- Listar vulnerabilidades cadastradas
- Consultar vulnerabilidades associadas a um ativo
- Atualizar tipo, descrição, severidade e status de tratamento
- Informar quando um ativo não possui vulnerabilidades cadastradas
- Impedir cadastro de vulnerabilidade para ativo inexistente

### Validações

- Tratamento de entradas numéricas inválidas
- Validação de campos de texto vazios
- Uso de opções padronizadas com `Enum`
- Verificação de existência de ativos antes de atualizar, remover ou cadastrar vulnerabilidades

---

## Tecnologias utilizadas

- Python 3
- JSON
- Git
- GitHub

---

## Estrutura do projeto

```text
projeto_crud/
│
├── main.py
├── services.py
├── database.py
├── models.py
├── utils.py
├── README.md
│
└── data/
    ├── ativos.json
    └── vulnerabilidades.json
```

## Arquitetura

- `models.py`: contém as entidades e os Enums.
- `database.py`: realiza a persistência nos arquivos JSON.
- `services.py`: contém as regras de negócio.
- `main.py`: contém o menu, as entradas e a exibição das mensagens.
- `utils.py`: contém as validações das entradas.

## Orientação a objetos

`Equipamento` é a classe-base dos ativos. `Notebook`, `Servidor`, `Roteador`
e `Impressora` herdam seus dados e comportamentos, mas cada subclasse possui
um `TipoAtivo` diferente. O método `to_dict()` funciona com todas elas.

`Vulnerabilidade` é uma entidade separada e se relaciona com um equipamento
por meio do atributo `ativo_id`.

## Persistência

Antes de salvar, os objetos são convertidos para dicionários:

```text
objeto -> to_dict() -> JSON
```

Ao carregar, os dicionários são reconstruídos como objetos:

```text
JSON -> dicionário -> from_dict() -> objeto
```

Os arquivos continuam armazenando listas de objetos JSON.

## Execução

```bash
python main.py
```

## Testes

```bash
python -m unittest discover -s testes -v
```
