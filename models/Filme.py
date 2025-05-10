class Filme:
    # genero? custo? bilheteria? duracao? elenco?
    def __init__(self, titulo: str, diretor: str, ano: int, categorias_concorrendo: []):
        self.__titulo = titulo
        self.__diretor = diretor
        self.__ano = ano
        self.__categorias_concorrendo = categorias_concorrendo

