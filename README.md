# Sistema de Inventário de Segurança

Projeto desenvolvido para a disciplina de Cibersegurança.

## Objetivo

Este projeto tem como objetivo implementar um sistema CRUD em Python para gerenciamento de ativos de TI e vulnerabilidades de segurança associadas a esses ativos.

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
- Remover ativo
- Impedir cadastro de ativos com ID duplicado
- Remover automaticamente as vulnerabilidades associadas ao ativo removido

### Gerenciamento de vulnerabilidades

- Cadastrar vulnerabilidade associada a um ativo existente
- Gerar ID automático para cada vulnerabilidade
- Consultar vulnerabilidades associadas a um ativo
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
