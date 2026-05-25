import json

def carregar_json(caminho):
    with open(caminho, "r", encoding="utf-8") as arquivo:
        return json.load(arquivo)


def salvar_json(caminho, dados):
    with open(caminho, "w", encoding="utf-8") as arquivo:
        json.dump(dados, arquivo, indent=4, ensure_ascii=False)


def carregar_ativos():
    # Lógica para carregar ativos do banco de dados
    pass    

def salvar_ativos(ativos):
    # Lógica para salvar ativos no banco de dados
    pass

def carregar_vulnerabilidades():
    # Lógica para carregar vulnerabilidades do banco de dados
    pass

def salvar_vulnerabilidades(vulnerabilidades):
    # Lógica para salvar vulnerabilidades no banco de dados
    pass
