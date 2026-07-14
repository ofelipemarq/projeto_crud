from database import carregar_ativos, salvar_ativos, salvar_vulnerabilidades, carregar_vulnerabilidades
from utils import ler_texto, ler_inteiro, escolher_opcao_enum
from models import TipoAtivo , Severidade, StatusTratamento, criar_equipamento


def buscar_por_campo(objetos, campo, valor):
    for objeto in objetos:
        if getattr(objeto, campo) == valor:
            return objeto
    return None

def filtrar_por_campo(objetos, campo, valor):
    resultado = []

    for objeto in objetos:
        if getattr(objeto, campo) == valor:
            resultado.append(objeto)

    return resultado


def gerar_proximo_id(lista):
    if not lista:
        return 1

    maior_id = 0

    for item in lista:
        if item.id > maior_id:
            maior_id = item.id

    return maior_id + 1




class AtivoServicos:

    def cadastrar_ativo(self, nome, descricao, responsavel, localizacao, tipo):
        ativos = carregar_ativos()
        novo_id = gerar_proximo_id(ativos)

        novo_ativo = criar_equipamento(
            tipo=tipo,
            id=novo_id,
            nome=nome,
            descricao=descricao,
            responsavel=responsavel,
            localizacao=localizacao
        )
        ativos.append(novo_ativo)
        salvar_ativos(ativos)

        return novo_ativo
    
    def exibir_ativo(self, ativo):
        print(f"ID: {ativo.id}")
        print(f"Nome: {ativo.nome}")
        print(f"Descrição: {ativo.descricao}")
        print(f"Responsável: {ativo.responsavel}")
        print(f"Localização: {ativo.localizacao}")
        print(f"Tipo: {ativo.tipo.name}")

    def listar_ativos(self):
        ativos = carregar_ativos()
        if ativos:
            print("Lista de Ativos:")
            for ativo in ativos:
                self.exibir_ativo(ativo)
                print("-" * 20)
        else:
            print("Nenhum ativo cadastrado.")
        
    def consultar_ativo_por_nome(self, nome_ativo):
        ativos = carregar_ativos()
        return buscar_por_campo(ativos, "nome", nome_ativo)

    def consultar_ativo_por_id(self, id_ativo):
        ativos = carregar_ativos()
        return buscar_por_campo(ativos, "id", id_ativo)
    
    def atualizar_ativo(
        self, 
        id_ativo, 
        nome=None, 
        descricao=None, 
        responsavel=None, 
        localizacao=None
        ):

        ativos = carregar_ativos()
        ativo_encontrado = None
        
        for ativo in ativos:
            if ativo.id == id_ativo:
                ativo_encontrado = ativo
                break

        if ativo_encontrado is None:
            return False

        ativo_encontrado.atualizar(
            nome=nome,
            descricao=descricao,
            responsavel=responsavel,
            localizacao=localizacao
        )

        salvar_ativos(ativos)
        return True
    

    def remover_ativo(self, id_ativo):
        ativos = carregar_ativos()
        
        for indice, ativo in enumerate(ativos):
            if ativo.id == id_ativo:
                del ativos[indice]
                salvar_ativos(ativos)

                return True
            
        return False
    
class VulnerabilidadeServicos:
    pass


