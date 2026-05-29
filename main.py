from database import carregar_ativos
from services import atualizar_ativo_por_fluxo, exibir_ativo_por_nome, exibir_vulnerabilidades_por_ativo, criar_vulnerabilidade_por_fluxo, criar_ativo, exibir_ativo_por_id, listar_ativos, listar_ativos_por_fluxo, remover_ativo_por_fluxo

def exibição_menu():
    print("\n -- SISTEMA DE INVENTÁRIO --")
    print("1. Cadastrar ativo")
    print("2. Listar ativos")
    print("3. Atualizar ativo")
    print("4. Excluir ativo")
    print("5. Cadastrar vulnerabilidade")
    print("6. Consultar vulnerabilidades por ID do ativo")
    print("7. Consultar ativo por ID")
    print("8. Consultar ativo por nome")
    print("0. Sair")

while True:
    exibição_menu()
    escolha = input("Escolha uma opção: ")

    if escolha == "1":
        print("Opção 1 selecionada: Cadastrar ativo")
        criar_ativo()

    elif escolha == "2":
        print("Opção 2 selecionada: Listar ativos")
        listar_ativos_por_fluxo()
        
    elif escolha == "3":
        print("Opção 3 selecionada: Atualizar ativo")
        atualizar_ativo_por_fluxo()

    elif escolha == "4":
        print("Opção 4 selecionada: Excluir ativo")
        remover_ativo_por_fluxo()

    elif escolha == "5":
        print("Opção 5 selecionada: Cadastrar vulnerabilidade")
        criar_vulnerabilidade_por_fluxo()

    elif escolha == "6":
        print("Opção 6 selecionada: Consultar vulnerabilidades por ID do ativo")
        exibir_vulnerabilidades_por_ativo()

    elif escolha == "7":
        print("Opção 7 selecionada: Consultar ativo por ID")
        exibir_ativo_por_id()
    
    elif escolha == "8":
        print("Opção 8 selecionada: Consultar ativo por nome")
        exibir_ativo_por_nome()

    elif escolha == "0":
        print("Saindo do sistema. Até logo!")
        break
    else:
        print("Opção inválida. Por favor, tente novamente.")
    
