from typing import List

from models.filme import Filme
from views.filme_view import FilmeView


class FilmeController:

    def __init__(self, filmes: List[Filme]):
        self.__filmes: List[Filme] = filmes
        self.__view = FilmeView()

    def iniciar(self):
        opcao = self.__view.mostrar_tela()

        while opcao != "0":
            if opcao == "1":
                self.__view.visualizar_filmes(self.__filmes)
            elif opcao == "2":
                nome, ano, diretor = self.__view.cadastrar_filme()
                self.__filmes.append(Filme(nome, ano, diretor))
            elif opcao == "3":
                # self.__view.editar_filme()
                continue
            else:
                print("Opção inválida")

