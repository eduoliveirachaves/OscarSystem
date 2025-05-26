from controllers.categoria_controller import CategoriaController
from controllers.membro_controller import MembroController
from models.edicao import Edicao
from models.membro import Membro
from models.voto import Voto
from views.votacao_view import VotacaoView


class VotacaoController:

    def __init__(self, membro_controller: MembroController,
                 categoria_controller: CategoriaController):
        self.__edicao = None
        self.__view = VotacaoView()
        self.__membro_controller = membro_controller
        self.__categoria_controller = categoria_controller

    def set_edicao(self, edicao: Edicao):
        self.__edicao = edicao

    @property
    def votos(self):
        return self.__edicao.votos

    def iniciar(self):
        opcao = self.__view.mostrar_tela()

        while opcao != "0":
            if opcao == "1":
                self.cadastrado()
            elif opcao == "2":
                self.__membro_controller.cadastrar()
            elif opcao == "3":
                self.__view.visualizar_votos_tela(self.__edicao.votos)
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
                res = self.realizar_voto(membro)
                if res:
                    self.add_voto(res)
                    print("Voto realizado com sucesso!")
            else:
                print("Opção inválida")
            opcao = self.__view.menu_membro_tela(membro.nome)

    def autenticar(self, nome, data_nascimento):
        return next((membro for membro in self.__membro_controller.membros if
                     membro.nome == nome and membro.data_nascimento == data_nascimento), None)

    def add_voto(self, voto: Voto):
        self.__edicao.votos.append(voto)

    def visualizar_votos(self, membro):
        votos_do_membro = [voto for voto in self.__edicao.votos if voto.membro == membro]
        self.__view.visualizar_votos_tela(votos_do_membro)

    def realizar_voto(self, membro: Membro):
        categorias = self.categorias_disponiveis(membro)

        categoria = self.escolher_categoria(categorias, membro.nome)

        if not categoria:
            return None

        escolhido = self.escolher_indicado(categoria)

        if not escolhido:
            return None

        voto = Voto(membro, categoria, escolhido)

        return voto

    def categorias_disponiveis(self, membro):
        categorias = self.__edicao.categorias
        return [c for c in categorias if
                c.id not in [v.categoria.id for v in self.__edicao.votos if v.membro == membro]]

    def escolher_categoria(self, categorias, nome_membro):
        opcao, categoria = self.__view.escolher_categoria_tela(categorias, nome_membro), None

        while True:

            if opcao == "0":
                print("Voto cancelado.")
                return None

            if opcao is not None:
                categoria = self.__categoria_controller.get_categoria_by_id(int(opcao))

                if not categoria:
                    print("Categoria não encontrada.")
                    continue

                return categoria

            opcao = self.__view.escolher_categoria_tela(categorias, nome_membro)
        return None

    def escolher_indicado(self, categoria):
        escolhido = self.__view.escolher_indicado_tela(categoria)

        while True:
            if escolhido == "0":
                print("Voto cancelado.")
                return None

            if escolhido is not None:
                escolhido = self.__categoria_controller.get_indicacao_by_id_and_categoria(int(escolhido), categoria)

                if escolhido is None:
                    print("Indicado não encontrado.")
                    continue

                return escolhido
            escolhido = self.__view.escolher_indicado_tela(categoria)
        return None


