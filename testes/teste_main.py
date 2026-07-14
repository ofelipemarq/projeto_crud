import unittest
from unittest.mock import MagicMock, patch

import main
from models import TipoAtivo, criar_equipamento
from utils import ler_inteiro


class TesteMain(unittest.TestCase):
    def test_todas_as_opcoes_do_menu_estao_conectadas(self):
        nomes_fluxos = [
            "fluxo_cadastrar_ativo",
            "fluxo_listar_ativos",
            "fluxo_consultar_ativo_por_id",
            "fluxo_consultar_ativo_por_nome",
            "fluxo_atualizar_ativo",
            "fluxo_remover_ativo",
            "fluxo_cadastrar_vulnerabilidade",
            "fluxo_listar_vulnerabilidades",
            "fluxo_consultar_vulnerabilidades_por_ativo",
            "fluxo_atualizar_vulnerabilidade"
        ]
        mocks = {}
        patchers = []

        for nome in nomes_fluxos:
            patcher = patch.object(main, nome)
            patchers.append(patcher)
            mocks[nome] = patcher.start()

        try:
            with patch.object(
                main,
                "ler_inteiro",
                side_effect=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 99, 0]
            ), patch("builtins.print"):
                main.main()
        finally:
            for patcher in patchers:
                patcher.stop()

        for fluxo in mocks.values():
            fluxo.assert_called_once_with()

    def test_fluxo_atualiza_tipo_sem_pedir_outros_campos(self):
        ativo = criar_equipamento(
            tipo=TipoAtivo.NOTEBOOK,
            id=1,
            nome="Notebook",
            descricao="Descrição",
            responsavel="Felipe",
            localizacao="Sala 1"
        )
        servico = MagicMock()
        servico.consultar_ativo_por_id.return_value = ativo
        servico.atualizar_ativo.return_value = True

        with patch.object(main, "AtivoServicos", return_value=servico), patch.object(
            main,
            "ler_inteiro",
            side_effect=[1, 5]
        ), patch.object(
            main,
            "escolher_opcao_enum",
            return_value=TipoAtivo.SERVIDOR
        ), patch.object(main, "exibir_ativo"), patch("builtins.print"):
            main.fluxo_atualizar_ativo()

        servico.atualizar_ativo.assert_called_once_with(
            id_ativo=1,
            tipo=TipoAtivo.SERVIDOR
        )

    def test_cancelamento_nao_remove_ativo(self):
        ativo = criar_equipamento(
            tipo=TipoAtivo.NOTEBOOK,
            id=1,
            nome="Notebook",
            descricao="Descrição",
            responsavel="Felipe",
            localizacao="Sala 1"
        )
        servico = MagicMock()
        servico.consultar_ativo_por_id.return_value = ativo

        with patch.object(main, "AtivoServicos", return_value=servico), patch.object(
            main,
            "ler_inteiro",
            return_value=1
        ), patch.object(main, "ler_texto", return_value="n"), patch(
            "builtins.print"
        ):
            main.fluxo_remover_ativo()

        servico.remover_ativo.assert_not_called()

    def test_ler_inteiro_trata_entrada_invalida(self):
        with patch("builtins.input", side_effect=["abc", "0"]), patch(
            "builtins.print"
        ) as imprimir:
            resultado = ler_inteiro("Escolha: ")

        self.assertEqual(resultado, 0)
        imprimir.assert_called_once()


if __name__ == "__main__":
    unittest.main()
