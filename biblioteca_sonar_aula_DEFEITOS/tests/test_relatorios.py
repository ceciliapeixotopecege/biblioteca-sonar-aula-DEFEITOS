import unittest
from biblioteca.catalogo import Catalogo
from biblioteca.emprestimos import ServicoEmprestimos
from biblioteca.modelos import Livro
from biblioteca.relatorios import gerar_resumo


class TestRelatorios(unittest.TestCase):
    def test_resumo_reflete_estado_atual(self):
        catalogo = Catalogo()
        catalogo.adicionar(Livro("1", "Livro A", "Autor A", 2020))
        catalogo.adicionar(Livro("2", "Livro B", "Autor B", 2021))
        servico = ServicoEmprestimos(catalogo)
        servico.emprestar("1", "Leitor")
        resumo = gerar_resumo(catalogo, servico)
        self.assertIn("Total de livros: 2", resumo)
        self.assertIn("Disponíveis: 1", resumo)
        self.assertIn("Emprestados: 1", resumo)
        self.assertIn("Empréstimos ativos: 1", resumo)


if __name__ == "__main__":
    unittest.main()
