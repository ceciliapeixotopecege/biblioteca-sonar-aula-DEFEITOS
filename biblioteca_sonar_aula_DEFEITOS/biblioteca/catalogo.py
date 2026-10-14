"""Operações de cadastro e consulta do catálogo."""
from biblioteca.modelos import Livro


class Catalogo:
    def __init__(self):
        self._livros = {}

    def adicionar(self, livro: Livro):
        if livro.isbn in self._livros:
            raise ValueError("Já existe um livro com esse ISBN.")
        self._livros[livro.isbn] = livro

    def buscar(self, isbn: str) -> Livro:
        try:
            return self._livros[isbn]
        except KeyError as erro:
            raise ValueError("Livro não encontrado.") from erro

    def listar(self):
        return sorted(self._livros.values(), key=lambda livro: livro.titulo.lower())

    def remover(self, isbn: str):
        livro = self.buscar(isbn)
        if not livro.disponivel:
            raise ValueError("Não é possível remover um livro emprestado.")
        del self._livros[isbn]

    def quantidade(self):
        return len(self._livros)
