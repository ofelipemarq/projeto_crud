from models import (
    TipoAtivo,
    Severidade,
    StatusTratamento
)

from services import (
    AtivoServicos,
    VulnerabilidadeServicos
)

from utils import (
    ler_inteiro,
    ler_texto,
    escolher_opcao_enum
)


def exibir_menu():
    print("\n=== SISTEMA DE INVENTÁRIO ===")
    print("1. Cadastrar ativo")
    print("2. Listar ativos")
    print("3. Consultar ativo por ID")
    print("4. Consultar ativo por nome")
    print("5. Atualizar ativo")
    print("6. Remover ativo")
    print("7. Cadastrar vulnerabilidade")
    print("8. Listar vulnerabilidades")
    print("9. Consultar vulnerabilidades por ativo")
    print("10. Atualizar vulnerabilidade")
    print("0. Sair")


def fluxo_cadastrar_ativo():
    print("\n=== CADASTRAR ATIVO ===")

    nome = ler_texto("Digite o nome do ativo: ")
    descricao = ler_texto("Digite a descrição do ativo: ")
    responsavel = ler_texto("Digite o responsável pelo ativo: ")
    localizacao = ler_texto("Digite a localização do ativo: ")

    tipo = escolher_opcao_enum(
        TipoAtivo,
        "Escolha o tipo do ativo:"
    )

    ativo_servicos = AtivoServicos()

    novo_ativo = ativo_servicos.cadastrar_ativo(
        nome=nome,
        descricao=descricao,
        responsavel=responsavel,
        localizacao=localizacao,
        tipo=tipo
    )

    print(
        f"Ativo cadastrado com sucesso! "
        f"ID: {novo_ativo.id}"
    )


def fluxo_listar_ativos():
    print("\n=== LISTAR ATIVOS ===")

    ativo_servicos = AtivoServicos()
    ativo_servicos.listar_ativos()


def fluxo_consultar_ativo_por_id():
    print("\n=== CONSULTAR ATIVO POR ID ===")

    id_ativo = ler_inteiro(
        "Digite o ID do ativo: "
    )

    ativo_servicos = AtivoServicos()

    ativo = ativo_servicos.consultar_ativo_por_id(
        id_ativo
    )

    if ativo:
        ativo_servicos.exibir_ativo(ativo)
    else:
        print("Ativo não encontrado.")


def fluxo_consultar_ativo_por_nome():
    print("\n=== CONSULTAR ATIVO POR NOME ===")

    nome_ativo = ler_texto(
        "Digite o nome do ativo: "
    )

    ativo_servicos = AtivoServicos()

    ativo = ativo_servicos.consultar_ativo_por_nome(
        nome_ativo
    )

    if ativo:
        ativo_servicos.exibir_ativo(ativo)
    else:
        print("Ativo não encontrado.")


def fluxo_atualizar_ativo():
    print("\n=== ATUALIZAR ATIVO ===")

    id_ativo = ler_inteiro(
        "Digite o ID do ativo a ser atualizado: "
    )

    ativo_servicos = AtivoServicos()

    ativo = ativo_servicos.consultar_ativo_por_id(
        id_ativo
    )

    if not ativo:
        print("Ativo não encontrado.")
        return

    ativo_servicos.exibir_ativo(ativo)

    print("\nQual campo deseja atualizar?")
    print("1. Nome")
    print("2. Descrição")
    print("3. Responsável")
    print("4. Localização")

    opcao = ler_inteiro(
        "Escolha uma opção: "
    )

    if opcao == 1:
        novo_nome = ler_texto(
            "Digite o novo nome: "
        )

        resultado = ativo_servicos.atualizar_ativo(
            id_ativo=id_ativo,
            nome=novo_nome
        )

    elif opcao == 2:
        nova_descricao = ler_texto(
            "Digite a nova descrição: "
        )

        resultado = ativo_servicos.atualizar_ativo(
            id_ativo=id_ativo,
            descricao=nova_descricao
        )

    elif opcao == 3:
        novo_responsavel = ler_texto(
            "Digite o novo responsável: "
        )

        resultado = ativo_servicos.atualizar_ativo(
            id_ativo=id_ativo,
            responsavel=novo_responsavel
        )

    elif opcao == 4:
        nova_localizacao = ler_texto(
            "Digite a nova localização: "
        )

        resultado = ativo_servicos.atualizar_ativo(
            id_ativo=id_ativo,
            localizacao=nova_localizacao
        )

    else:
        print("Opção inválida.")
        return

    if resultado:
        print("Ativo atualizado com sucesso.")
    else:
        print("Não foi possível atualizar o ativo.")


