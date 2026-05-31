from database import carregar_ativos, salvar_ativos, salvar_vulnerabilidades, carregar_vulnerabilidades
from utils import ler_texto, ler_inteiro, escolher_opcao_enum
from models import TipoAtivo , Severidade, StatusTratamento


def buscar_por_campo(lista, campo, valor):
    indice = {
        item[campo]: item
        for item in lista
        if campo in item
    }

    return indice.get(valor)

def filtrar_por_campo(lista, campo, valor):
    resultado = []

    for item in lista:
        if item.get(campo) == valor:
            resultado.append(item)

    return resultado


def gerar_proximo_id(lista):
    if not lista:
        return 1

    maior_id = 0

    for item in lista:
        if item["id"] > maior_id:
            maior_id = item["id"]

    return maior_id + 1


def cadastrar_ativo():
    id_ativo = ler_inteiro("Digite o ID do ativo: ")
    tipo_ativo = escolher_opcao_enum(TipoAtivo, "Escolha o tipo do ativo: ")
    descricao_ativo = ler_texto("Digite a descrição do ativo: ")
    localizacao_ativo = ler_texto("Digite a localização do ativo: ")
    responsavel_ativo = ler_texto("Digite o responsável pelo ativo: ")
    nome_ativo = ler_texto("Digite o nome do ativo: ")

    ativo = {
        "id": id_ativo,
        "tipo": tipo_ativo.name,
        "descricao": descricao_ativo,
        "localizacao": localizacao_ativo,
        "responsavel": responsavel_ativo,
        "nome": nome_ativo
    }

    return ativo


def criar_ativo():
    ativos = carregar_ativos()
    novo_ativo = cadastrar_ativo()

    ativo_existente = consultar_ativo_por_id(ativos, novo_ativo["id"])
    if ativo_existente:
        print("Já existe um ativo com este ID. Por favor, escolha um ID diferente.")
        return

    ativos.append(novo_ativo)
    salvar_ativos(ativos)

    print("Ativo cadastrado com sucesso!")


def listar_ativos(ativos):
    if not ativos:
        print("Nenhum ativo cadastrado.")
        return

    for ativo in ativos:
        exibir_ativo(ativo)

def listar_ativos_por_fluxo():
    ativos = carregar_ativos()
    listar_ativos(ativos)


def exibir_ativo(ativo):
    print(
        f"ID: {ativo['id']}, "
        f"Tipo: {ativo['tipo']}, "
        f"Descrição: {ativo['descricao']}, "
        f"Localização: {ativo['localizacao']}, "
        f"Responsável: {ativo['responsavel']}, "
        f"Nome: {ativo['nome']}"
    )


def consultar_ativo_por_id(ativos, id_ativo):
    return buscar_por_campo(ativos, "id", id_ativo)


def exibir_ativo_por_id():
    ativos = carregar_ativos()
    id_ativo = ler_inteiro("Digite o ID do ativo: ")

    ativo = consultar_ativo_por_id(ativos, id_ativo)

    if ativo:
        exibir_ativo(ativo)
    else:
        print("Ativo não encontrado.")


def atualizar_ativo(ativos, id_ativo):
    ativo = consultar_ativo_por_id(ativos, id_ativo)

    if not ativo:
        print("Ativo não encontrado.")
        return

    exibir_ativo(ativo)

    alteracao = ler_texto(
        "Digite o campo que deseja alterar "
        "(tipo, descricao, localizacao, responsavel, nome): "
    )

    if alteracao == "tipo":
        novo_valor = escolher_opcao_enum(TipoAtivo, "Escolha o novo tipo do ativo: ")
        ativo[alteracao] = novo_valor.name

    elif alteracao in ativo and alteracao != "id":
        novo_valor = ler_texto(f"Digite o novo valor para {alteracao}: ")
        ativo[alteracao] = novo_valor

    else:
        print("Campo inválido.")
        return

    salvar_ativos(ativos)
    print("Ativo atualizado com sucesso!")



def atualizar_ativo_por_fluxo():
    ativos = carregar_ativos()
    id_ativo = ler_inteiro("Digite o ID do ativo: ")

    atualizar_ativo(ativos, id_ativo)


