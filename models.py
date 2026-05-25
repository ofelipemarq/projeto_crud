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

class StatusVulnerabilidade(Enum):
    ABERTA = 1
    EM_ANALISE = 2
    RESOLVIDA = 3
    ACEITA_COMO_RISCO = 4
    