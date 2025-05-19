from typing import List

from models.categoria import Categoria
from models.filme import Filme
from models.indicavel import Indicavel
from models.profissional import Profissional
from models.voto import Voto


class Edicao:

    def __init__(self, ano: int):
        self.__ano = ano
        self.__filmes: List[Filme] = []
        self.__categorias: List[Categoria] = []
        self.__profissionais: List[Profissional] = []
        self.__votos: List[Voto] = []
        self.__filmes_id = 1
        self.__atores_id = 1
        self.__diretores_id = 1
        self.__categorias_id = 1

    @property
    def ano(self):
        return self.__ano

    @property
    def categorias(self):
        return self.__categorias

    @property
    def votos(self):
        return self.__votos

    @property
    def filmes(self):
        return self.__filmes

    @property
    def profissionais(self):
        return self.__profissionais

    @property
    def categorias_id(self):
        counter = self.__categorias_id
        self.__categorias_id += 1
        return counter

    @property
    def filmes_id(self):
        counter = self.__filmes_id
        self.__filmes_id += 1
        return counter

    @property
    def atores_id(self):
        counter = self.__atores_id
        self.__atores_id += 1
        return counter

    @property
    def diretores_id(self):
        counter = self.__diretores_id
        self.__diretores_id += 1
        return counter
