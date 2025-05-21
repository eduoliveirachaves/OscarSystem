from controllers.edicao_controller import EdicaoController
from controllers.membro_controller import MembroController
from models.edicao import Edicao
from views.sistema_view import SistemaView


class EdicoesController:
    def __init__(self, carregar_dados: bool = False):
        self.__carregar_dados = carregar_dados
        self.__sistema_view = SistemaView()
        self.__edicoes = self.carregar_edicoes(carregar_dados)
        self.__membro_controller = None

    @property
    def edicoes(self):
        return self.__edicoes

    def iniciar(self, membro_controller: MembroController):
        opcao = self.__sistema_view.mostrar_tela()
        self.__membro_controller = membro_controller
        while opcao != "0":
            if opcao == "1":
                edicao = self.escolher_edicao()

                if edicao:
                    edicao_controller = EdicaoController(self.__carregar_dados, edicao, self.__membro_controller)
                    edicao_controller.iniciar()

            elif opcao == "2":
                self.cadastro()

            else:
                print("Opção inválida")
            opcao = self.__sistema_view.mostrar_tela()

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

    def cadastro(self):
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
