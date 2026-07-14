from database import (
    carregar_ativos,
    salvar_ativos
)

from models import (
    Notebook,
    TipoAtivo,
    criar_equipamento
)


ativo = criar_equipamento(
    tipo=TipoAtivo.NOTEBOOK,
    id=1,
    nome="Notebook Teste",
    descricao="Teste de persistência",
    responsavel="Felipe",
    localizacao="Sala 1"
)

salvar_ativos([ativo])

ativos = carregar_ativos()

print(type(ativos[0]))
print(ativos[0].nome)
print(ativos[0].tipo)