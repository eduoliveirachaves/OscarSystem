from controllers.membro_controller import MembroController
from controllers.edicoes_controller import EdicoesController
from controllers.user_controller import UserController
from views.app_view import AppView


class AppController:

    def __init__(self, carregar_dados: bool = False):
        self.__membro_controller = MembroController([])
        self.__sistema_controller = EdicoesController(carregar_dados)
        self.__user_controller = UserController()
        self.__view = AppView()

    def iniciar(self):
        opcao = self.__view.mostrar_tela()

        while opcao != "0":
            if opcao == "1":
                self.__user_controller.iniciar(self.__sistema_controller)
            elif opcao == "2":
                self.__membro_controller.iniciar()
            elif opcao == "3":
                self.__sistema_controller.iniciar(self.__membro_controller)
            else:
                print("Opção inválida")
            opcao = self.__view.mostrar_tela()
