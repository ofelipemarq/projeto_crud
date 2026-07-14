import unittest

from models import (
    Equipamento,
    Impressora,
    Notebook,
    Roteador,
    Severidade,
    Servidor,
    StatusTratamento,
    TipoAtivo,
    Vulnerabilidade,
    criar_equipamento,
    equipamento_from_dict,
    vulnerabilidade_from_dict
)


class TesteModels(unittest.TestCase):
    def test_criar_as_quatro_subclasses(self):
        casos = [
            (TipoAtivo.NOTEBOOK, Notebook),
            (TipoAtivo.SERVIDOR, Servidor),
            (TipoAtivo.ROTEADOR, Roteador),
            (TipoAtivo.IMPRESSORA, Impressora)
        ]

        for tipo, classe_esperada in casos:
            with self.subTest(tipo=tipo):
                equipamento = criar_equipamento(
                    tipo=tipo,
                    id=1,
                    nome="Equipamento",
                    descricao="Descrição",
                    responsavel="Responsável",
                    localizacao="Sala 1"
                )
                self.assertIsInstance(equipamento, Equipamento)
                self.assertIsInstance(equipamento, classe_esperada)
                self.assertEqual(equipamento.tipo, tipo)

    def test_serializar_e_reconstruir_equipamento(self):
        equipamento = criar_equipamento(
            tipo=TipoAtivo.SERVIDOR,
            id=8,
            nome="Servidor Principal",
            descricao="Servidor de aplicações",
            responsavel="Felipe",
            localizacao="Datacenter"
        )

        dados = equipamento.to_dict()
        reconstruido = equipamento_from_dict(dados)

        self.assertEqual(dados["tipo"], "SERVIDOR")
        self.assertIsInstance(reconstruido, Servidor)
        self.assertEqual(reconstruido.id, 8)
        self.assertEqual(reconstruido.nome, "Servidor Principal")

    def test_serializar_e_reconstruir_vulnerabilidade(self):
        vulnerabilidade = Vulnerabilidade(
            id=3,
            ativo_id=8,
            tipo="Software desatualizado",
            descricao="Atualização pendente",
            severidade=Severidade.ALTA,
            status_tratamento=StatusTratamento.ABERTA
        )

        dados = vulnerabilidade.to_dict()
        reconstruida = vulnerabilidade_from_dict(dados)

        self.assertEqual(dados["severidade"], "ALTA")
        self.assertEqual(dados["status_tratamento"], "ABERTA")
        self.assertEqual(reconstruida.ativo_id, 8)
        self.assertEqual(reconstruida.severidade, Severidade.ALTA)
        self.assertEqual(
            reconstruida.status_tratamento,
            StatusTratamento.ABERTA
        )


if __name__ == "__main__":
    unittest.main()
