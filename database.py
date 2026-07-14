from models import (
    equipamento_from_dict,
    vulnerabilidade_from_dict
)
import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
BASE_DIR = BASE_DIR / "data"

CAMINHO_ATIVOS = BASE_DIR / "ativos.json"
CAMINHO_VULNERABILIDADES = BASE_DIR / "vulnerabilidades.json"


def carregar_json(caminho):
    with open(caminho, "r", encoding="utf-8") as arquivo:
        return json.load(arquivo)


def salvar_json(caminho, dados):
    with open(caminho, "w", encoding="utf-8") as arquivo:
        json.dump(dados, arquivo, indent=4, ensure_ascii=False)


def carregar_ativos():
    dados = carregar_json(CAMINHO_ATIVOS)
    ativos = []
    for item in dados:
        ativo = equipamento_from_dict(item)
        ativos.append(ativo)
    return ativos

def salvar_ativos(ativos):
    dados = []
    for ativo in ativos:
        dados.append(ativo.to_dict())
    salvar_json(CAMINHO_ATIVOS, dados)

def carregar_vulnerabilidades():
    dados = carregar_json(CAMINHO_VULNERABILIDADES)
    vulnerabilidades = []
    for item in dados:
        vulnerabilidade = vulnerabilidade_from_dict(item)
        vulnerabilidades.append(vulnerabilidade)
    return vulnerabilidades

def salvar_vulnerabilidades(vulnerabilidades):
    dados = []
    for vulnerabilidade in vulnerabilidades:
        dados.append(vulnerabilidade.to_dict())
    salvar_json(CAMINHO_VULNERABILIDADES, dados)
