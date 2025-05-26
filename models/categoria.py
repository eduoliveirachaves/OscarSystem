from typing import List

from models.indicacao import Indicacao


class Categoria:
    # tipo se refere a que tipo de indicados a lista tera! como para filmes ou para atores ou para pessoas que ..
    def __init__(self, id_counter, nome, tipo_indicados):
        self.__id = id_counter
        self.__nome = nome
        self.__indicados: List[Indicacao] = []
        self.__tipo_indicados = tipo_indicados  # tipo de indicados, como filme, ator, diretor, etc.
        self.__vencedor = "Nenhum"

    @property
    def id(self):
        return self.__id

    @property
    def nome(self):
        return self.__nome

    @property
    def vencedor(self):
        return self.__vencedor

    @property
    def indicados(self):
        return self.__indicados

    @property
    def tipo_indicados(self):
        return self.__tipo_indicados

    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    def add_indicado(self, indicado):
        self.__indicados.append(indicado)

    def definir_vencedor(self):
        vencedor = None
        if not self.__indicados:
            return None

        max_votos = max(len(ind.votos) for ind in self.__indicados)
        vencedores: List[Indicacao] = [ind for ind in self.__indicados if len(ind.votos) == max_votos]

        if len(vencedores) == 1:
            vencedor = vencedores[0].indicado
        else:
            # criar criterio de desempate !
            vencedor = vencedores[0].indicado

        self.__vencedor = vencedor

        return self.__vencedor

    def __str__(self):
        return f"{self.__id} - {self.__nome}"
