from models.pessoa import Pessoa


class Ator(Pessoa):
    def __init__(self, ID, nome, nacionalidade, data_nascimento: str):
        super().__init__(nome)
        self.__id = ID
        self.__data_nascimento = data_nascimento
        self.__nacionalidade = nacionalidade


    @property
    def id(self):
        return self.__id

    @property
    def data_nascimento(self):
        return self.__data_nascimento

    @property
    def nacionalidade(self):
        return self.__nacionalidade

    @property
    def nome(self):
        return super().nome

    @data_nascimento.setter
    def data_nascimento(self, data_nascimento):
        self.__data_nascimento = data_nascimento

    @nacionalidade.setter
    def nacionalidade(self, nacionalidade):
        self.__nacionalidade = nacionalidade

    @nome.setter
    def nome(self, nome):
        super().nome = nome

    def __str__(self):
        return f"{self.nome} - {self.data_nascimento} - {self.nacionalidade}"



