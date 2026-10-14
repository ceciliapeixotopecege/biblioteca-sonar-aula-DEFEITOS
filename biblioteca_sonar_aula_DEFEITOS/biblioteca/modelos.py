"""Modelos de domínio usados pela aplicação."""
from dataclasses import dataclass


@dataclass
class Livro:
    isbn: str
    titulo: str
    autor: str
    ano: int
    disponivel: bool = True

    def __post_init__(self):
        if not self.isbn.strip():
            raise ValueError("O ISBN é obrigatório.")
        if not self.titulo.strip():
            raise ValueError("O título é obrigatório.")
        if not self.autor.strip():
            raise ValueError("O autor é obrigatório.")
        if self.ano < 0:
            raise ValueError("O ano não pode ser negativo.")
