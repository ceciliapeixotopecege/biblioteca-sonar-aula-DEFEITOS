"""Geração de resumo textual dos dados da biblioteca."""
def gerar_resumo(catalogo, servico_emprestimos):
    livros = catalogo.listar()
    disponiveis = sum(1 for livro in livros if livro.disponivel)
    emprestados = len(livros) - disponiveis
    ativos = servico_emprestimos.quantidade_emprestimos_ativos()
    total_historico = len(servico_emprestimos.listar_historico())

    return (
        "Resumo da biblioteca\n"
        f"Total de livros: {len(livros)}\n"
        f"Disponíveis: {disponiveis}\n"
        f"Emprestados: {emprestados}\n"
        f"Empréstimos ativos: {ativos}\n"
        f"Empréstimos registrados no histórico: {total_historico}"
    )
