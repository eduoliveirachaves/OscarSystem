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
            print("")


    def cadastrar_categoria(self):
        print("\nCadastrar categoria\n")
        print("Digite o nome da categoria")
        nome = input("Nome: ")
        print(f"Categoria {nome} cadastrada com sucesso!")
        return nome

    def editar_tela(self):
        print("\nEditar categoria\n")
        print("1 - Adicionar indicados")
        print("2 - Remover indicados")
        print("3 = Editar nome")
        print("0 - Sair")
        opcao = input("\nDigite a opção desejada: ")
        return opcao

    def remover_indicados(self, categorias: list):
        pass

    def editar_nome(self, categorias: list):
        pass
