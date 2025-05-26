from controllers.edicoes_controller import EdicoesController
from models.categoria import Categoria
from models.edicao import Edicao
from views.relatorios_view import RelatoriosView


class RelatoriosController:
    def __init__(self, edicoes_controller: EdicoesController):
        self.__edicoes_controller = edicoes_controller
        self.__view = RelatoriosView()

    def iniciar(self):
        opcao = self.__view.mostrar_tela()

        while opcao != "0":
            # indicacoes por ano e categoria
            if opcao == "1":
                res = self.indicacoes_ano_categoria()

                if res is not None:
                    categoria, ano = res["categoria"], res["ano"]
                    self.__view.visualizar_indicados(categoria, ano)

            # votos por ano e categoria
            elif opcao == "2":
                self.votos_ano_categoria()

            # vencedores por ano e edicao
            elif opcao == "3":
                self.vencedores_por_ano_edicao()

            # vencedores por nacionalidade / todas as edições? / por edicao?
            elif opcao == "4":
                self.vencedores_por_nacionalidade()

            # top 3 filmes mais premiados / da historia? / por edicao?
            elif opcao == "5":
                self.top_filmes_mais_premiados()

            else:
                print("Opção inválida.")

            opcao = self.__view.mostrar_tela()

    def indicacoes_ano_categoria(self):
        edicao = self.get_edicao()

        if edicao is None:
            return None

        categoria = self.get_categoria(edicao)

        if categoria is None:
            return None

        return {"ano": edicao.ano, "categoria": categoria}

    def votos_ano_categoria(self):
        edicao = self.get_edicao()
        if edicao is None:
            return None

        ver_edicao = self.ver_edicao_ou_categoria()

        if ver_edicao is None:
            return None

        categoria = None
        if ver_edicao:
            categoria = edicao.categorias
        else:
            categoria = self.get_categoria(edicao)
            if categoria is None:
                return None

        return {"ano": edicao.ano, "categoria": categoria}

    def vencedores_por_ano_edicao(self):
        edicao = self.get_edicao()

        vencedores = edicao.get_vencedores()
        self.__view.mostrar_vencedores(edicao.ano, vencedores)

    def vencedores_por_nacionalidade(self):
        nacionalidade = self.__view.solicitar_nacionalidade()

        for edicao in self.__edicoes_controller.edicoes:
            vencedores = edicao.get_vencedores()
            vencedores_nacionalidade = [v for v in vencedores if v.vencedor.nacionalidade == nacionalidade]
            self.__view.mostrar_vencedores_nacionalidade(edicao.ano, vencedores_nacionalidade, nacionalidade=nacionalidade)

    def top_filmes_mais_premiados(self):
        edicao = self.get_edicao()
        filmes_premiados = edicao.get_top_filmes_premiados()
        self.__view.mostrar_top_filmes(filmes_premiados)

    # helper
    def get_edicao(self):
        edicao = self.__edicoes_controller.escolher_edicao()

        if edicao is None:
            print("Edição não encontrada.")
            return None

        return edicao

    # helper
    def get_categoria(self, edicao: Edicao):
        edicao_controller = self.__edicoes_controller.get_edicao_controller(edicao)

        categorias = edicao.categorias

        if not categorias:
            print("Edição não possui categorias.")
            return None

        categoria_id = self.__view.categoria_desejada_tela(categorias)

        categoria: Categoria = edicao_controller.get_categoria_by_id(categoria_id)

        if not categoria:
            print("Categoria não encontrada.")
            return None

        return categoria

    def ver_edicao_ou_categoria(self):
        opcao = self.__view.edicao_ou_categoria_tela()

        if opcao == "0":
            return None

        return opcao == "1"  # True para ver todas as categorias, False para uma específica
