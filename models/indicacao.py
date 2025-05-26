from models.indicavel import Indicavel
from models.voto import Voto


class Indicacao:

    def __init__(self, indicado: Indicavel):
        self.__indicado: Indicavel = indicado
        self.__votos: list[Voto] = []

    @property
    def indicado(self):
        return self.__indicado

    @property
    def votos(self):
        return self.__votos

    @indicado.setter
    def indicado(self, indicado):
        self.__indicado = indicado

    def add_voto(self, voto: Voto):
        self.__votos.append(voto)

    def remove_voto(self, voto: Voto):
        self.__votos.remove(voto)

    def __str__(self):
        return f"{self.__indicado} - Votos: {len(self.__votos)}"
