from typing import List

from models.ator import Ator
from models.diretor import Diretor
from views.profissional_view import ProfissionalView


class ProfissionalController:

    def __init__(self, atores: List[Ator], diretores: List[Diretor] = []):
        self.__atores: List[Ator] = atores
        self.__diretores: List[Diretor] = diretores
        self.__profissional_view = ProfissionalView()

    def iniciar(self):
        opcao = self.__profissional_view.mostrar_tela()

        while opcao != "0":
            if opcao == "1":
                self.listagens()
            elif opcao == "2":
                self.cadastros()
            elif opcao == "3":
                self.editar()
            else:
                print("Opção inválida")

    def listagens(self):
        # todos / atores / diretores
        qual_profissional = self.__profissional_view.tela_visualizar()

        while qual_profissional != "0":

            if qual_profissional == "1":
                self.__profissional_view.visualizar_todos(self.__atores, self.__diretores)
            elif qual_profissional == "2":
                self.__profissional_view.visualizar_atores(self.__atores)
            elif qual_profissional == "3":
                self.__profissional_view.visualizar_diretores(self.__diretores)

            qual_profissional = self.__profissional_view.tela_visualizar()

    def cadastros(self):
        opcao = self.__profissional_view.tela_cadastro()

        while opcao != "0":
            if opcao == "1":
                nome, nacionalidade, data_nascimento = self.__profissional_view.cadastrar_ator()
                self.__atores.append(Ator(nome, nacionalidade, data_nascimento))
            elif opcao == "2":
                nome, data_nascimento = self.__profissional_view.cadastrar_diretor()
                self.__diretores.append(Diretor(nome, data_nascimento))
            else:
                print("Opção inválida")

    def editar(self):
        pass