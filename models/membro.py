from models.profissional import Profissional
from models.voto import Voto


class Membro(Profissional):
    _id_counter = 1
    def __init__(self, nome, data_nascimento, nacionalidade):
        super().__init__(nome, data_nascimento)
        self.__id = Membro._id_counter
        self.__nacionalidade = nacionalidade
        self.__votos = []
        Membro._id_counter += 1

    @property
    def id(self):
        return self.__id

    @property
    def nome(self):
        return self._nome

    @property
    def data_nascimento(self):
        return self._data_nascimento

    @property
    def nacionalidade(self):
        return self.__nacionalidade

    @property
    def votos(self):
        return self.__votos

    @nome.setter
    def nome(self, nome):
        self._nome = nome

    @data_nascimento.setter
    def data_nascimento(self, data_nascimento):
        self._data_nascimento = data_nascimento

    @nacionalidade.setter
    def nacionalidade(self, nacionalidade):
        self.__nacionalidade = nacionalidade

    def add_voto(self, voto: Voto):
        self.__votos.append(voto)

    def __str__(self):
        return f"{self._nome} - {self._data_nascimento} - {self.__nacionalidade}"
