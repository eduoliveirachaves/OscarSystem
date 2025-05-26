from typing import List

from models.categoria import Categoria
from models.edicao import Edicao
from models.indicacao import Indicacao
from models.indicavel import Indicavel
from views.categoria_view import CategoriaView


class CategoriaController:
    def __init__(self, filmes_controller, profissionais_controller):
        self.__edicao = None
        self.__view = CategoriaView()
        self.__filmes_controller = filmes_controller
        self.__profissionais_controller = profissionais_controller

    def set_edicao(self, edicao: Edicao):
        self.__edicao = edicao

    @property
    def categorias(self):
        return self.__edicao.categorias

    def iniciar(self):
        opcao = self.__view.mostrar_tela()

        while opcao != "0":
            if opcao == "1":
                self.visualizar()
            elif opcao == "2":
                nome, tipo = self.__view.cadastrar_categoria()
                self.add_categoria(nome, tipo)
            elif opcao == "3":
                self.editar()
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

    def add_categoria(self, nome, tipo):
        cat = Categoria(self.__edicao.categorias_id, nome, tipo)
        self.__edicao.categorias.append(cat)
        return cat

    def editar(self):
        opcao = self.__view.editar_tela()

        while opcao != "0":
            if opcao == "1":
                self.adicionar_indicados()
            elif opcao == "2":
                self.remover_indicados()
            elif opcao == "3":
                self.editar_categoria()
            else:
                print("Opção inválida")
            opcao = self.__view.editar_tela()

    def add_nomeacao(self, categorias, nomeacao: Indicavel):
        categorias = self.get_categorias_by_string(categorias)

        # revisar
        if not categorias:
            return False

        for categoria in categorias:
            # cria um objeto indicacao - serve pra que cada indicacao/categoria possa rastrear seu voto
            indicado = Indicacao(nomeacao)
            categoria.add_indicado(indicado)

        return True

    def adicionar_indicados(self):
        categoria_str = self.__view.selecionar_categoria(self.__edicao.categorias)
        categoria = self.get_categoria_by_id(int(categoria_str))

        if not categoria:
            print("Nenhuma categoria selecionada.")
            return

        tipo = categoria.tipo_indicados
        todos_indicaveis = None
        if tipo == "Filme":
            todos_indicaveis = self.__filmes_controller.filmes
        elif tipo == "Diretor":
            todos_indicaveis = self.__profissionais_controller.diretores()
        else :
            todos_indicaveis = self.__profissionais_controller.atores()

        lista_indicaveis = [indicavel for indicavel in todos_indicaveis
                            if indicavel.id not in [i.indicado.id for i in categoria.indicados]]

        if not lista_indicaveis:
            print("Todos os possíveis indicados já foram adicionados a essa categoria.")
            return

        nomeacao_id_str = self.__view.selecionar_nomeacao_tela(lista_indicaveis)
        if not nomeacao_id_str:
            print("Nenhuma nomeação selecionada.")
            return

        try:
            nomeacao_id = int(nomeacao_id_str)
        except ValueError:
            print("ID inválido.")
            return

        #objeto pelo ID
        nomeacao = next((i for i in lista_indicaveis if i.id == nomeacao_id), None)

        if not nomeacao:
            print("Nomeação não encontrada.")
            return

        if not self.add_nomeacao(categoria_str, nomeacao):
            print("Erro ao adicionar nomeação. Verifique se as categorias foram cadastradas corretamente.")

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

    def get_votos_por_categoria(self, categoria: Categoria):
        votos = {}
        for indicado in categoria.indicados:
            votos[indicado.indicado.nome] = indicado.votos
        return votos

    def get_votos(self):
        votos = {}
        for categoria in self.__edicao.categorias:
            votos[categoria.nome] = self.get_votos_por_categoria(categoria)
        return votos

    # basicamente retorna todas as categorias para uma determinada classe como ator, diretor, filme
    def get_categoria_by_tipo(self, tipo: str):
        categorias_por_tipo = []
        for categoria in self.__edicao.categorias:
            if categoria.tipo_indicados == tipo:
                categorias_por_tipo.append(categoria)
        return categorias_por_tipo

    def get_categoria_by_id(self, categoria_id: int):
        return next((cat for cat in self.__edicao.categorias if cat.id == categoria_id), None)

    def get_indicacao_by_id_and_categoria(self, nomeacao_id: int, categoria: Categoria):
        return next((nomeacao for nomeacao in categoria.indicados if nomeacao.indicado.id == nomeacao_id), None)

    def remover_indicados(self):
        pass

    def editar_categoria(self):
        pass
