from models.pessoa import Pessoa


class Membro(Pessoa):

    def __init__(self, ID, nome, data_nascimento, nacionalidade):
        super().__init__(nome)
        self.__id = ID
        self.__nome = nome
        self.__data_nascimento = data_nascimento
        self.__nacionalidade = nacionalidade
        self.__votos = []

    @property
    def id(self):
        return self.__id

    @property
    def nome(self):
        return self.__nome

    @property
    def data_nascimento(self):
        return self.__data_nascimento

    @property
    def nacionalidade(self):
        return self.__nacionalidade

    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    @data_nascimento.setter
    def data_nascimento(self, data_nascimento):
        self.__data_nascimento = data_nascimento

    @nacionalidade.setter
    def nacionalidade(self, nacionalidade):
        self.__nacionalidade = nacionalidade

    def add_voto(self, voto):
        self.__votos.append(voto)

    def __str__(self):
        return f"{self.nome} - {self.data_nascimento} - {self.nacionalidade}"
