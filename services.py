from database import carregar_ativos, salvar_ativos, salvar_vulnerabilidades, carregar_vulnerabilidades
from models import Vulnerabilidade, criar_equipamento


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
    
    def listar_ativos(self):
        return carregar_ativos()
        
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
        localizacao=None,
        tipo=None
        ):

        ativos = carregar_ativos()

        for indice, ativo in enumerate(ativos):
            if ativo.id == id_ativo:
                if tipo is None:
                    ativo.atualizar(
                        nome=nome,
                        descricao=descricao,
                        responsavel=responsavel,
                        localizacao=localizacao
                    )
                else:
                    ativo_atualizado = criar_equipamento(
                        tipo=tipo,
                        id=ativo.id,
                        nome=nome if nome is not None else ativo.nome,
                        descricao=(
                            descricao
                            if descricao is not None
                            else ativo.descricao
                        ),
                        responsavel=(
                            responsavel
                            if responsavel is not None
                            else ativo.responsavel
                        ),
                        localizacao=(
                            localizacao
                            if localizacao is not None
                            else ativo.localizacao
                        )
                    )
                    ativos[indice] = ativo_atualizado

                salvar_ativos(ativos)
                return True

        return False
    

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
    
    def listar_vulnerabilidades(self):
        return carregar_vulnerabilidades()

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
