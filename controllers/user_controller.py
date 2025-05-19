from typing import List

from controllers.admin_controller import AdminController
from controllers.membro_controller import MembroController
from models.edicao import Edicao
from views.user_view import UserView


class UserController:
    def __init__(self, sistema_controller):
        self.__sistema_controller = sistema_controller
        self.__edicoes = self.__sistema_controller.edicoes
        self.__view = UserView()

    def iniciar(self):
        opcao = self.__view.mostrar_tela()
        edicoes = self.__sistema_controller.edicoes

        while opcao != "0":
            if opcao == "1":
                self.relatorios_gerais(edicoes)
            elif opcao == "2":
                self.selecionar_edicao(edicoes)
            else:
                print("Opção inválida")
            opcao = self.__view.mostrar_tela()

    def relatorios_gerais(self, edicoes: List[Edicao]):
        pass

    def selecionar_edicao(self, edicoes: list[Edicao]):
        ano = self.__view.selecionar_edicao_tela(edicoes)

        while ano != "0":
            if ano in [str(e.ano) for e in edicoes]:
                self.edicao_especifica(self.__sistema_controller.get_edicao_by_ano(ano))

            print("Valor inválido. Tente novamente.")
            ano = self.__view.selecionar_edicao_tela(edicoes)

    def edicao_especifica(self, edicao: Edicao):
        pass
