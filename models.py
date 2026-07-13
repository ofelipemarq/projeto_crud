from enum import Enum

class TipoAtivo(Enum):
    NOTEBOOK = 1
    SERVIDOR = 2
    ROTEADOR = 3
    IMPRESSORA = 4  


class Severidade(Enum):
    BAIXA = 1
    MEDIA = 2
    ALTA = 3
    CRITICA = 4

class StatusTratamento(Enum):
    ABERTA = 1
    EM_ANALISE = 2
    RESOLVIDA = 3
    ACEITA_COMO_RISCO = 4
    

class Equipamento:
    tipo = None

    def __init__(self, id, nome, descricao, responsavel, localizacao):
        self.id = id
        self.nome = nome
        self.descricao = descricao
        self.responsavel = responsavel
        self.localizacao = localizacao

    def atualizar(self, nome=None, descricao=None, responsavel=None, localizacao=None):
        if nome is not None:
            self.nome = nome
        if descricao is not None:
            self.descricao = descricao
        if responsavel is not None:
            self.responsavel = responsavel
        if localizacao is not None:
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
    
class Notebook(Equipamento):
    tipo = TipoAtivo.NOTEBOOK

class Servidor(Equipamento):
    tipo = TipoAtivo.SERVIDOR

class Roteador(Equipamento):
    tipo = TipoAtivo.ROTEADOR

class Impressora(Equipamento):
    tipo = TipoAtivo.IMPRESSORA

def criar_equipamento(tipo, id, nome, descricao, responsavel, localizacao):
    if tipo == TipoAtivo.NOTEBOOK:
        return Notebook(id, nome, descricao, responsavel, localizacao)
    elif tipo == TipoAtivo.SERVIDOR:
        return Servidor(id, nome, descricao, responsavel, localizacao)
    elif tipo == TipoAtivo.ROTEADOR:
        return Roteador(id, nome, descricao, responsavel, localizacao)
    elif tipo == TipoAtivo.IMPRESSORA:
        return Impressora(id, nome, descricao, responsavel, localizacao)
    else:
        raise ValueError("Tipo de equipamento inválido")
    

def equipamento_from_dict(data):
    tipo = TipoAtivo[data["tipo"]]
    return criar_equipamento(
        tipo=tipo,
        id=data["id"],
        nome=data["nome"],
        descricao=data["descricao"],
        responsavel=data["responsavel"],
        localizacao=data["localizacao"]
    )


class Vulnerabilidade:
    def __init__(
        self,
        id,
        ativo_id,
        tipo,
        descricao,
        severidade,
        status_tratamento
    ):
        self.id = id
        self.ativo_id = ativo_id
        self.tipo = tipo
        self.descricao = descricao
        self.severidade = severidade
        self.status_tratamento = status_tratamento

    def alterar_status(self, novo_status):
        self.status_tratamento = novo_status

    def to_dict(self):
        return {
            "id": self.id,
            "ativo_id": self.ativo_id,
            "tipo": self.tipo,
            "descricao": self.descricao,
            "severidade": self.severidade.name,
            "status_tratamento": self.status_tratamento.name
        }
    
def vulnerabilidade_from_dict(data):
    severidade = Severidade[data["severidade"]]
    status_tratamento = StatusTratamento[data["status_tratamento"]]
    return Vulnerabilidade(
        id=data["id"],
        ativo_id=data["ativo_id"],
        tipo=data["tipo"],
        descricao=data["descricao"],
        severidade=severidade,
        status_tratamento=status_tratamento
    )