class UserView:

    def mostrar_tela(self):
        print("\nLISTAGEM\n")
        # DUVIDA
        # print("1 - Visualizar Votos") // nao eh publico / eu deveria exibir aqui mesmo assim?
        # estou pensando em algo minimamente real onde o publico simplesmente nao teria acesso
        # mas tambem se for apenas pra cumprir os requisitors tudo pode ser exibido aqui
        print("1 - Visualizar Filmes")
        print("2 - Visualizar Categorias")
        print("3 - Visualizar Atores")
        print("4 - Visualizar Diretores")
        print("5 - Visualizar Membros da Academia")
        print("0 - Voltar")
        opcao = input("\nDigite a opção desejada: ")
        print("")
        return opcao

    def visualizar_filmes(self, filmes):
        for filme in filmes:
            print(filme)

    def visualizar_categorias(self, categorias):
        for categoria in categorias:
            print(categoria)


    def visualizar_atores(self, atores):
        for ator in atores:
            print(ator)

    def visualizar_diretores(self, diretores):
        for diretor in diretores:
            print(diretor)

    def visualizar_membros(self, membros):
        for membro in membros:
            print(membro)