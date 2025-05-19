from controllers.admin_controller import AdminController
from controllers.membro_controller import MembroController
from controllers.user_controller import UserController
from models.edicao import Edicao
from views.sistema_view import SistemaView


class SistemaController:
    def __init__(self, carregar_dados: bool = False):
        self.__carregar_dados = carregar_dados
        self.__sistema_view = SistemaView()
        self.__edicoes = self.carregar_edicoes(self.__carregar_dados)
        self.__membro_controller = MembroController([])
        self.__user_controller = UserController(self)

    @property
    def edicoes(self):
        return self.__edicoes

    def iniciar(self):
        opcao = self.__sistema_view.mostrar_tela()

        while opcao != "0":
            if opcao == "1":
                self.__user_controller.iniciar()
            elif opcao == "2":
                self.__membro_controller.iniciar()
            elif opcao == "3":
                self.edicoes_menu()
            else:
                print("Opção inválida")
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

    def add_edicao(self, ano):
        ano = int(ano)
        edicao = Edicao(ano)
        self.__edicoes.append(edicao)
        return edicao

    def get_edicao_by_ano(self, ano):
        return next((edicao for edicao in self.__edicoes if edicao.ano == ano), None)

    def carregar_edicoes(self, carregar_dados):
        if carregar_dados:
            return [Edicao(2024), Edicao(2023), Edicao(2022)]
        return []

    def edicoes_menu(self):
        edicao = self.__sistema_view.edicao_tela()
        while edicao != "0":
            if edicao == "1":
                res = self.escolher_edicao()

                if res:
                    self.home(res)


            elif edicao == "2":
                res = self.cadastro_edicao()
                if res:
                    self.add_edicao(res)
                    print("Edição cadastrada com sucesso!")
                    edicao = self.__sistema_view.edicao_tela()
                    continue

            else:
                print("Opção inválida")
            edicao = self.__sistema_view.edicao_tela()

    def cadastro_edicao(self):
        ano = self.__sistema_view.cadastrar_edicao_tela([edicao.ano for edicao in self.__edicoes])
        while ano != "0":
            if ano is not None and int(ano) not in [e.ano for e in self.__edicoes]:
                return ano
            print("Valor inválido. Tente novamente.")
            ano = self.__sistema_view.cadastrar_edicao_tela([edicao.ano for edicao in self.__edicoes])
        return None

    def escolher_edicao(self):
        escolha = self.__sistema_view.escolher_edicao_tela(self.__edicoes)

        if escolha is None or escolha == "0" or escolha not in [str(e.ano) for e in self.__edicoes]:
            return None

        edicao = self.get_edicao_by_ano(int(escolha))
        return edicao
