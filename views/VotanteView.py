class VotanteView:
    def __init__(self, votante):
        self.__votante = votante
        self.mostrar_tela()

    def mostrar_tela(self):
        print(f'Bem Vindo ao Sistema de Votação ${self.__votante.nome}')

