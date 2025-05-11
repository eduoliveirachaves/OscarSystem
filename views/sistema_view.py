class SistemaView:

    def __init__(self):
        pass

    def mostrar_tela(self):
        print("Bem vindo ao sistema do Oscar")
        print("1 - Visualizar Votos")
        print("2 - Area para membros")
        print("3 - Area para admin")
        print("0 - Sair")
        opcao = input("Digite a opção desejada: ")
        return opcao

