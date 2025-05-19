from controllers.categoria_controller import CategoriaController
from controllers.membro_controller import MembroController
from controllers.profissional_controller import ProfissionalController
from controllers.filme_controller import FilmeController
from controllers.votacao_controller import VotacaoController
from data.data_loader import DataLoader
from models.edicao import Edicao  # Criamos esta classe
from views.admin_view import AdminView
from models.ator import Ator
from models.membro import Membro


class AdminController:
    def __init__(self, carregar_dados: bool, edicao: Edicao, membros_controller: MembroController):
        # Centralize tudo numa edição
        self.__edicao = edicao
        self.__membro_controller = membros_controller
        self.__view = AdminView()

        # Passa a edição para todos os controllers
        self.__categoria_controller = CategoriaController(self.__edicao)
        self.__profissional_controller = ProfissionalController(self.__edicao, self.__categoria_controller)
        self.__filme_controller = FilmeController(self.__edicao, self.__profissional_controller,
                                                  self.__categoria_controller)
        self.__votos_controller = VotacaoController(
            self.__edicao,
            self.__membro_controller,
            self.__categoria_controller,
        )

        if carregar_dados:
            self.carregar_dados(edicao.ano)

    def iniciar(self):
        opcao = self.__view.mostrar_tela()
        while opcao != "0":
            if opcao == "1":
                self.__filme_controller.iniciar()
            elif opcao == "2":
                self.__profissional_controller.iniciar()
            elif opcao == "3":
                self.__categoria_controller.iniciar()
            elif opcao == "4":
                self.__membro_controller.iniciar()
            elif opcao == "5":
                self.__votos_controller.iniciar()
            else:
                print("Opção inválida")
            opcao = self.__view.mostrar_tela()

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
