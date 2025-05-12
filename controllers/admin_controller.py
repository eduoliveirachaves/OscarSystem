from models.categoria import Categoria
from models.filme import Filme
from views.admin_view import AdminView
from models.ator import Pessoa, Ator


class AdminController:

    def __init__(self):
        self.__admin_view = AdminView()
        # usar runtime memory por agora
        self.__atores = []
        self.__filmes = []
        self.__diretores = []
        self.__categorias = []
        self.carregar_dados()

    @property
    def filmes(self):
        if len(self.__filmes) == 0:
            return ["Nenhum filme cadastrado"]
        return self.__filmes

    @property
    def categorias(self):
        if len(self.__categorias) == 0:
            return ["Nenhuma categoria cadastrada"]
        return self.__categorias

    @property
    def atores(self):
        if len(self.__atores) == 0:
            return ["Nenhum ator cadastrado"]
        return self.__atores

    @property
    def diretores(self):
        if len(self.__diretores) == 0:
            return ["Nenhum diretor cadastrado"]
        return self.__diretores

    def iniciar(self):
        opcao = self.__admin_view.mostrar_tela()
        while opcao != "0":
            if opcao == "1":
                self.cadastrar_filme()
            elif opcao == "2":
                self.cadastrar_ator()
            elif opcao == "3":
                self.cadastrar_diretor()
            elif opcao == "4":
                self.cadastrar_categoria()
            else:
                print("Opção inválida")
            opcao = self.__admin_view.mostrar_tela()
        return

    def cadastrar_ator(self):
        # metodo igual == self.__atores.append(self.__admin_view.castrar_ator())
        # mas achei mais legivel como esta
        nome, nacionalidade, data_nascimento = self.__admin_view.cadastrar_ator()
        ator = Ator(nome, nacionalidade, data_nascimento)
        self.__atores.append(ator)

    def cadastrar_filme(self):
        nome, ano_lancamento, diretor, categorias_concorrendo = self.__admin_view.cadastrar_filme()
        categorias_concorrendo = categorias_concorrendo.split(",")
        filme = Filme(nome, ano_lancamento, diretor)
        filme.add_categoria_concorrendo(categorias_concorrendo)
        self.__filmes.append(filme)

    def cadastrar_diretor(self):
        pass

    def cadastrar_categoria(self):
        self.__categorias.append(self.__admin_view.cadastrar_categoria())

    def add_indicado_na_categoria(self):
        pass

    def carregar_dados(self):
        categorias_basicas = [
            "Ator Coadjuvante",
            "Animação",
            "Curta de animação",
            "Figurino",
            "Roteiro Original",
            "Roteiro Adaptado",
            "Maquiagem e cabelo",
            "Edição",
            "Atriz Coadjuvante",
            "Direção de Arte",
            "Canção Original",
            "Curta documentário",
            "Documentário",
            "Som",
            "Efeitos Visuais",
            "Curta Live Action",
            "Fotografia",
            "Filme Internacional",
            "Trilha Original.",
            "Ator",
            "Direção",
            "Atriz",
            "Filme"
        ]

        i = 1
        for categoria in categorias_basicas:
            self.__categorias.append(Categoria(i, categoria))
            i += 1

