from models.edicao import Edicao
from models.indicavel import Indicavel


class Indicacao:

    def __init__(self, indicado: Indicavel, edicao: Edicao):
        self.__indicado = indicado
        self.__edicao = edicao
        self.__votos = 0



    def nome(self):
        self.__indicado.nome

    def edicao(self):
        return

    def add_categoria(self, categoria):
        pass

    def add_voto(self):
        self.__votos += 1

    def __str__(self):
        return f"{self.__indicado} - {self.} - {self.__votos}"



