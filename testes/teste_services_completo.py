import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

import database
from models import (
    Severidade,
    Servidor,
    StatusTratamento,
    TipoAtivo
)
from services import AtivoServicos, VulnerabilidadeServicos


class TesteServicesCompleto(unittest.TestCase):
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

        self.ativos = AtivoServicos()
        self.vulnerabilidades = VulnerabilidadeServicos()

    def tearDown(self):
        self.patch_ativos.stop()
        self.patch_vulnerabilidades.stop()
        self.diretorio.cleanup()

    def cadastrar_ativo(self, nome, tipo):
        return self.ativos.cadastrar_ativo(
            nome=nome,
            descricao="Descrição inicial",
            responsavel="Felipe",
            localizacao="Sala 1",
            tipo=tipo
        )

    def cadastrar_vulnerabilidade(self, ativo_id, tipo="Falha inicial"):
        return self.vulnerabilidades.cadastrar_vulnerabilidade(
            ativo_id=ativo_id,
            tipo=tipo,
            descricao="Descrição inicial",
            severidade=Severidade.MEDIA,
            status_tratamento=StatusTratamento.ABERTA
        )

    def test_fluxo_completo_de_ativos_e_atualizacao_de_tipo(self):
        notebook = self.cadastrar_ativo(
            "Notebook Financeiro",
            TipoAtivo.NOTEBOOK
        )
        servidor = self.cadastrar_ativo(
            "Servidor Principal",
            TipoAtivo.SERVIDOR
        )

        self.assertEqual(len(self.ativos.listar_ativos()), 2)
        self.assertEqual(
            self.ativos.consultar_ativo_por_id(notebook.id).nome,
            "Notebook Financeiro"
        )
        self.assertEqual(
            self.ativos.consultar_ativo_por_nome("Servidor Principal").id,
            servidor.id
        )

        self.assertTrue(
            self.ativos.atualizar_ativo(notebook.id, nome="Servidor Financeiro")
        )
        self.assertTrue(
            self.ativos.atualizar_ativo(notebook.id, descricao="Nova descrição")
        )
        self.assertTrue(
            self.ativos.atualizar_ativo(notebook.id, responsavel="Ana")
        )
        self.assertTrue(
            self.ativos.atualizar_ativo(notebook.id, localizacao="Datacenter")
        )
        self.assertTrue(
            self.ativos.atualizar_ativo(notebook.id, tipo=TipoAtivo.SERVIDOR)
        )

        atualizado = self.ativos.consultar_ativo_por_id(notebook.id)
        self.assertIsInstance(atualizado, Servidor)
        self.assertEqual(atualizado.id, notebook.id)
        self.assertEqual(atualizado.nome, "Servidor Financeiro")
        self.assertEqual(atualizado.descricao, "Nova descrição")
        self.assertEqual(atualizado.responsavel, "Ana")
        self.assertEqual(atualizado.localizacao, "Datacenter")

        dados_json = database.carregar_json(self.caminho_ativos)
        self.assertEqual(dados_json[0]["tipo"], "SERVIDOR")
        recarregado = database.carregar_ativos()[0]
        self.assertIsInstance(recarregado, Servidor)
        self.assertEqual(recarregado.id, notebook.id)

    def test_fluxo_completo_de_vulnerabilidade(self):
        ativo = self.cadastrar_ativo("Servidor", TipoAtivo.SERVIDOR)
        vulnerabilidade = self.cadastrar_vulnerabilidade(ativo.id)

        with self.assertRaisesRegex(ValueError, "Ativo não encontrado"):
            self.cadastrar_vulnerabilidade(999)

        self.assertEqual(
            self.vulnerabilidades.consultar_vulnerabilidade_por_id(
                vulnerabilidade.id
            ).id,
            vulnerabilidade.id
        )
        self.assertEqual(len(self.vulnerabilidades.listar_vulnerabilidades()), 1)
        self.assertEqual(
            len(
                self.vulnerabilidades
                .consultar_vulnerabilidades_por_ativo_id(ativo.id)
            ),
            1
        )

        self.assertTrue(
            self.vulnerabilidades.atualizar_vulnerabilidade(
                vulnerabilidade.id,
                tipo="Falha atualizada"
            )
        )
        self.assertTrue(
            self.vulnerabilidades.atualizar_vulnerabilidade(
                vulnerabilidade.id,
                descricao="Descrição atualizada"
            )
        )
        self.assertTrue(
            self.vulnerabilidades.atualizar_vulnerabilidade(
                vulnerabilidade.id,
                severidade=Severidade.CRITICA
            )
        )
        self.assertTrue(
            self.vulnerabilidades.atualizar_vulnerabilidade(
                vulnerabilidade.id,
                status_tratamento=StatusTratamento.RESOLVIDA
            )
        )

        recarregada = database.carregar_vulnerabilidades()[0]
        self.assertEqual(recarregada.tipo, "Falha atualizada")
        self.assertEqual(recarregada.descricao, "Descrição atualizada")
        self.assertEqual(recarregada.severidade, Severidade.CRITICA)
        self.assertEqual(
            recarregada.status_tratamento,
            StatusTratamento.RESOLVIDA
        )

    def test_remocao_em_cascata_preserva_outros_dados(self):
        ativo_a = self.cadastrar_ativo("Ativo A", TipoAtivo.NOTEBOOK)
        ativo_b = self.cadastrar_ativo("Ativo B", TipoAtivo.SERVIDOR)
        vulnerabilidade_1 = self.cadastrar_vulnerabilidade(ativo_a.id, "Falha 1")
        vulnerabilidade_2 = self.cadastrar_vulnerabilidade(ativo_a.id, "Falha 2")
        vulnerabilidade_3 = self.cadastrar_vulnerabilidade(ativo_b.id, "Falha 3")

        self.assertTrue(self.ativos.remover_ativo(ativo_a.id))

        self.assertIsNone(self.ativos.consultar_ativo_por_id(ativo_a.id))
        self.assertIsNotNone(self.ativos.consultar_ativo_por_id(ativo_b.id))
        ids_restantes = [
            item.id
            for item in self.vulnerabilidades.listar_vulnerabilidades()
        ]
        self.assertNotIn(vulnerabilidade_1.id, ids_restantes)
        self.assertNotIn(vulnerabilidade_2.id, ids_restantes)
        self.assertIn(vulnerabilidade_3.id, ids_restantes)


if __name__ == "__main__":
    unittest.main()
