class Categoria:
    __id_counter = 1
    # tipo se refere a que tipo de indicados a lista tera! como para filmes ou para atores ou para pessoas que .....
    def __init__(self, nome):
        self.__id = Categoria.__id_counter
        self.__nome = nome
        self.__indicados = []
        self.__votos = []
        self.__tipo_indicados = "" # implementar

        Categoria.__id_counter += 1

    @property
    def id(self):
        return self.__id

    @property
    def nome(self):
        return self.__nome

    @property
    def indicados(self):
        return self.__indicados

    @property
    def votos(self):
        return self.__votos

    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    def add_indicado(self, indicado):
        self.__indicados.append(indicado)

    def add_voto(self, voto):
        self.__votos.append(voto)

    def __str__(self):
        return f"{self.__id} - {self.__nome} - {self.__tipo_indicados}"
