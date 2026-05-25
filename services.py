from database import carregar_ativos, salvar_ativos

def cadastrar_ativo():
    id_ativo = int(input("Digite o ID do ativo: "))
    tipo_ativo = input("Digite o tipo do ativo: ")
    descricao_ativo = input("Digite a descrição do ativo: ")
    localizacao_ativo = input("Digite a localização do ativo: ")
    responsavel_ativo = input("Digite o responsável pelo ativo: ")
    nome_ativo = input("Digite o nome do ativo: ")

    ativo = {"id": id_ativo,
             "tipo": tipo_ativo,
             "descricao": descricao_ativo,
             "localizacao": localizacao_ativo,
             "responsavel": responsavel_ativo,
             "nome": nome_ativo}
    return ativo

def criar_ativo():
    ativos = carregar_ativos()
    novo_ativo = cadastrar_ativo()
    ativos.append(novo_ativo)
    salvar_ativos(ativos)
    print("Ativo cadastrado com sucesso!")

def listar_ativos(ativos):
    if not ativos:
        print("Nenhum ativo cadastrado.")
    else:
        for ativo in ativos:
            print(f"ID: {ativo['id']}, Tipo: {ativo['tipo']}, Descrição: {ativo['descricao']}, Localização: {ativo['localizacao']}, Responsável: {ativo['responsavel']}, Nome: {ativo['nome']}")

def consultar_ativo_por_id(ativos, id_ativo):
    for ativo in ativos:
        if ativo["id"] == id_ativo:
            return ativo
    return None