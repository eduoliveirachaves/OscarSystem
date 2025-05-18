from models.profissional import Profissional


class Ator(Profissional):

    def __init__(self, nome, nacionalidade, data_nascimento: str):
        super().__init__(nome, data_nascimento)
        self.__nacionalidade = nacionalidade
        self.__categoria_concorrendo = []


    @property
    def id(self):
        return self._id

    @property
    def data_nascimento(self):
        return self._data_nascimento

    @property
    def nacionalidade(self):
        return self.__nacionalidade

    @property
    def nome(self):
        return self._nome

    @data_nascimento.setter
    def data_nascimento(self, data_nascimento):
        self._data_nascimento = data_nascimento

    @nacionalidade.setter
    def nacionalidade(self, nacionalidade):
        self.__nacionalidade = nacionalidade

    @nome.setter
    def nome(self, nome):
        self._nome = nome

    def add_categoria_concorrendo(self, categoria):
        self.__categoria_concorrendo.append(categoria)

    def __str__(self):
        return f"[{self._id}] - {self._nome} - {self._data_nascimento} - {self.__nacionalidade}"



