from controllers.categoria_controller import CategoriaController
from controllers.membro_controller import MembroController
from controllers.profissional_controller import ProfissionalController
from controllers.filme_controller import FilmeController
from controllers.votacao_controller import VotacaoController
from models.edicao import Edicao
from views.edicao_view import EdicaoView


class EdicaoController:
    def __init__(self, edicao: Edicao, membros_controller: MembroController, categoria_controller: CategoriaController,
                 filme_controller: FilmeController, profissional_controller: ProfissionalController, votacao_controller: VotacaoController):

        self.__edicao = edicao
        self.__membro_controller = membros_controller
        self.__view = EdicaoView()

        self.__categoria_controller = categoria_controller
        self.__profissional_controller = profissional_controller
        self.__filme_controller = filme_controller
        self.__votos_controller = votacao_controller

    @property
    def edicao(self):
        return self.__edicao

    def iniciar(self):
        opcao = self.__view.mostrar_tela(self.__edicao.ano)
        while opcao != "0":
            if opcao == "1":
                self.edicao_menu()
            elif opcao == "2":
                self.__votos_controller.iniciar()
            else:
                print("Opção inválida")

            opcao = self.__view.mostrar_tela(self.__edicao.ano)

    def edicao_menu(self):
        opcao = self.__view.edicao_tela(self.__edicao.ano)
        while opcao != "0":
            if opcao == "1":
                self.__filme_controller.iniciar()
            elif opcao == "2":
                self.__profissional_controller.iniciar()
            elif opcao == "3":
                self.__categoria_controller.iniciar()
            else:
                print("Opção inválida")
            opcao = self.__view.edicao_tela(self.__edicao.ano)

    def get_categoria_by_id(self, categoria_id):
        return self.__categoria_controller.get_categoria_by_id(categoria_id)


