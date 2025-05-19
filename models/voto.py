from models.categoria import Categoria


class Voto:
    def __init__(self, membro, categoria: Categoria, escolhido):
        self.__membro = membro
        self.__categoria = categoria #!
        # DUVIDA: (categoria aqui) pode ser considerado duplicado ja que a propria categoria
        # rastreia os votos, mas acho que possa ser util para descobrir se o membro ja votou
        # naquela categoria mais rapidamente
        self.__escolhido = escolhido

    @property
    def membro(self):
        return self.__membro

    @property
    def categoria(self):
        return self.__categoria

    @property
    def escolhido(self):
        return self.__escolhido

    def __str__(self):
        return f"{self.__membro.nome} - {self.__categoria.nome} - {self.__escolhido.nome}"
