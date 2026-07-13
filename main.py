from services import AtivoServicos
from utils import ler_inteiro
ativo_servicos = AtivoServicos()

def exibir_menu():
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
    exibir_menu()
    escolha = input("Escolha uma opção: ")

    if escolha == "1":
        print("Opção 1 selecionada: Cadastrar ativo")
        ativo_servicos.cadastrar_ativo()

    elif escolha == "2":
        print("Opção 2 selecionada: Listar ativos")
        ativo_servicos.listar_ativos()

    elif escolha == "3":
        print("Opção 3 selecionada: Atualizar ativo")
        ativo_servicos.atualizar_ativo(id_ativo=ler_inteiro("Digite o ID do ativo a ser atualizado: "))

    elif escolha == "4":
        print("Opção 4 selecionada: Excluir ativo")
        ativo_servicos.remover_ativo(id_ativo=ler_inteiro("Digite o ID do ativo a ser removido: "))

    elif escolha == "5":
        print("Opção 5 selecionada: Cadastrar vulnerabilidade")
       

    elif escolha == "6":
        print("Opção 6 selecionada: Consultar vulnerabilidades por ID do ativo")
        

    elif escolha == "7":
        print("Opção 7 selecionada: Consultar ativo por ID")
       
    
    elif escolha == "8":
        print("Opção 8 selecionada: Consultar ativo por nome")
       

    elif escolha == "0":
        print("Saindo do sistema. Até logo!")
        break
    else:
        print("Opção inválida. Por favor, tente novamente.")
    
