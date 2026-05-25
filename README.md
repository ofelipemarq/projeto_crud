# Sistema de Inventário de Segurança

Projeto desenvolvido para a disciplina de Cibersegurança da UFU.

## Objetivo

Desenvolver um sistema CRUD em Python para gerenciamento de ativos de TI e vulnerabilidades de segurança, utilizando persistência em arquivos JSON e organização modular do código.

## Funcionalidades implementadas

### Ativos
- Cadastro de ativos
- Listagem de ativos
- Consulta de ativos por ID
- Persistência dos dados em JSON

### Estrutura do Projeto

```text
projeto_crud/
│
├── main.py
├── services.py
├── database.py
├── models.py
├── utils.py
│
└── data/
    ├── ativos.json
    └── vulnerabilidades.json