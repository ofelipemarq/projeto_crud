from 

from models import Severidade, StatusTratamento, TipoAtivo, criar_equipamento, equipamento_from_dict
import modelsmodels import (
    TipoAtivo,
    Severidade,
    StatusTratamento,
    criar_equipamento,
    equipamento_from_dict,
    Vulnerabilidade,
    vulnerabilidade_from_dict
)


equipamento = criar_equipamento(
    tipo=TipoAtivo.NOTEBOOK,
    id=1,
    nome="Notebook TI",
    descricao="Notebook da equipe técnica",
    responsavel="Felipe",
    localizacao="Sala de TI"
)

print(type(equipamento))
print(equipamento.to_dict())

dados_equipamento = equipamento.to_dict()
equipamento_reconstruido = equipamento_from_dict(dados_equipamento)

print(type(equipamento_reconstruido))
print(equipamento_reconstruido.nome)


vulnerabilidade = Vulnerabilidade(
    id=1,
    ativo_id=1,
    tipo="Software desatualizado",
    descricao="Sistema operacional sem atualização.",
    severidade=Severidade.ALTA,
    status_tratamento=StatusTratamento.ABERTA
)

print(vulnerabilidade.to_dict())

dados_vulnerabilidade = vulnerabilidade.to_dict()
vulnerabilidade_reconstruida = vulnerabilidade_from_dict(
    dados_vulnerabilidade
)

print(type(vulnerabilidade_reconstruida))
print(vulnerabilidade_reconstruida.severidade)