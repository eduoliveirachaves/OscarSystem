from controllers.categoria_controller import CategoriaController
from models.ator import Ator
from models.diretor import Diretor
from models.edicao import Edicao
from views.profissional_view import ProfissionalView


class ProfissionalController:

    def __init__(self, categoria_controller: CategoriaController):
        self.__edicao = None
        self.__profissional_view = ProfissionalView()
        self.__categoria_controller = categoria_controller

    def set_edicao(self, edicao: Edicao):
        self.__edicao = edicao

    @property
    def profissionais(self):
        return self.__edicao.profissionais

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

            opcao = self.__profissional_view.mostrar_tela()

    def listagens(self):
        # todos / atores / diretores
        qual_profissional = self.__profissional_view.tela_visualizar()

        while qual_profissional != "0":

            if qual_profissional == "1":
                self.__profissional_view.visualizar_todos(self.__edicao.profissionais)
            elif qual_profissional == "2":
                self.__profissional_view.visualizar_atores(self.atores())
            elif qual_profissional == "3":
                self.__profissional_view.visualizar_diretores(self.diretores())

            qual_profissional = self.__profissional_view.tela_visualizar()

    def cadastros(self):
        while True:
            opcao = self.__profissional_view.tela_cadastro()
            if opcao == "1":
                nome, nacionalidade, data_nascimento = self.__profissional_view.cadastrar_ator()
                self.__edicao.profissionais.append(Ator(nome, nacionalidade, data_nascimento))
                break
            elif opcao == "2":
                nome, data_nascimento = self.__profissional_view.cadastrar_diretor()
                self.__edicao.profissionais.append(Diretor(nome, data_nascimento))
                break
            elif opcao == "0":
                break
            else:
                print("Opção inválida")

    def editar(self):
        pass

    def add_ator(self, nome, nacionalidade, data_nascimento):
        self.__edicao.profissionais.append(Ator(self.__edicao.atores_id, nome, nacionalidade, data_nascimento))

    def add_diretor(self, nome, data_nascimento):
        diretor = Diretor(self.__edicao.diretores_id, nome, data_nascimento)
        self.__edicao.profissionais.append(diretor)
        return diretor

    def atores(self):
        atores = []
        for profissional in self.__edicao.profissionais:
            if isinstance(profissional, Ator):
                atores.append(profissional)

        return atores

    def diretores(self):
        diretores = []
        for profissional in self.__edicao.profissionais:
            if isinstance(profissional, Diretor):
                diretores.append(profissional)

        return diretores
