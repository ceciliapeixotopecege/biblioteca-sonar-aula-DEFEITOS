"""Interface de linha de comando do sistema Biblioteca Fácil."""
from biblioteca.catalogo import Catalogo
from biblioteca.emprestimos import ServicoEmprestimos
from biblioteca.modelos import Livro
from biblioteca.relatorios import gerar_resumo


def mostrar_menu():
    print("\n=== BIBLIOTECA FÁCIL ===")
    print("1 - Cadastrar livro")
    print("2 - Listar livros")
    print("3 - Registrar empréstimo")
    print("4 - Devolver livro")
    print("5 - Mostrar resumo")
    print("0 - Sair")


def executar():
    catalogo = Catalogo()
    emprestimos = ServicoEmprestimos(catalogo)
    catalogo.adicionar(Livro("978000000001", "Python para iniciantes", "Ana Lima", 2022))
    catalogo.adicionar(Livro("978000000002", "Qualidade de Software", "Bruno Alves", 2021))

    while True:
        mostrar_menu()
        opcao = input("Escolha: ").strip()
        if opcao == "1":
            isbn = input("ISBN: ").strip()
            titulo = input("Título: ").strip()
            autor = input("Autor: ").strip()
            try:
                ano = int(input("Ano de publicação: "))
                catalogo.adicionar(Livro(isbn, titulo, autor, ano))
                print("Livro cadastrado.")
            except (ValueError, TypeError) as erro:
                print(f"Não foi possível cadastrar: {erro}")
        elif opcao == "2":
            livros = catalogo.listar()
            if not livros:
                print("Nenhum livro cadastrado.")
            for livro in livros:
                estado = "disponível" if livro.disponivel else "emprestado"
                print(f"{livro.titulo} — {livro.autor} ({livro.isbn}) — {estado}")
        elif opcao == "3":
            isbn = input("ISBN do livro: ").strip()
            pessoa = input("Nome do leitor: ").strip()
            try:
                emprestimos.emprestar(isbn, pessoa)
                print("Empréstimo registrado.")
            except ValueError as erro:
                print(f"Erro: {erro}")
        elif opcao == "4":
            isbn = input("ISBN do livro: ").strip()
            try:
                emprestimos.devolver(isbn)
                print("Devolução registrada.")
            except ValueError as erro:
                print(f"Erro: {erro}")
        elif opcao == "5":
            print(gerar_resumo(catalogo, emprestimos))
        elif opcao == "0":
            print("Até logo!")
            break
        else:
            print("Opção inválida. Escolha uma opção do menu.")


if __name__ == "__main__":
    executar()
