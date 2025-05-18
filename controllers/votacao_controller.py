from typing import List

from models.voto import Voto


class VotacaoController:

    def __init__(self, votos: List[Voto]):
        self.__votos = votos

    def iniciar(self):
        pass