from typing import List

from controllers.categoria_controller import CategoriaController
from controllers.profissional_controller import ProfissionalController
from models.filme import Filme
from views.filme_view import FilmeView


class FilmeController:

    def __init__(self, filmes: List[Filme], profissional_controller: ProfissionalController,
                 categoria_controller: CategoriaController):
        self.__filmes: List[Filme] = filmes
        self.__view = FilmeView()
        self.__profissional_controller = profissional_controller
        self.__categoria_controller = categoria_controller

    @property
    def filmes(self):
        return self.__filmes

    def iniciar(self):
        opcao = self.__view.mostrar_tela()

        while opcao != "0":
            if opcao == "1":
                self.visualizar()
            elif opcao == "2":
                self.cadastrar_filme()
            elif opcao == "3":
                # self.__view.editar_filme()
                print("Funcionalidade ainda não implementada.")
            else:
                print("Opção inválida")
            opcao = self.__view.mostrar_tela()

    def visualizar(self):
        self.__view.visualizar_filmes(self.__filmes)

    def cadastrar_filme(self):
        categorias = self.__categoria_controller.categorias
        diretores = self.__profissional_controller.diretores
        input_data = self.__view.cadastrar_filme(diretores, categorias)

        if not input_data:
            print("Cadastro cancelado.")
            return

        nome = input_data["nome"]
        ano = input_data["ano"]
        diretor_info = input_data["diretor"]
        categorias_raw = input_data["categorias_raw"]

        # Verifica se alguma informacao esta faltando ou talvez se a operacao foi cancelada
        if not nome or not ano or not diretor_info or not categorias_raw:
            print("Preencha todos os campos.")
            return

        if diretor_info["id"] == "novo":
            diretor_obj = self.__profissional_controller.add_diretor(diretor_info["nome"],
                                                                     diretor_info["data"])
        else:
            diretor_obj = next(
                (d for d in self.__profissional_controller.diretores() if d.id == diretor_info["id"]), None)
            if not diretor_obj:
                print(f"ERRO: Diretor '{diretor_info['nome']}' não encontrado. Cadastre o profissional primeiro.")
                return

        filme = Filme(nome, ano, diretor_obj)

        self.__filmes.append(filme)

        sucesso = self.__categoria_controller.add_nomeacao(categorias_raw, filme)

        if not sucesso:
            print(
                "Ocorreu algum erro ao adicionar as categorias. "
                "Verifique se as categorias existem e se foram digitadas corretamente.")
            return

        print("\nFilme cadastrado com sucesso!\n")

    def add_filme(self, nome, ano_lancamento, nome_diretor, categorias):
        # Buscar diretor pelo nome
        diretor = next(
            (d for d in self.__profissional_controller.diretores() if d.nome.lower() == nome_diretor.lower()), None)
        if not diretor:
            print(f"Diretor '{nome_diretor}' não encontrado. Cadastre o profissional primeiro.")
            return