def remover_ativo(ativos, id_ativo):
    ativo = consultar_ativo_por_id(ativos, id_ativo)

    if not ativo:
        print("Ativo não encontrado.")
        return

    exibir_ativo(ativo)

    confirmacao = ler_texto("Tem certeza que deseja excluir este ativo? (s/n): ")

    if confirmacao.lower() == "s":
        vulnerabilidades = carregar_vulnerabilidades()

        vulnerabilidades_atualizadas = [
            vulnerabilidade
            for vulnerabilidade in vulnerabilidades
            if vulnerabilidade["ativo_id"] != id_ativo
        ]

        ativos.remove(ativo)
        salvar_ativos(ativos)
        salvar_vulnerabilidades(vulnerabilidades_atualizadas)

        print("Ativo e suas vulnerabilidades associadas excluídos com sucesso!")
    else:
        print("Exclusão cancelada.")


def remover_ativo_por_fluxo():
    ativos = carregar_ativos()
    id_ativo = ler_inteiro("Digite o ID do ativo: ")
   
    remover_ativo(ativos, id_ativo)


def cadastrar_vulnerabilidade(ativos, id_ativo, vulnerabilidades):
    ativo = consultar_ativo_por_id(ativos, id_ativo)

    if not ativo:
        print("Ativo não encontrado.")
        return None

    tipo_vulnerabilidade = ler_texto("Digite o tipo da vulnerabilidade: ")

    severidade_vulnerabilidade = escolher_opcao_enum(
        Severidade,
        "Escolha a severidade da vulnerabilidade: "
    )

    descricao_vulnerabilidade = ler_texto("Digite a descrição da vulnerabilidade: ")

    status_de_tratamento = escolher_opcao_enum(
        StatusTratamento,
        "Escolha o status de tratamento da vulnerabilidade: "
    )

    vulnerabilidade = {
        "id": gerar_proximo_id(vulnerabilidades),
        "ativo_id": id_ativo,
        "tipo": tipo_vulnerabilidade,
        "severidade": severidade_vulnerabilidade.name,
        "descricao": descricao_vulnerabilidade,
        "status_de_tratamento": status_de_tratamento.name,
    }

    return vulnerabilidade


def criar_vulnerabilidade(ativos, id_ativo):
    vulnerabilidades = carregar_vulnerabilidades()
    
    nova_vulnerabilidade = cadastrar_vulnerabilidade(
        ativos,
        id_ativo,
        vulnerabilidades
    )

    if nova_vulnerabilidade:
        vulnerabilidades.append(nova_vulnerabilidade)
        salvar_vulnerabilidades(vulnerabilidades)
        print("Vulnerabilidade cadastrada com sucesso!")


def criar_vulnerabilidade_por_fluxo():
    ativos = carregar_ativos()
    id_ativo = ler_inteiro("Digite o ID do ativo: ")

    criar_vulnerabilidade(ativos, id_ativo)


def consultar_vulnerabilidades_por_ativo(vulnerabilidades, id_ativo):
    return filtrar_por_campo(vulnerabilidades, "ativo_id", id_ativo)


def exibir_vulnerabilidade(vulnerabilidade):
    print(f"ID: {vulnerabilidade['id']}")
    print(f"Tipo: {vulnerabilidade['tipo']}")
    print(f"Severidade: {vulnerabilidade['severidade']}")
    print(f"Descrição: {vulnerabilidade['descricao']}")
    print(f"Status: {vulnerabilidade['status_de_tratamento']}")
    print("-" * 50)


def exibir_vulnerabilidades_por_ativo():
    ativos = carregar_ativos()
    vulnerabilidades = carregar_vulnerabilidades()

    id_ativo = ler_inteiro("Digite o ID do ativo: ")

    ativo = consultar_ativo_por_id(ativos, id_ativo)

    if not ativo:
        print("Ativo não encontrado.")
        return

    vulnerabilidades_do_ativo = consultar_vulnerabilidades_por_ativo(
        vulnerabilidades,
        id_ativo
    )

    print(f"\nVulnerabilidades associadas ao ativo {ativo['nome']} (ID {id_ativo}):")
    print("-" * 50)

    if not vulnerabilidades_do_ativo:
        print("Este ativo está sem vulnerabilidades registradas.")
        return

    for vulnerabilidade in vulnerabilidades_do_ativo:
        exibir_vulnerabilidade(vulnerabilidade)


def consultar_ativo_por_nome(ativos, nome_ativo):
    return buscar_por_campo(ativos, "nome", nome_ativo)

def exibir_ativo_por_nome():
    ativos = carregar_ativos()
    nome_ativo = ler_texto("Digite o nome do ativo: ")

    ativo = consultar_ativo_por_nome(ativos, nome_ativo)

    if ativo:
        exibir_ativo(ativo)
    else:
        print("Ativo não encontrado.")

