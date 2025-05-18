class SistemaView:

    def __init__(self):
        pass

    def mostrar_tela(self):
        print("\nBem vindo ao sistema do Oscar\n")
        print("1 - Relatórios")
        print("2 - Membros da Academia")
        print("0 - Sair")
        opcao = input("\nDigite a opção desejada: ")
        return opcao

