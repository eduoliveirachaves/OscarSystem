from typing import List

from controllers.categoria_controller import CategoriaController
from controllers.filme_controller import FilmeController
from controllers.membro_controller import MembroController
from controllers.profissional_controller import ProfissionalController
from models.membro import Membro
from models.voto import Voto
from views.votacao_view import VotacaoView


class VotacaoController:

    def __init__(self, votos: List[Voto], membro_controller: MembroController,
                 categoria_controller: CategoriaController, filme_controller: FilmeController,
                 profissional_controller: ProfissionalController):
        self.__votos = votos
        self.__view = VotacaoView()
        self.__membro_controller = membro_controller
        self.__categoria_controller = categoria_controller
        self.__filme_controller = filme_controller
        self.__profissional_controller = profissional_controller

    @property
    def votos(self):
        return self.__votos

    def iniciar(self):
        opcao = self.__view.mostrar_tela()

        while opcao != "0":
            if opcao == "1":
                self.cadastrado()
            elif opcao == "2":
                self.__membro_controller.cadastrar()
            elif opcao == "3":
                self.__view.visualizar_votos_tela(self.__votos)
            else:
                print("Opção inválida")
            opcao = self.__view.mostrar_tela()

    def cadastrado(self):
        nome, data = self.__view.membro_login_tela()
        membro = self.autenticar(nome, data)

        if not membro:
            print("Membro não encontrado.")
            return

        opcao = self.__view.menu_membro_tela(membro.nome)

        while opcao != "0":
            if opcao == "1":
                self.visualizar_votos(membro)
            elif opcao == "2":
                self.realizar_voto(membro)
            else:
                print("Opção inválida")
            opcao = self.__view.menu_membro_tela(membro.nome)

    def autenticar(self, nome, data_nascimento):
        return next((membro for membro in self.__membro_controller.membros if
                     membro.nome == nome and membro.data_nascimento == data_nascimento), None)

    def add_voto(self, voto: Voto):
        self.__votos.append(voto)

    def visualizar_votos(self, membro):
        votos_do_membro = [voto for voto in self.__votos if voto.membro == membro]
        self.__view.visualizar_votos_tela(votos_do_membro)

    def realizar_voto(self, membro: Membro):
        categoria = self.__view.escolher_categoria_tela(self.__categoria_controller.categorias, membro.nome)

        categoria = self.__categoria_controller.get_categoria_by_id(int(categoria))

        if not categoria:
            print("Categoria não encontrada.")
            return

        escolhido = self.__view.escolher_indicado_tela(categoria)

        escolhido = self.__categoria_controller.get_indicacao_by_id_and_categoria(int(escolhido), categoria)

        if not escolhido:
            print("Indicado não encontrado.")

        self.add_voto(Voto(membro, categoria, escolhido))
