from database import carregar_ativos, salvar_ativos, salvar_vulnerabilidades, carregar_vulnerabilidades
from utils import ler_texto, ler_inteiro, escolher_opcao_enum
from models import TipoAtivo , Severidade, StatusTratamento, Vulnerabilidade, criar_equipamento


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

                vulnerabilidades = carregar_vulnerabilidades()
                vulnerabilidades_restantes = []

                for vulnerabilidade in vulnerabilidades:
                    if vulnerabilidade.ativo_id != id_ativo:
                        vulnerabilidades_restantes.append(
                            vulnerabilidade
                        )

                salvar_vulnerabilidades(
                    vulnerabilidades_restantes
                )

                return True

        return False
    
class VulnerabilidadeServicos:
    
    def cadastrar_vulnerabilidade(
        self, 
        ativo_id, 
        tipo, 
        descricao, 
        severidade, 
        status_tratamento
    ):
        
        ativos = carregar_ativos()
        ativo_encontrado = buscar_por_campo(ativos, "id", ativo_id)
        if ativo_encontrado is None:
            raise ValueError("Ativo não encontrado para o ID fornecido.")
        
        vulnerabilidades = carregar_vulnerabilidades()
        novo_id = gerar_proximo_id(vulnerabilidades)

        nova_vulnerabilidade = Vulnerabilidade(
            id=novo_id,
            ativo_id=ativo_id,
            tipo=tipo,
            descricao=descricao,
            severidade=severidade,
            status_tratamento=status_tratamento
        )
        vulnerabilidades.append(nova_vulnerabilidade)
        salvar_vulnerabilidades(vulnerabilidades)

        return nova_vulnerabilidade
    
    def exibir_vulnerabilidade(self, vulnerabilidade):
        print(f"ID: {vulnerabilidade.id}")
        print(f"Ativo ID: {vulnerabilidade.ativo_id}")
        print(f"Tipo: {vulnerabilidade.tipo}")
        print(f"Descrição: {vulnerabilidade.descricao}")
        print(f"Severidade: {vulnerabilidade.severidade.name}")
        print(f"Status de Tratamento: {vulnerabilidade.status_tratamento.name}")

    def listar_vulnerabilidades(self):
        vulnerabilidades = carregar_vulnerabilidades()
        if vulnerabilidades:
            print("Lista de Vulnerabilidades:")
            for vulnerabilidade in vulnerabilidades:
                self.exibir_vulnerabilidade(vulnerabilidade)
                print("-" * 20)
        else:
            print("Nenhuma vulnerabilidade cadastrada.")

    def consultar_vulnerabilidade_por_id(self, id_vulnerabilidade):
        vulnerabilidades = carregar_vulnerabilidades()
        return buscar_por_campo(vulnerabilidades, "id", id_vulnerabilidade)
    
    def consultar_vulnerabilidades_por_ativo_id(self, ativo_id):
        vulnerabilidades = carregar_vulnerabilidades()
        return filtrar_por_campo(vulnerabilidades, "ativo_id", ativo_id)
    
    def atualizar_vulnerabilidade(
        self, 
        id_vulnerabilidade, 
        tipo=None, 
        descricao=None, 
        severidade=None, 
        status_tratamento=None
    ):
        vulnerabilidades = carregar_vulnerabilidades()
        vulnerabilidade_encontrada = None
        
        for vulnerabilidade in vulnerabilidades:
            if vulnerabilidade.id == id_vulnerabilidade:
                vulnerabilidade_encontrada = vulnerabilidade
                break

        if vulnerabilidade_encontrada is None:
            return False

        if tipo is not None:
            vulnerabilidade_encontrada.tipo = tipo
        if descricao is not None:
            vulnerabilidade_encontrada.descricao = descricao
        if severidade is not None:
            vulnerabilidade_encontrada.severidade = severidade
        if status_tratamento is not None:
            vulnerabilidade_encontrada.alterar_status(status_tratamento)

        salvar_vulnerabilidades(vulnerabilidades)
        return True 
    
    def remover_vulnerabilidade_por_ativo_id(self, ativo_id):
        vulnerabilidades = carregar_vulnerabilidades()

        vulnerabilidades_restantes = []

        for vulnerabilidade in vulnerabilidades:
            if vulnerabilidade.ativo_id != ativo_id:
                vulnerabilidades_restantes.append(
                    vulnerabilidade
                )

        quantidade_removida = (
            len(vulnerabilidades)
            - len(vulnerabilidades_restantes)
        )

        salvar_vulnerabilidades(
            vulnerabilidades_restantes
        )

        return quantidade_removida
