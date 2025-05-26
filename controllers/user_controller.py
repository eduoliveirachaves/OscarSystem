from typing import List

from controllers.edicoes_controller import EdicoesController
from models.categoria import Categoria
from models.edicao import Edicao
from views.user_view import UserView


class UserController:
    def __init__(self):
        self.__edicoes_controller = None
        self.__view = UserView()

    def iniciar(self, edicoes_controller: EdicoesController):
        self.__edicoes_controller = edicoes_controller
        opcao = self.__view.mostrar_tela()
        edicoes = self.__edicoes_controller.edicoes

        while opcao != "0":
            if opcao == "1":
                self.relatorios_gerais(edicoes)
            elif opcao == "2":
                pass
                # self.selecionar_edicao(edicoes)
            else:
                print("Opção inválida")
            opcao = self.__view.mostrar_tela()

    def relatorios_gerais(self, edicoes: List[Edicao]):
        opcao = self.__view.menu_relatorios_gerais()

        while opcao != "0":
            # filtrar por ano e categoria
            if opcao == "1":
                res = self.filtro_ano_categoria(edicoes)

                if res:
                    categoria, ano = res["categoria"], res["ano"]
                    self.__view.visualizar_indicados(categoria, ano)


            # filtrar
            elif opcao == "2":
                pass
                # ano = self.__view.solicitar_ano()
                # edicao = self.__edicoes_controller.get_edicao_by_ano(ano)
                # if edicao:
                #     relatorio = edicao.get_votos_por_categoria()
                #     self.__view.mostrar_votos_por_categoria(relatorio)
                # else:
                #     print("Edição não encontrada.")

            elif opcao == "3":
                pass
                # for edicao in edicoes:
                #     vencedores = edicao.get_vencedores()
                #     self.__view.mostrar_vencedores(edicao.ano, vencedores)

            elif opcao == "4":
                pass
                # nacionalidade = self.__view.solicitar_nacionalidade()
                # for edicao in edicoes:
                #     vencedores = edicao.get_vencedores_por_nacionalidade(nacionalidade)
                #     self.__view.mostrar_vencedores(edicao.ano, vencedores)

            elif opcao == "5":
                pass
                # filmes_premiados = self.__edicoes_controller.get_top_filmes_mais_premiados()
                # self.__view.mostrar_top_filmes(filmes_premiados)

            else:
                print("Opção inválida.")

            opcao = self.__view.menu_relatorios_gerais()

    def filtro_ano_categoria(self, edicoes_disponiveis: List[Edicao]):
        ano = self.__view.ano_desejado_tela(edicoes_disponiveis)

        edicao = self.__edicoes_controller.get_edicao_by_ano(ano)

        if not edicao:
            print("Edição não encontrada.")
            return None

        categorias = edicao.categorias

        if not categorias:
            print("Edição não possui categorias.")
            return None

        categoria_id = self.__view.categoria_desejada_tela(categorias)

        categoria: Categoria = edicao.categoria_controller.get_categoria_by_id(categoria_id)

        if not categoria:
            print("Categoria não encontrada.")
            return None

        return {"ano": ano, "categoria": categoria}
