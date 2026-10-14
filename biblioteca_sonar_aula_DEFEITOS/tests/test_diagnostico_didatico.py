import unittest
from biblioteca.diagnostico_didatico import avaliar_emprestimo


class TestDiagnosticoDidatico(unittest.TestCase):
    def test_aluno_aprovado(self):
        self.assertEqual(avaliar_emprestimo("aluno", 0, 1, 20, False, False), "aprovado")

    def test_professor_bloqueado(self):
        self.assertEqual(avaliar_emprestimo("professor", 15, 2, 40, False, False), "bloqueado")
