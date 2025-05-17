class Categoria:
    # tipo se refere a que tipo de indicados a lista tera! como para filmes ou para atores ou para pessoas que .....
    def __init__(self, id_counter, nome, tipo_indicados):
        self.__id_counter = id_counter
        self.__nome = nome
        self.__indicados = []
        self.__votos = []
        self.__tipo_indicados = tipo_indicados

    @property
    def id_counter(self):
        return self.__id_counter

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
        pass

    def __str__(self):
        return f"{self.__id_counter} - {self.__nome} - {self.__tipo_indicados}"
