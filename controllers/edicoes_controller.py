from controllers.categoria_controller import CategoriaController
from controllers.edicao_controller import EdicaoController
from controllers.filme_controller import FilmeController
from controllers.membro_controller import MembroController
from controllers.profissional_controller import ProfissionalController
from controllers.votacao_controller import VotacaoController
from data.data_loader import DataLoader
from models.ator import Ator
from models.edicao import Edicao
from models.membro import Membro
from views.edicoes_view import EdicoesView


class EdicoesController:
    def __init__(self, membro_controller: MembroController):
        self.__view = EdicoesView()
        self.__edicoes = []
        self.__membro_controller = membro_controller
        self.__categoria_controller = CategoriaController()
        self.__profissional_controller = ProfissionalController(self.__categoria_controller)
        self.__filme_controller = FilmeController(self.__profissional_controller, self.__categoria_controller)
        self.__votos_controller = VotacaoController(self.__membro_controller, self.__categoria_controller)

    @property
    def edicoes(self):
        return self.__edicoes

    def iniciar(self):
        opcao = self.__view.mostrar_tela()
        while opcao != "0":
            if opcao == "1":
                edicao = self.escolher_edicao()

                if edicao:
                    edicao_controller = self.get_edicao_controller(edicao)
                    self.carregar_dados(edicao.ano)
                    edicao_controller.iniciar()

            elif opcao == "2":
                edicao = self.cadastro()
                self.add_edicao(edicao)

            else:
                print("Opção inválida")
            opcao = self.__view.mostrar_tela()

    def add_edicao(self, ano):
        ano = int(ano)
        edicao = Edicao(ano)
        self.__edicoes.append(edicao)
        return edicao

    def get_edicao_by_ano(self, ano):
        return next((edicao for edicao in self.__edicoes if edicao.ano == ano), None)

    def cadastro(self):
        ano = self.__view.cadastrar_edicao_tela([edicao.ano for edicao in self.__edicoes])
        while ano != "0":
            if ano is not None and int(ano) not in [e.ano for e in self.__edicoes]:
                return ano
            print("Valor inválido. Tente novamente.")
            ano = self.__view.cadastrar_edicao_tela([edicao.ano for edicao in self.__edicoes])
        return None

    def escolher_edicao(self):
        escolha = self.__view.escolher_edicao_tela(self.__edicoes)

        if escolha is None or escolha == "0" or escolha not in [str(e.ano) for e in self.__edicoes]:
            return None

        edicao = self.get_edicao_by_ano(int(escolha))
        return edicao

    def set_edicao_controllers(self, edicao: Edicao):
        self.__categoria_controller.set_edicao(edicao)
        self.__profissional_controller.set_edicao(edicao)
        self.__filme_controller.set_edicao(edicao)
        self.__votos_controller.set_edicao(edicao)
        return edicao

    def carregar_dados(self, ano: int):

        data = DataLoader.carregar_dados(ano)
        sucess = data["success"]

        if not sucess:
            return

        categorias_basicas = data["categorias"]
        atores_iniciais = data["atores"]
        diretores_iniciais = data["diretores"]
        filmes_iniciais = data["filmes"]
        membros_iniciais = data["membros"]

        for categoria in categorias_basicas:
            nome, tipo = categoria.split(", ")
            self.__categoria_controller.add_categoria(nome)

        for ator in atores_iniciais:
            nome, filme, ano, nacionalidade = ator.split(", ")
            self.__profissional_controller.add_ator(nome, nacionalidade, str(ano))

        for diretor in diretores_iniciais:
            nome, nascimento = diretor.split(", ")
            self.__profissional_controller.add_diretor(nome, str(nascimento))

        for filme in filmes_iniciais:
            nome, ano, diretor_nome, categoria = filme.split(", ")
            diretor = next((d for d in self.__profissional_controller.diretores() if d.nome == diretor_nome), None)
            if diretor:
                self.__filme_controller.add_filme(nome, int(ano), diretor)

        for nome in membros_iniciais:
            self.__membro_controller.membros.append(Membro(nome, "data", "Brazil"))

        for profissional in self.__profissional_controller.profissionais:
            if isinstance(profissional, Ator):
                self.__categoria_controller.add_nomeacao("20", profissional)

        for filme in self.__filme_controller.filmes:
            self.__categoria_controller.add_nomeacao("23", filme)

    def get_edicao_controller(self, edicao: Edicao):
        self.set_edicao_controllers(edicao)
        return EdicaoController(edicao, self.__membro_controller, self.__categoria_controller,
                                self.__filme_controller, self.__profissional_controller, self.__votos_controller)
