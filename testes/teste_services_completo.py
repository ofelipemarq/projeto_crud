from models import TipoAtivo
from services import AtivoServicos


servicos = AtivoServicos()


novo_ativo = servicos.cadastrar_ativo(
    nome="Servidor de teste",
    descricao="Servidor usado nos testes",
    responsavel="Felipe",
    localizacao="Laboratório",
    tipo=TipoAtivo.SERVIDOR
)

print("Cadastrado:")
servicos.exibir_ativo(novo_ativo)


print("\nConsulta por ID:")
ativo = servicos.consultar_ativo_por_id(
    novo_ativo.id
)

servicos.exibir_ativo(ativo)


print("\nAtualizando:")
resultado = servicos.atualizar_ativo(
    novo_ativo.id,
    localizacao="Datacenter"
)

print(resultado)


print("\nApós atualização:")
ativo = servicos.consultar_ativo_por_id(
    novo_ativo.id
)

servicos.exibir_ativo(ativo)


print("\nRemovendo:")
resultado = servicos.remover_ativo(
    novo_ativo.id
)

print(resultado)