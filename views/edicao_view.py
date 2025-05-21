class EdicaoView:

    def __init__(self):
        pass

    def mostrar_tela(self, ano):
        print(f"\n=== OSCAR {ano} ===\n")
        print("1 - Editar Edição")
        print("2 - Votar")
        print("\n0 - Voltar")
        return input("\nDigite a opção desejada: ")

    def edicao_tela(self, ano):
        print(f"\n=== OSCAR {ano} ===\n")
        print("1 - Filmes")
        print("2 - Profissionais do Cinema")
        print("3 - Categorias")
        print("\n0 - Voltar")
        opcao = input("\nDigite a opção desejada: ")
        return opcao
