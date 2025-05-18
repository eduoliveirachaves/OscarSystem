class AdminView:

    def __init__(self):
        pass

    # ainda nao sei se a tela vai possivelmente precisar de alguma variavel da classe
    @staticmethod
    def mostrar_tela():
        print("\nADMIN\n")
        print("1 - Filmes")
        print("2 - Profissionais do Cinema")
        print("3 - Categorias")
        print("4 - Membros")
        print("5 - Votos")
        print("0 - Voltar")
        opcao = input("\nDigite a opção desejada: ")
        return opcao
