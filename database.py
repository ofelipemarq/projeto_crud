import json

def carregar_json(caminho):
    with open(caminho, "r", encoding="utf-8") as arquivo:
        return json.load(arquivo)


def salvar_json(caminho, dados):
    with open(caminho, "w", encoding="utf-8") as arquivo:
        json.dump(dados, arquivo, indent=4, ensure_ascii=False)


def carregar_ativos():
    return carregar_json("ativos.json")

def salvar_ativos(ativos):
    salvar_json("ativos.json", ativos)

def carregar_vulnerabilidades():
    return carregar_json("vulnerabilidades.json")

def salvar_vulnerabilidades(vulnerabilidades):
    salvar_json("vulnerabilidades.json", vulnerabilidades)
