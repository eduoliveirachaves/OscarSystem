from controllers.membro_controller import MembroController
from controllers.edicoes_controller import EdicoesController
from controllers.relatorios_controller import RelatoriosController
from views.app_view import AppView


class AppController:

    def __init__(self):
        self.__membro_controller = MembroController()
        self.__edicoes_controller = EdicoesController(membro_controller=self.__membro_controller)
        self.__relatorio_controller = RelatoriosController(self.__edicoes_controller)
        self.__view = AppView()

    def iniciar(self):
        opcao = self.__view.mostrar_tela()

        while opcao != "0":
            if opcao == "1":
                self.__edicoes_controller.iniciar()
            elif opcao == "2":
                self.__membro_controller.iniciar()
            elif opcao == "3":
                self.__relatorio_controller.iniciar()
            else:
                print("Opção inválida")
            opcao = self.__view.mostrar_tela()
