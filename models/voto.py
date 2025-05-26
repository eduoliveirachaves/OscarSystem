class Voto:
    def __init__(self, membro, categoria):
        self.__membro = membro
        self.__categoria = categoria



    @property
    def membro(self):
        return self.__membro

    @membro.setter
    def membro(self, membro):
        self.__membro = membro

    @property
    def categoria(self):
        return self.__categoria

    @categoria.setter
    def categoria(self, categoria):
        self.__categoria = categoria



    def __str__(self):
        return f"{self.__membro.nome} - {self.__categoria.nome}"
