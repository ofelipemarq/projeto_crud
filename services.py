from database import carregar_ativos, salvar_ativos, salvar_vulnerabilidades, carregar_vulnerabilidades

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

def atualizar_ativo(ativos, id_ativo):
    ativo = consultar_ativo_por_id(ativos, id_ativo)
    if ativo:
        print (ativo)
        alteracao = input("Digite o campo que deseja alterar (tipo, descricao, localizacao, responsavel, nome): ")
        if alteracao in ativo:
            novo_valor = input(f"Digite o novo valor para {alteracao}: ")
            ativo[alteracao] = novo_valor
            salvar_ativos(ativos)
            print("Ativo atualizado com sucesso!")
        else:
            print("Campo inválido.")
    else:
        print("Ativo não encontrado.")  

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

def remover_ativo(ativos, id_ativo):
    ativo = consultar_ativo_por_id(ativos, id_ativo)
    if ativo:
        print(ativo)
        confirmacao = input("Tem certeza que deseja excluir este ativo? (s/n): ")
        if confirmacao.lower() == "s":
            ativos.remove(ativo)
            salvar_ativos(ativos)
            print("Ativo excluído com sucesso!")
        else:
            print("Exclusão cancelada.")
    else:
        print("Ativo não encontrado.")  

def cadastrar_vulnerabilidade(ativos, id_ativo):
    ativo = consultar_ativo_por_id(ativos, id_ativo)
    if ativo:
        tipo_vulnerabilidade = input("Digite o tipo da vulnerabilidade: ")
        severidade_vulnerabilidade = input("Digite a severidade da vulnerabilidade: ")
        descricao_vulnerabilidade = input("Digite a descrição da vulnerabilidade: ")
        status_de_tratamento = input("Digite o status de tratamento da vulnerabilidade: ")
        vulnerabilidade = {"id do ativo": id_ativo,
                            "tipo": tipo_vulnerabilidade,
                           "severidade": severidade_vulnerabilidade,
                           "descricao": descricao_vulnerabilidade,
                           "status_de_tratamento": status_de_tratamento}
        return vulnerabilidade
    else:
        print("Ativo não encontrado.")
        return None 
    
def criar_vulnerabilidade(ativos, id_ativo):
    vulnerabilidades = carregar_vulnerabilidades()
    nova_vulnerabilidade = cadastrar_vulnerabilidade(ativos, id_ativo)
    if nova_vulnerabilidade:
        vulnerabilidades.append(nova_vulnerabilidade)
        salvar_vulnerabilidades(vulnerabilidades)
        print("Vulnerabilidade cadastrada com sucesso!")

def buscar_vulnerabilidades_por_ativo(vulnerabilidades, id_ativo, ativos):
    id_ativo = int(input("Digite o ID do ativo para buscar suas vulnerabilidades: "))
    if consultar_ativo_por_id(ativos, id_ativo):
        
    
