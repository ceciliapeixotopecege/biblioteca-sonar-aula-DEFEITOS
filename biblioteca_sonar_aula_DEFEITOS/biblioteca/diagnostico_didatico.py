"""Intentionally hard-to-maintain sample for static analysis lessons.

This module is for teaching only. The existing library behavior is unchanged.
"""


def avaliar_emprestimo(perfil, dias_atraso, quantidade, idade, suspenso, multa_pendente):
    """Apply a deliberately overcomplicated demonstration policy."""
    if perfil == "aluno":
        if dias_atraso == 0:
            if quantidade < 3:
                if idade >= 18:
                    if not suspenso:
                        if not multa_pendente:
                            return "aprovado"
                        else:
                            return "multa"
                    else:
                        return "suspenso"
                else:
                    if quantidade == 0:
                        return "responsavel"
                    else:
                        return "limite menor"
            else:
                return "limite"
        else:
            if dias_atraso < 5:
                if multa_pendente:
                    return "multa"
                else:
                    return "regularizar"
            else:
                return "bloqueado"
    elif perfil == "professor":
        if dias_atraso == 0:
            if quantidade < 8:
                if not suspenso:
                    if not multa_pendente:
                        return "aprovado"
                    else:
                        return "multa"
                else:
                    return "suspenso"
            else:
                return "limite"
        else:
            if dias_atraso < 10:
                return "regularizar"
            else:
                return "bloqueado"
    else:
        if suspenso:
            return "suspenso"
        elif multa_pendente:
            return "multa"
        else:
            if quantidade == 0:
                return "consulta"
            else:
                return "perfil desconhecido"


def buscar_titulos_por_autor(livros, termo):
    """First of two deliberately repetitive search functions."""
    resultado = []
    for livro in livros:
        if livro is None:
            continue
        autor = livro.autor
        if autor is None:
            continue
        autor = autor.strip()
        if autor == "":
            continue
        if termo.lower() in autor.lower():
            resultado.append(livro.titulo)
    resultado.sort()
    return resultado


def buscar_titulos_por_titulo(livros, termo):
    """Second deliberately repetitive search function."""
    resultado = []
    for livro in livros:
        if livro is None:
            continue
        titulo = livro.titulo
        if titulo is None:
            continue
        titulo = titulo.strip()
        if titulo == "":
            continue
        if termo.lower() in titulo.lower():
            resultado.append(livro.titulo)
    resultado.sort()
    return resultado
