from models.categoria import Categoria


class Voto:
    def __init__(self, id_membro: int, categoria: Categoria, escolhido):
        self.__id_membro = id_membro
        self.__categoria = categoria #!
        # DUVIDA: (categoria aqui) pode ser considerado duplicado ja que a propria categoria
        # rastreia os votos, mas acho que possa ser util para descobrir se o membro ja votou
        # naquela categoria mais rapidamente
        self.__escolhido = escolhido

    @property
    def id_membro(self):
        return self.__id_membro

    @property
    def categoria(self):
        return self.__categoria

    @property
    def escolhido(self):
        return self.__escolhido

    def __str__(self):
        return f"{self.id_membro} - {self.categoria} - {self.escolhido}"
