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


class Ativo:
    def __init__(self, id, nome, tipo, descricao, responsavel, localizacao):
        self.id = id
        self.nome = nome
        self.tipo = tipo
        self.descricao = descricao
        self.responsavel = responsavel
        self.localizacao = localizacao

    def to_dict(self):
        return {
            "id": self.id,
            "nome": self.nome,
            "tipo": self.tipo.name,
            "descricao": self.descricao,
            "responsavel": self.responsavel,
            "localizacao": self.localizacao
        }

class AtivoServicos:

    def cadastrar_ativo(self):
        ativos = carregar_ativos()

        nome_ativo = ler_texto("Digite o nome do ativo: ")

        tipo_ativo = escolher_opcao_enum(
            TipoAtivo,
            "Escolha o tipo do ativo: "
        )

        descricao_ativo = ler_texto("Digite a descrição do ativo: ")
        responsavel_ativo = ler_texto("Digite o responsável pelo ativo: ")
        localizacao_ativo = ler_texto("Digite a localização do ativo: ")

        novo_ativo = Ativo(
            id=gerar_proximo_id(ativos),
            nome=nome_ativo,
            tipo=tipo_ativo,
            descricao=descricao_ativo,
            responsavel=responsavel_ativo,
            localizacao=localizacao_ativo
        )
        ativos.append(novo_ativo.to_dict())
        salvar_ativos(ativos)

        print("Ativo cadastrado com sucesso!")

    def listar_ativos(self):
        ativos = carregar_ativos()

        if not ativos:
            print("Nenhum ativo cadastrado.")
            return

        print("\nLista de Ativos:")
        print("-" * 50)

        for ativo in ativos:
            self.exibir_ativo(ativo)

    def exibir_ativo(self, ativo):
        print(f"ID: {ativo['id']}")
        print(f"Nome: {ativo['nome']}")
        print(f"Tipo: {ativo['tipo']}")
        print(f"Descrição: {ativo['descricao']}")
        print(f"Responsável: {ativo['responsavel']}")
        print(f"Localização: {ativo['localizacao']}")
        print("-" * 50)

    def consultar_ativo_por_id(self, ativos, id_ativo):
        return buscar_por_campo(ativos, "id", id_ativo)

    def atualizar_ativo(self, id_ativo):
        ativos = carregar_ativos()
        ativo = self.consultar_ativo_por_id(ativos, id_ativo)

        if not ativo:
            print("Ativo não encontrado.")
            return

        print("Atualizando informações do ativo:")
        print("-" * 50)

        nome_ativo = ler_texto(f"Digite o novo nome do ativo (atual: {ativo['nome']}): ")
        tipo_ativo = escolher_opcao_enum(
            TipoAtivo,
            f"Escolha o novo tipo do ativo (atual: {ativo['tipo']}): "
        )
        descricao_ativo = ler_texto(f"Digite a nova descrição do ativo (atual: {ativo['descricao']}): ")
        responsavel_ativo = ler_texto(f"Digite o novo responsável pelo ativo (atual: {ativo['responsavel']}): ")
        localizacao_ativo = ler_texto(f"Digite a nova localização do ativo (atual: {ativo['localizacao']}): ")

        ativo['nome'] = nome_ativo
        ativo['tipo'] = tipo_ativo.name
        ativo['descricao'] = descricao_ativo
        ativo['responsavel'] = responsavel_ativo
        ativo['localizacao'] = localizacao_ativo

        salvar_ativos(ativos)
        print("Ativo atualizado com sucesso!")

    def remover_ativo(self, id_ativo):
        ativos = carregar_ativos()
        ativo = self.consultar_ativo_por_id(ativos, id_ativo)

        if not ativo:
            print("Ativo não encontrado.")
            return

        ativos.remove(ativo)
        salvar_ativos(ativos)
        print("Ativo removido com sucesso!")

class VulnerabilidadeServicos:
    pass


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

