"""Regras para registrar e encerrar empréstimos."""
from dataclasses import dataclass
from datetime import date
from biblioteca.catalogo import Catalogo


@dataclass
class Emprestimo:
    isbn: str
    leitor: str
    data_emprestimo: date
    data_devolucao: date | None = None

    @property
    def ativo(self):
        return self.data_devolucao is None


class ServicoEmprestimos:
    def __init__(self, catalogo: Catalogo):
        self.catalogo = catalogo
        self._historico = []

    def emprestar(self, isbn: str, leitor: str):
        nome = leitor.strip()
        if not nome:
            raise ValueError("O nome do leitor é obrigatório.")
        livro = self.catalogo.buscar(isbn)
        if not livro.disponivel:
            raise ValueError("O livro já está emprestado.")
        livro.disponivel = False
        emprestimo = Emprestimo(isbn, nome, date.today())
        self._historico.append(emprestimo)
        return emprestimo

    def devolver(self, isbn: str):
        livro = self.catalogo.buscar(isbn)
        if livro.disponivel:
            raise ValueError("O livro não possui empréstimo ativo.")
        for emprestimo in reversed(self._historico):
            if emprestimo.isbn == isbn and emprestimo.ativo:
                emprestimo.data_devolucao = date.today()
                livro.disponivel = True
                return emprestimo
        raise ValueError("Empréstimo ativo não encontrado.")

    def listar_historico(self):
        return list(self._historico)

    def listar_ativos(self):
        return [item for item in self._historico if item.ativo]

    def quantidade_emprestimos_ativos(self):
        return len(self.listar_ativos())
