def exibição_menu():
    print("\n -- SISTEMA DE INVENTÁRIO --")
    print("1. Cadastrar ativo")
    print("2. Listar ativos")
    print("3. Atualizar ativo")
    print("4. Excluir ativo")
    print ("5. Cadastrar vulnerabilidade")
    print("6. Listar vulnerabilidades")
    print("0. Sair")

while True:
    exibição_menu()
    escolha = input("Escolha uma opção: ")

    if escolha == "1":
        print("Opção 1 selecionada: Cadastrar ativo")
        # Lógica para cadastrar ativo
    elif escolha == "2":
        print("Opção 2 selecionada: Listar ativos")
        # Lógica para listar ativos
    elif escolha == "3":
        print("Opção 3 selecionada: Atualizar ativo")
        # Lógica para atualizar ativo
    elif escolha == "4":
        print("Opção 4 selecionada: Excluir ativo")
        # Lógica para excluir ativo
    elif escolha == "5":
        print("Opção 5 selecionada: Cadastrar vulnerabilidade")
        # Lógica para cadastrar vulnerabilidade
    elif escolha == "6":
        print("Opção 6 selecionada: Listar vulnerabilidades")
        # Lógica para listar vulnerabilidades
    elif escolha == "0":
        print("Saindo do sistema. Até logo!")
        break
    else:
        print("Opção inválida. Por favor, tente novamente.")
    