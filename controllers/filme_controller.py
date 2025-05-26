from controllers.categoria_controller import CategoriaController
from controllers.profissional_controller import ProfissionalController
from models.diretor import Diretor
from models.edicao import Edicao
from models.filme import Filme
from views.filme_view import FilmeView


class FilmeController:

    def __init__(self, profissional_controller: ProfissionalController):
        self.__edicao = None
        self.__view = FilmeView()
        self.__profissional_controller = profissional_controller

    @property
    def filmes(self):
        return self.__edicao.filmes

    def set_edicao(self, edicao: Edicao):
        self.__edicao = edicao

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
        self.__view.visualizar_filmes(self.__edicao.filmes)

    def cadastrar_filme(self):
        diretores = self.__profissional_controller.diretores()
        input_data = self.__view.cadastrar_filme(diretores)

        if not input_data:
            print("Cadastro cancelado.")
            return

        nome = input_data["nome"]
        diretor_info = input_data["diretor"]

        # Verifica se alguma informacao esta faltando ou talvez se a operacao foi cancelada
        if not nome or not diretor_info:
            print("Preencha todos os campos.")
            return

        if diretor_info["id"] == "novo":
            diretor_obj = self.__profissional_controller.add_diretor(diretor_info["nome"],
                                                                     diretor_info["data"])
        else:
            diretor_obj = next(
                (d for d in diretores if str(d.id) == str(diretor_info["id"])), None)
            if not diretor_obj:
                print(f"ERRO: Diretor '{diretor_info['nome']}' não encontrado. Cadastre o profissional primeiro.")
                return

        filme = self.add_filme(nome, diretor_obj)

        print("\nFilme cadastrado com sucesso!\n")

    def add_filme(self, nome: str, diretor: Diretor):
        filme = Filme(self.__edicao.filmes_id, nome, self.__edicao.ano - 1, diretor)
        self.__edicao.filmes.append(filme)
        return filme
