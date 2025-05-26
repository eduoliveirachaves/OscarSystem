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
        tipo = input("Feito para? (Filme/Ator/Atriz/Diretor): ")
        print(f"Categoria {nome} cadastrada com sucesso!")
        return nome, tipo

    def editar_tela(self):
        print("\nEditar categoria\n")
        print("1 - Adicionar indicados")
        print("2 - Remover indicados")
        print("3 = Editar nome")
        print("0 - Sair")
        opcao = input("\nDigite a opção desejada: ")
        return opcao

    def selecionar_categoria(self, categorias: list):
        print("\nSelecione a categoria:")
        for categoria in categorias:
            print(f"{categoria.id} - {categoria.nome}")
        categoria_id = input("Digite o ID da categoria: ")
        if not categoria_id.isdigit() or int(categoria_id) not in [cat.id for cat in categorias]:
            print("ID inválido. Tente novamente.")
            return None

        return categoria_id

    def selecionar_nomeacao_tela(self, indicaveis: list):
        print("\nDisponiveis para esta categoria:")
        for indicavel in indicaveis:
            print(f"{indicavel.id} - {indicavel.nome}")
        id = input("Digite o ID: ")
        return id

    def remover_indicados(self, categorias: list):
        pass

    def editar_nome(self, categorias: list):
        pass
