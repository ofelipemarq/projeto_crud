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
    return carregar_json(CAMINHO_ATIVOS)

def salvar_ativos(ativos):
    salvar_json(CAMINHO_ATIVOS, ativos)

def carregar_vulnerabilidades():
    return carregar_json(CAMINHO_VULNERABILIDADES)

def salvar_vulnerabilidades(vulnerabilidades):
    salvar_json(CAMINHO_VULNERABILIDADES, vulnerabilidades)

