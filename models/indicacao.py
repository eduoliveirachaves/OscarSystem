from models.indicavel import Indicavel


class Indicacao:

    def __init__(self, indicado: Indicavel):
        self.__indicado: Indicavel = indicado
        self.__votos = 0

    @property
    def indicado(self):
        return self.__indicado

    @property
    def votos(self):
        return self.__votos

    @indicado.setter
    def indicado(self, indicado):
        self.__indicado = indicado


    def add_voto(self):
        self.__votos += 1

    def remove_voto(self):
        if self.__votos == 0:
            return

        self.__votos -= 1

    def __str__(self):
        return f"{self.__indicado} - {self.__votos}"
