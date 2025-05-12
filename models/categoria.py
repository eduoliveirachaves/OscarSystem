class Categoria:
    def __init__(self, nome):
        self.__nome = nome
        self.__indicados = []
        self.__votos = []

    def add_indicado(self, indicado):
        pass

    def add_voto(self, voto):
        pass

    def __str__(self):
        return self.__nome