def fluxo_remover_ativo():
    print("\n=== REMOVER ATIVO ===")

    id_ativo = ler_inteiro(
        "Digite o ID do ativo a ser removido: "
    )

    ativo_servicos = AtivoServicos()

    ativo = ativo_servicos.consultar_ativo_por_id(
        id_ativo
    )

    if not ativo:
        print("Ativo não encontrado.")
        return

    confirmacao = ler_texto(
        f"Tem certeza que deseja remover "
        f"o ativo '{ativo.nome}'? (s/n): "
    )

    if confirmacao.lower() == "s":
        resultado = ativo_servicos.remover_ativo(
            id_ativo
        )

        if resultado:
            print(
                "Ativo e suas vulnerabilidades "
                "foram removidos com sucesso."
            )
        else:
            print("Não foi possível remover o ativo.")

    else:
        print("Remoção cancelada.")


def fluxo_cadastrar_vulnerabilidade():
    print("\n=== CADASTRAR VULNERABILIDADE ===")

    ativo_servicos = AtivoServicos()
    vulnerabilidade_servicos = VulnerabilidadeServicos()

    id_ativo = ler_inteiro(
        "Digite o ID do ativo associado "
        "à vulnerabilidade: "
    )

    ativo = ativo_servicos.consultar_ativo_por_id(
        id_ativo
    )

    if not ativo:
        print("Ativo não encontrado.")
        return

    tipo = ler_texto(
        "Digite o tipo da vulnerabilidade: "
    )

    descricao = ler_texto(
        "Digite a descrição da vulnerabilidade: "
    )

    severidade = escolher_opcao_enum(
        Severidade,
        "Escolha a severidade da vulnerabilidade:"
    )

    status_tratamento = escolher_opcao_enum(
        StatusTratamento,
        "Escolha o status de tratamento "
        "da vulnerabilidade:"
    )

    try:
        nova_vulnerabilidade = (
            vulnerabilidade_servicos
            .cadastrar_vulnerabilidade(
                ativo_id=id_ativo,
                tipo=tipo,
                descricao=descricao,
                severidade=severidade,
                status_tratamento=status_tratamento
            )
        )

        print(
            f"Vulnerabilidade cadastrada com sucesso! "
            f"ID: {nova_vulnerabilidade.id}"
        )

    except ValueError as erro:
        print(f"Erro: {erro}")


def fluxo_listar_vulnerabilidades():
    print("\n=== LISTAR VULNERABILIDADES ===")

    vulnerabilidade_servicos = (
        VulnerabilidadeServicos()
    )

    vulnerabilidade_servicos.listar_vulnerabilidades()


def fluxo_consultar_vulnerabilidades_por_ativo():
    print(
        "\n=== CONSULTAR VULNERABILIDADES "
        "POR ATIVO ==="
    )

    id_ativo = ler_inteiro(
        "Digite o ID do ativo: "
    )

    vulnerabilidade_servicos = (
        VulnerabilidadeServicos()
    )

    vulnerabilidades = (
        vulnerabilidade_servicos
        .consultar_vulnerabilidades_por_ativo_id(
            id_ativo
        )
    )

    if not vulnerabilidades:
        print(
            "Nenhuma vulnerabilidade encontrada "
            "para este ativo."
        )
        return

    for vulnerabilidade in vulnerabilidades:
        vulnerabilidade_servicos.exibir_vulnerabilidade(
            vulnerabilidade
        )

        print("-" * 20)


