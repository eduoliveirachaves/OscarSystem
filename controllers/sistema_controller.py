from controllers.admin_controller import AdminController
from controllers.user_controller import UserController
from controllers.membro_controller import MembroController
from controllers.votacao_controller import VotacaoController
from models.edicao import Edicao
from views import sistema_view
from views.sistema_view import SistemaView


class SistemaController:
    def __init__(self, carregar_dados: bool = False):
        self.__carregar_dados = carregar_dados
        self.__sistema_view = SistemaView()
        self.__edicoes = self.carregar_edicoes(self.__carregar_dados)
        self.__user_controller = UserController(self.__edicoes)
        self.__membro_controller = MembroController([])

    def iniciar(self):
        opcao = self.__sistema_view.mostrar_tela()

        while opcao != "0":
            for edicao in self.__edicoes:
                if int(opcao) == edicao.ano:
                    self.home(edicao)

            self.cadastrar_edicao()

            opcao = self.__sistema_view.mostrar_tela()

    def home(self, edicao: Edicao):
        admin_controller = AdminController(self.__carregar_dados, edicao, self.__membro_controller)
        while True:
            opcao = self.__sistema_view.home_tela(edicao.ano)
            if opcao == "1":
                # ver os votos contagem/categorias {ver tambem os filmes listados?} (opcao publica) | LISTAR |
                # votos controller
                self.__user_controller.iniciar()
            elif opcao == "2":
                # area para membros da academia cadastros/editar/listar/ etc.
                admin_controller.iniciar()
            elif opcao == "0":
                return
            else:
                print("Opção inválida")

    def cadastrar_edicao(self):
        pass

    def get_edicao_by_ano(self, ano):
        return next((edicao for edicao in self.__edicoes if edicao.ano == ano), None)

    def carregar_edicoes(self, carregar_dados):
        if carregar_dados:
            return [Edicao(2024), Edicao(2023), Edicao(2022)]
        return []
