class SistemaView:

    def __init__(self):
        pass

    def mostrar_tela(self):
        print("\nBem vindo ao sistema do Oscar\n")
        print("1 - Visualizar informacoes")
        print("2 - Area para membros")
        print("3 - Area para admin")
        print("0 - Sair")
        opcao = input("\nDigite a opção desejada: ")
        return opcao