def fluxo_atualizar_vulnerabilidade():
    print("\n=== ATUALIZAR VULNERABILIDADE ===")

    id_vulnerabilidade = ler_inteiro(
        "Digite o ID da vulnerabilidade "
        "a ser atualizada: "
    )

    vulnerabilidade_servicos = (
        VulnerabilidadeServicos()
    )

    vulnerabilidade = (
        vulnerabilidade_servicos
        .consultar_vulnerabilidade_por_id(
            id_vulnerabilidade
        )
    )

    if not vulnerabilidade:
        print("Vulnerabilidade não encontrada.")
        return

    vulnerabilidade_servicos.exibir_vulnerabilidade(
        vulnerabilidade
    )

    print("\nQual campo deseja atualizar?")
    print("1. Tipo")
    print("2. Descrição")
    print("3. Severidade")
    print("4. Status de tratamento")

    opcao = ler_inteiro(
        "Escolha uma opção: "
    )

    if opcao == 1:
        novo_tipo = ler_texto(
            "Digite o novo tipo: "
        )

        resultado = (
            vulnerabilidade_servicos
            .atualizar_vulnerabilidade(
                id_vulnerabilidade=id_vulnerabilidade,
                tipo=novo_tipo
            )
        )

    elif opcao == 2:
        nova_descricao = ler_texto(
            "Digite a nova descrição: "
        )

        resultado = (
            vulnerabilidade_servicos
            .atualizar_vulnerabilidade(
                id_vulnerabilidade=id_vulnerabilidade,
                descricao=nova_descricao
            )
        )

    elif opcao == 3:
        nova_severidade = escolher_opcao_enum(
            Severidade,
            "Escolha a nova severidade:"
        )

        resultado = (
            vulnerabilidade_servicos
            .atualizar_vulnerabilidade(
                id_vulnerabilidade=id_vulnerabilidade,
                severidade=nova_severidade
            )
        )

    elif opcao == 4:
        novo_status = escolher_opcao_enum(
            StatusTratamento,
            "Escolha o novo status de tratamento:"
        )

        resultado = (
            vulnerabilidade_servicos
            .atualizar_vulnerabilidade(
                id_vulnerabilidade=id_vulnerabilidade,
                status_tratamento=novo_status
            )
        )

    else:
        print("Opção inválida.")
        return

    if resultado:
        print(
            "Vulnerabilidade atualizada com sucesso."
        )
    else:
        print(
            "Não foi possível atualizar "
            "a vulnerabilidade."
        )


def main():
    while True:
        exibir_menu()

        escolha = ler_inteiro(
            "Escolha uma opção: "
        )

        if escolha == 1:
            fluxo_cadastrar_ativo()

        elif escolha == 2:
            fluxo_listar_ativos()

        elif escolha == 3:
            fluxo_consultar_ativo_por_id()

        elif escolha == 4:
            fluxo_consultar_ativo_por_nome()

        elif escolha == 5:
            fluxo_atualizar_ativo()

        elif escolha == 6:
            fluxo_remover_ativo()

        elif escolha == 7:
            fluxo_cadastrar_vulnerabilidade()

        elif escolha == 8:
            fluxo_listar_vulnerabilidades()

        elif escolha == 9:
            fluxo_consultar_vulnerabilidades_por_ativo()

        elif escolha == 10:
            fluxo_atualizar_vulnerabilidade()

        elif escolha == 0:
            print("Saindo do sistema. Até logo!")
            break

        else:
            print(
                "Opção inválida. "
                "Por favor, tente novamente."
            )


if __name__ == "__main__":
    main()