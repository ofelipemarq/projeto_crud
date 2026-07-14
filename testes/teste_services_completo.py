from models import (
    TipoAtivo,
    Severidade,
    StatusTratamento
)

from services import (
    AtivoServicos,
    VulnerabilidadeServicos
)


ativo_servicos = AtivoServicos()
vulnerabilidade_servicos = VulnerabilidadeServicos()


print("\n=== TESTE 1: CADASTRAR ATIVOS ===")

ativo_1 = ativo_servicos.cadastrar_ativo(
    nome="Servidor Principal",
    descricao="Servidor usado pela aplicação",
    responsavel="Felipe",
    localizacao="Datacenter",
    tipo=TipoAtivo.SERVIDOR
)

print(f"Ativo criado com ID: {ativo_1.id}")
print(f"Classe criada: {type(ativo_1).__name__}")


ativo_2 = ativo_servicos.cadastrar_ativo(
    nome="Notebook Administrativo",
    descricao="Notebook da equipe administrativa",
    responsavel="Ana",
    localizacao="Sala 2",
    tipo=TipoAtivo.NOTEBOOK
)

print(f"Ativo criado com ID: {ativo_2.id}")
print(f"Classe criada: {type(ativo_2).__name__}")


print("\n=== TESTE 2: CONSULTAR ATIVO POR ID ===")

ativo_encontrado = ativo_servicos.consultar_ativo_por_id(
    ativo_1.id
)

if ativo_encontrado is not None:
    print("Ativo encontrado:")
    ativo_servicos.exibir_ativo(ativo_encontrado)
else:
    print("ERRO: ativo não encontrado.")


print("\n=== TESTE 3: CONSULTAR ATIVO POR NOME ===")

ativo_encontrado = ativo_servicos.consultar_ativo_por_nome(
    "Notebook Administrativo"
)

if ativo_encontrado is not None:
    print("Ativo encontrado:")
    ativo_servicos.exibir_ativo(ativo_encontrado)
else:
    print("ERRO: ativo não encontrado.")


print("\n=== TESTE 4: ATUALIZAR ATIVO ===")

resultado_atualizacao = ativo_servicos.atualizar_ativo(
    id_ativo=ativo_1.id,
    responsavel="Carlos",
    localizacao="Datacenter 2"
)

print(f"Atualização realizada: {resultado_atualizacao}")

ativo_atualizado = ativo_servicos.consultar_ativo_por_id(
    ativo_1.id
)

if ativo_atualizado is not None:
    ativo_servicos.exibir_ativo(ativo_atualizado)


print("\n=== TESTE 5: CADASTRAR VULNERABILIDADES ===")

vulnerabilidade_1 = (
    vulnerabilidade_servicos.cadastrar_vulnerabilidade(
        ativo_id=ativo_1.id,
        tipo="Software desatualizado",
        descricao="Sistema operacional sem atualizações recentes",
        severidade=Severidade.ALTA,
        status_tratamento=StatusTratamento.ABERTA
    )
)

print(
    "Vulnerabilidade criada com ID: "
    f"{vulnerabilidade_1.id}"
)


vulnerabilidade_2 = (
    vulnerabilidade_servicos.cadastrar_vulnerabilidade(
        ativo_id=ativo_1.id,
        tipo="Senha fraca",
        descricao="Conta administrativa usa senha fraca",
        severidade=Severidade.CRITICA,
        status_tratamento=StatusTratamento.EM_ANALISE
    )
)

print(
    "Vulnerabilidade criada com ID: "
    f"{vulnerabilidade_2.id}"
)


vulnerabilidade_3 = (
    vulnerabilidade_servicos.cadastrar_vulnerabilidade(
        ativo_id=ativo_2.id,
        tipo="Antivírus desatualizado",
        descricao="Antivírus precisa ser atualizado",
        severidade=Severidade.MEDIA,
        status_tratamento=StatusTratamento.ABERTA
    )
)

print(
    "Vulnerabilidade criada com ID: "
    f"{vulnerabilidade_3.id}"
)


print("\n=== TESTE 6: CONSULTAR VULNERABILIDADES POR ATIVO ===")

vulnerabilidades_servidor = (
    vulnerabilidade_servicos
    .consultar_vulnerabilidades_por_ativo_id(
        ativo_1.id
    )
)

print(
    "Quantidade encontrada: "
    f"{len(vulnerabilidades_servidor)}"
)

for vulnerabilidade in vulnerabilidades_servidor:
    vulnerabilidade_servicos.exibir_vulnerabilidade(
        vulnerabilidade
    )
    print("-" * 20)


print("\n=== TESTE 7: ATUALIZAR VULNERABILIDADE ===")

resultado_atualizacao = (
    vulnerabilidade_servicos.atualizar_vulnerabilidade(
        id_vulnerabilidade=vulnerabilidade_1.id,
        severidade=Severidade.CRITICA,
        status_tratamento=StatusTratamento.RESOLVIDA
    )
)

print(
    "Atualização realizada: "
    f"{resultado_atualizacao}"
)

vulnerabilidade_atualizada = (
    vulnerabilidade_servicos
    .consultar_vulnerabilidade_por_id(
        vulnerabilidade_1.id
    )
)

if vulnerabilidade_atualizada is not None:
    vulnerabilidade_servicos.exibir_vulnerabilidade(
        vulnerabilidade_atualizada
    )


print("\n=== TESTE 8: ATIVO INEXISTENTE ===")

try:
    vulnerabilidade_servicos.cadastrar_vulnerabilidade(
        ativo_id=999999,
        tipo="Teste inválido",
        descricao="Este cadastro não deve acontecer",
        severidade=Severidade.BAIXA,
        status_tratamento=StatusTratamento.ABERTA
    )

    print("ERRO: vulnerabilidade foi cadastrada indevidamente.")

except ValueError as erro:
    print(f"Erro esperado capturado: {erro}")


print("\n=== TESTE 9: REMOÇÃO EM CASCATA ===")

resultado_remocao = ativo_servicos.remover_ativo(
    ativo_1.id
)

print(f"Ativo removido: {resultado_remocao}")

ativo_removido = ativo_servicos.consultar_ativo_por_id(
    ativo_1.id
)

vulnerabilidades_restantes = (
    vulnerabilidade_servicos
    .consultar_vulnerabilidades_por_ativo_id(
        ativo_1.id
    )
)

print(f"Consulta do ativo removido: {ativo_removido}")

print(
    "Vulnerabilidades restantes do ativo removido: "
    f"{len(vulnerabilidades_restantes)}"
)


print("\n=== TESTE 10: PRESERVAR OUTROS ATIVOS ===")

ativo_2_ainda_existe = (
    ativo_servicos.consultar_ativo_por_id(
        ativo_2.id
    )
)

vulnerabilidades_ativo_2 = (
    vulnerabilidade_servicos
    .consultar_vulnerabilidades_por_ativo_id(
        ativo_2.id
    )
)

print(
    "Segundo ativo ainda existe: "
    f"{ativo_2_ainda_existe is not None}"
)

print(
    "Vulnerabilidades do segundo ativo: "
    f"{len(vulnerabilidades_ativo_2)}"
)


print("\n=== FIM DOS TESTES ===")


























































































































































































































































