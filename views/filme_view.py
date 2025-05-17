class FilmeView:

    def mostrar_tela(self):
        print("\nFilmes\n")
        print("1 - Visualizar filmes")
        print("2 - Cadastrar filme")
        print("3 - Editar filme")
        print("0 - Voltar")
        opcao = input(">> ")
        return opcao

    def visualizar_filmes(self, filmes):
        for filme in filmes:
            print(filme)

    def cadastrar_filme(self):
        print("\nCadastrar filme\n")
        print("Digite os dados do filme")
        nome = input("Titulo: ")
        ano_lancamento = input("Ano de lançamento: ")
        diretor = input("Diretor: ")
        return nome, ano_lancamento, diretor