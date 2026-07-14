import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

import database
from models import Notebook, TipoAtivo, criar_equipamento


class TesteDatabase(unittest.TestCase):
    def setUp(self):
        self.diretorio = tempfile.TemporaryDirectory()
        raiz = Path(self.diretorio.name)
        self.caminho_ativos = raiz / "ativos.json"
        self.caminho_vulnerabilidades = raiz / "vulnerabilidades.json"

        self.patch_ativos = patch.object(
            database,
            "CAMINHO_ATIVOS",
            self.caminho_ativos
        )
        self.patch_vulnerabilidades = patch.object(
            database,
            "CAMINHO_VULNERABILIDADES",
            self.caminho_vulnerabilidades
        )
        self.patch_ativos.start()
        self.patch_vulnerabilidades.start()
        database.salvar_json(self.caminho_ativos, [])
        database.salvar_json(self.caminho_vulnerabilidades, [])

    def tearDown(self):
        self.patch_ativos.stop()
        self.patch_vulnerabilidades.stop()
        self.diretorio.cleanup()

    def test_salvar_e_carregar_ativo_como_objeto(self):
        ativo = criar_equipamento(
            tipo=TipoAtivo.NOTEBOOK,
            id=1,
            nome="Notebook Teste",
            descricao="Teste de persistência",
            responsavel="Felipe",
            localizacao="Sala 1"
        )

        database.salvar_ativos([ativo])
        ativos = database.carregar_ativos()

        self.assertEqual(len(ativos), 1)
        self.assertIsInstance(ativos[0], Notebook)
        self.assertEqual(ativos[0].nome, "Notebook Teste")

    def test_json_de_ativos_permanece_lista_de_objetos(self):
        ativo = criar_equipamento(
            tipo=TipoAtivo.NOTEBOOK,
            id=1,
            nome="Notebook Teste",
            descricao="Descrição",
            responsavel="Felipe",
            localizacao="Sala 1"
        )

        database.salvar_ativos([ativo])
        dados = database.carregar_json(self.caminho_ativos)

        self.assertIsInstance(dados, list)
        self.assertIsInstance(dados[0], dict)
        self.assertEqual(dados[0]["tipo"], "NOTEBOOK")


if __name__ == "__main__":
    unittest.main()
