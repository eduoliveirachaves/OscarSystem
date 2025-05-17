class CategoriaView:

    def mostrar_tela(self):
        print("\nCategorias\n")
        print("1 - Visualizar categorias")
        print("2 - Cadastrar categoria")
        print("3 - Editar categoria")
        print("0 - Voltar")
        opcao = input("\nDigite a opção desejada: ")
        return opcao

    def visualizar(self):
        print("\nCategorias\n")
        print("1 - Visualizar as categorias disponíveis")
        print("2 - Visualizar os indicados")
        print("3 - Visualizar o andamento da votação")
        print("0 - Voltar")
        opcao = input("\nDigite a opção desejada: ")
        return opcao

    def visualizar_todas(self, categorias: list):
        for categoria in categorias:
            print(categoria.nome)

    def visualizar_indicados(self, categorias: list):
        for categoria in categorias:
            print(categoria.nome)
            print("Indicados: " + ", ".join([str(x) for x in categoria.indicados]))

        def visualizar_votos(self, categorias: list):
            for categoria in categorias:
                print(categoria.votos)
