from database import carregar_ativos
from services import criar_vulnerabilidade, atualizar_ativo, criar_ativo, listar_ativos, consultar_ativo_por_id, remover_ativo

def exibição_menu():
    print("\n -- SISTEMA DE INVENTÁRIO --")
    print("1. Cadastrar ativo")
    print("2. Listar ativos")
    print("3. Atualizar ativo")
    print("4. Excluir ativo")
    print ("5. Cadastrar vulnerabilidade")
    print("6. Listar vulnerabilidades")
    print("7. Consultar ativo por ID")
    print("0. Sair")

while True:
    exibição_menu()
    escolha = input("Escolha uma opção: ")

    if escolha == "1":
        print("Opção 1 selecionada: Cadastrar ativo")
        criar_ativo()

    elif escolha == "2":
        print("Opção 2 selecionada: Listar ativos")
        listar_ativos(carregar_ativos())
        
    elif escolha == "3":
        print("Opção 3 selecionada: Atualizar ativo")
        id_ativo = int(input("Digite o ID do ativo: "))
        atualizar_ativo(carregar_ativos(), id_ativo)

    elif escolha == "4":
        print("Opção 4 selecionada: Excluir ativo")
        id_ativo = int(input("Digite o ID do ativo: "))
        remover_ativo(carregar_ativos(), id_ativo)

    elif escolha == "5":
        print("Opção 5 selecionada: Cadastrar vulnerabilidade")
        id_ativo = int(input("Digite o ID do ativo: "))
        criar_vulnerabilidade(carregar_ativos(), id_ativo) 
    elif escolha == "6":
        print("Opção 6 selecionada: Listar vulnerabilidades")

    elif escolha == "7":
        print("Opção 7 selecionada: Consultar ativo por ID")
        id_ativo = int(input("Digite o ID do ativo: "))
        ativo = consultar_ativo_por_id(carregar_ativos(), id_ativo)
        if ativo:
            print(f"ID: {ativo['id']}, Tipo: {ativo['tipo']}, Descrição: {ativo['descricao']}, Localização: {ativo['localizacao']}, Responsável: {ativo['responsavel']}, Nome: {ativo['nome']}")
        else:
            print("Ativo não encontrado.")

    elif escolha == "0":
        print("Saindo do sistema. Até logo!")
        break
    else:
        print("Opção inválida. Por favor, tente novamente.")
    