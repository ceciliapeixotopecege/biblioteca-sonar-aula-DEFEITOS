import unittest
from biblioteca.catalogo import Catalogo
from biblioteca.emprestimos import ServicoEmprestimos
from biblioteca.modelos import Livro


class TestEmprestimos(unittest.TestCase):
    def setUp(self):
        self.catalogo = Catalogo()
        self.livro = Livro("123", "Python", "Maria", 2023)
        self.catalogo.adicionar(self.livro)
        self.servico = ServicoEmprestimos(self.catalogo)

    def test_empresta_livro(self):
        emprestimo = self.servico.emprestar("123", "Carlos")
        self.assertEqual(emprestimo.leitor, "Carlos")
        self.assertFalse(self.livro.disponivel)
        self.assertEqual(self.servico.quantidade_emprestimos_ativos(), 1)

    def test_nao_empresta_livro_ja_emprestado(self):
        self.servico.emprestar("123", "Carlos")
        with self.assertRaisesRegex(ValueError, "já está emprestado"):
            self.servico.emprestar("123", "Joana")

    def test_nao_aceita_leitor_vazio(self):
        with self.assertRaisesRegex(ValueError, "obrigatório"):
            self.servico.emprestar("123", " ")

    def test_devolve_livro(self):
        self.servico.emprestar("123", "Carlos")
        devolucao = self.servico.devolver("123")
        self.assertIsNotNone(devolucao.data_devolucao)
        self.assertTrue(self.livro.disponivel)
        self.assertEqual(self.servico.quantidade_emprestimos_ativos(), 0)

    def test_nao_devolve_livro_disponivel(self):
        with self.assertRaisesRegex(ValueError, "não possui empréstimo ativo"):
            self.servico.devolver("123")


if __name__ == "__main__":
    unittest.main()
