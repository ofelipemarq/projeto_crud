# Sistema de Inventário de Segurança

Projeto desenvolvido para a disciplina de Cibersegurança da UFU.

## Objetivo

Desenvolver um sistema CRUD em Python para gerenciamento de ativos de TI e vulnerabilidades de segurança, utilizando persistência em arquivos JSON, menu textual e organização modular do código.

O sistema permite cadastrar, consultar, atualizar e remover ativos de TI, além de registrar vulnerabilidades associadas a cada ativo.

---

## Funcionalidades

### Ativos de TI

- Cadastrar ativos
- Listar todos os ativos
- Consultar ativo por ID
- Consultar ativo por nome
- Atualizar informações de um ativo
- Remover ativo
- Remover automaticamente as vulnerabilidades associadas ao ativo excluído
- Impedir cadastro de ativo com ID duplicado

### Vulnerabilidades

- Cadastrar vulnerabilidade associada a um ativo existente
- Gerar ID automático para cada vulnerabilidade
- Consultar vulnerabilidades por ID do ativo
- Informar quando um ativo não possui vulnerabilidades cadastradas
- Associar vulnerabilidades aos ativos usando o campo `ativo_id`

### Validações e organização

- Tratamento de entrada inválida para números inteiros
- Validação de campos de texto vazios
- Uso de `Enum` para padronizar:
  - Tipo de ativo
  - Severidade da vulnerabilidade
  - Status de tratamento
- Uso de dicionários e funções genéricas para busca e filtro
- Persistência dos dados em arquivos JSON

---

## Tecnologias utilizadas

- Python 3
- JSON
- Git e GitHub

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