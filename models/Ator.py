from models.Pessoa import Pessoa


class Ator(Pessoa):
    def __init__(self, ID, nome, nacionalidade, data_nascimento: str,  filmes: []):
        super().__init__(nome)
        self.__id = ID
        self.__data_nascimento = data_nascimento
        self.__nacionalidade = nacionalidade
        self.__filmes = filmes

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
    def filmes(self):
        return self.__filmes

    @filmes.setter
    def filmes(self, filmes):
        self.__filmes = filmes





