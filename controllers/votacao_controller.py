from controllers.categoria_controller import CategoriaController
from controllers.membro_controller import MembroController
from models.edicao import Edicao
from models.membro import Membro
from models.voto import Voto
from views.votacao_view import VotacaoView


class VotacaoController:

    def __init__(self, membro_controller: MembroController, categoria_controller: CategoriaController):
        self.__edicao = None
        self.__view = VotacaoView()
        self.__membro_controller = membro_controller
        self.__categoria_controller = categoria_controller

    def set_edicao(self, edicao: Edicao):
        self.__edicao: Edicao = edicao

    @property
    def votos(self):
        return self.get_votos()

    def iniciar(self):
        while (opcao := self.__view.mostrar_tela()) != "0":
            match opcao:
                case "1":
                    self.fluxo_login_membro()
                case "2":
                    votos = self.get_votos()
                    self.__view.visualizar_votos_tela(votos)
                case _:
                    print("Opção inválida")

    def fluxo_login_membro(self):
        nome, data = self.__view.membro_login_tela()
        membro = self.autenticar_membro(nome, data)

        if not membro:
            print("Membro não encontrado.")
            return

        while (opcao := self.__view.menu_membro_tela(membro.nome)) != "0":
            match opcao:
                case "1":
                    votos = self.get_votos_membro(membro)
                    self.__view.visualizar_votos_tela(votos)
                case "2":
                    if self.criar_voto(membro):
                        print("Voto realizado com sucesso!")
                case _:
                    print("Opção inválida")

    def autenticar_membro(self, nome, data_nascimento):
        for membro in self.__membro_controller.membros:
            if membro.nome == nome and membro.data_nascimento == data_nascimento:
                return membro
        return None

    def get_votos_membro(self, membro: Membro):
        votos_do_membro = []

        for categoria in self.__edicao.categorias:
            for indicacao in categoria.indicados:
                for voto in indicacao.votos:
                    if voto.membro == membro:
                        votos_do_membro.append(f"{voto} = Escolha: {indicacao.indicado}")

        return votos_do_membro

    def get_votos(self):
        votos = []

        for categoria in self.__edicao.categorias:
            for indicacao in categoria.indicados:
                for voto in indicacao.votos:
                    votos.append(voto)

        return votos

    def criar_voto(self, membro: Membro):
        categorias_disponiveis = self.get_categorias_disponiveis_para_membro(membro)
        if not categorias_disponiveis:
            print("Nenhuma categoria disponível para votar.")
            return None

        categoria = self.selecionar_categoria(categorias_disponiveis, membro.nome)

        if not categoria:
            return None

        indicado = self.selecionar_indicado(categoria)

        if not indicado:
            return None

        return indicado.add_voto(Voto(membro, categoria))

    def get_categorias_disponiveis_para_membro(self, membro: Membro):
        return [
            c for c in self.__edicao.categorias
            if not any(voto.membro == membro for indicacao in c.indicados for voto in indicacao.votos)
        ]

    def selecionar_categoria(self, categorias, nome_membro):
        while True:
            opcao = self.__view.escolher_categoria_tela(categorias, nome_membro)
            if opcao == "0":
                print("Voto cancelado.")
                return None

            categoria = self.__categoria_controller.get_categoria_by_id(int(opcao))
            if categoria:
                return categoria

            print("Categoria não encontrada.")

    def selecionar_indicado(self, categoria):
        while True:
            opcao = self.__view.escolher_indicado_tela(categoria)
            if opcao == "0":
                print("Voto cancelado.")
                return None

            indicado = self.__categoria_controller.get_indicacao_by_id_and_categoria(int(opcao), categoria)
            if indicado:
                return indicado

            print("Indicado não encontrado.")
