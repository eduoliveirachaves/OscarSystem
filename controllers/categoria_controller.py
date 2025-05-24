from typing import List

from models.categoria import Categoria
from models.edicao import Edicao
from models.indicacao import Indicacao
from models.indicavel import Indicavel
from views.categoria_view import CategoriaView


class CategoriaController:
    def __init__(self, edicao: Edicao):
        self.__edicao = edicao
        self.__view = CategoriaView()

    @property
    def categorias(self):
        return self.__edicao.categorias

    def iniciar(self):
        opcao = self.__view.mostrar_tela()

        while opcao != "0":
            if opcao == "1":
                self.visualizar()
            elif opcao == "2":
                nome = self.__view.cadastrar_categoria()
                self.add_categoria(nome)
            elif opcao == "3":
                self.editar()
                continue
            else:
                print("Opção inválida")
            opcao = self.__view.mostrar_tela()

    def visualizar(self):
        opcao = self.__view.visualizar()

        while opcao != "0":
            if opcao == "1":
                self.__view.visualizar_todas(self.__edicao.categorias)
            elif opcao == "2":
                self.__view.visualizar_indicados(self.__edicao.categorias)

            opcao = self.__view.visualizar()

    def add_categoria(self, nome):
        cat = Categoria(self.__edicao.categorias_id, nome)
        self.__edicao.categorias.append(cat)
        return cat

    def editar(self):
        opcao = self.__view.editar_tela()

        while opcao != "0":
            if opcao == "1":
                self.__view.editar_nome(self.__edicao.categorias)
            elif opcao == "2":
                self.__view.remover_indicados(self.__edicao.categorias)
            else:
                print("Opção inválida")
            opcao = self.__view.mostrar_tela()

    def add_nomeacao(self, categoria_str: str, nomeacao: Indicavel):
        categorias = self.get_categorias_by_string(categoria_str)

        # revisar
        if not categorias:
            return False

        for categoria in categorias:
            # add a categoria ao indicado (Ator, Diretor, Filme) para que ele saiba suas categorias
            nomeacao.add_categoria(categoria)
            # cria um objeto indicacao - serve pra que cada indicacao/categoria possa rastrear seu voto
            indicado = Indicacao(nomeacao)
            categoria.add_indicado(indicado)

        return True

    def get_categoria_by_id(self, categoria_id: int):
        return next((cat for cat in self.__edicao.categorias if cat.id == categoria_id), None)

    def get_indicacao_by_id_and_categoria(self, nomeacao_id: int, categoria: Categoria):
        return next((nomeacao for nomeacao in categoria.indicados if nomeacao.id == nomeacao_id), None)

    def get_categorias_by_string(self, categoria_str: str):
        categorias: List[Categoria] = []  # armazena os objetos

        # converter string em lista de inteiros
        if isinstance(categoria_str, str):
            categoria_str = [int(c.strip()) for c in categoria_str.split(",") if c.strip().isdigit()]

        for categoria_id in categoria_str:
            categoria = self.get_categoria_by_id(categoria_id)

            if categoria is None:
                print(f"ERRO: Categoria ID '{categoria_id}' não encontrada. Verifique se foi cadastrada.")
                return []

            categorias.append(categoria)

        return categorias



