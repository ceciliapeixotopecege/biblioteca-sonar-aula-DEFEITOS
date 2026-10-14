import unittest
from biblioteca.catalogo import Catalogo
from biblioteca.modelos import Livro


class TestCatalogo(unittest.TestCase):
    def setUp(self):
        self.catalogo = Catalogo()
        self.livro = Livro("123", "Python", "Maria", 2023)

    def test_adiciona_e_busca_livro(self):
        self.catalogo.adicionar(self.livro)
        self.assertEqual(self.catalogo.buscar("123").titulo, "Python")

    def test_nao_permite_isbn_duplicado(self):
        self.catalogo.adicionar(self.livro)
        with self.assertRaises(ValueError):
            self.catalogo.adicionar(Livro("123", "Outro", "João", 2020))

    def test_busca_livro_inexistente(self):
        with self.assertRaisesRegex(ValueError, "não encontrado"):
            self.catalogo.buscar("999")

    def test_lista_em_ordem_alfabetica(self):
        self.catalogo.adicionar(Livro("2", "Zebra", "Autor", 2020))
        self.catalogo.adicionar(Livro("1", "Abelha", "Autor", 2020))
        self.assertEqual([item.titulo for item in self.catalogo.listar()], ["Abelha", "Zebra"])


if __name__ == "__main__":
    unittest.main()
