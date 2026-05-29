


def ler_inteiro(mensagem):
    while True:
        try:
            valor = int(input(mensagem))
            return valor
        except ValueError:
            print("Entrada inválida. Por favor, digite um número inteiro.")

def ler_texto(mensagem):
    while True:
        texto = input(mensagem).strip()
        if texto:
            return texto
        else:
            print("Entrada inválida. Por favor, digite um texto.")

def escolher_opcao_enum(enum_class, mensagem):
    print(mensagem)
    for item in enum_class:
        print(f"{item.value}. {item.name.capitalize()}")
    while True:
        try:
            escolha = int(input("Escolha uma opção: "))
            if escolha in [item.value for item in enum_class]:
                return enum_class(escolha)
            else:
                print("Opção inválida. Por favor, escolha uma opção válida.")
        except ValueError:
            print("Entrada inválida. Por favor, digite um número inteiro correspondente à opção.")