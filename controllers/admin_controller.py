from typing import List

from controllers.categoria_controller import CategoriaController
from controllers.membro_controller import MembroController
from controllers.profissional_controller import ProfissionalController
from controllers.filme_controller import FilmeController
from models.categoria import Categoria
from models.diretor import Diretor
from models.filme import Filme
from views.admin_view import AdminView
from models.ator import Ator


class AdminController:

    def __init__(self, carregar_dados: bool = False):
        filmes, categorias, atores, diretores, membros\
            = self.carregar_dados(carregar_dados)
        self.__categoria_controller = CategoriaController(categorias)
        self.__profissional_controller = ProfissionalController(atores, diretores, self.__categoria_controller)
        self.__filme_controller = FilmeController(filmes, self.__profissional_controller, self.__categoria_controller)
        self.__membro_controller = MembroController()
        self.__admin_view = AdminView()
        self.carregar_nomeacoes(filmes, atores)


    def iniciar(self):
        opcao = self.__admin_view.mostrar_tela()
        while opcao != "0":
            if opcao == "1":
                self.__filme_controller.iniciar()
            elif opcao == "2":
                self.__profissional_controller.iniciar()
            elif opcao == "3":
                self.__categoria_controller.iniciar()
            elif opcao == "4":
                self.__membro_controller.iniciar()
            else:
                print("Opção inválida")
            opcao = self.__admin_view.mostrar_tela()
        return

    # adiciona alguns dados ao iniciar o sistema para fins de teste e visualizacao
    def carregar_dados(self, carregar_dados: bool = False):
        if not carregar_dados:
            return [], [], [], [], []

        categorias_basicas = [
            "Ator Coadjuvante, Ator",
            "Animação, Filme",
            "Curta de animação, Filme",
            "Figurino, Filme",
            "Roteiro Original, Filme",
            "Roteiro Adaptado, Filme",
            "Maquiagem e cabelo, Filme",
            "Edição, Filme",
            "Atriz Coadjuvante, Ator",
            "Direção de Arte, Filme",
            "Canção Original, Filme",
            "Curta documentário, Filme",
            "Documentário, Filme",
            "Som, Filme",
            "Efeitos Visuais, Filme",
            "Curta Live Action, Filme",
            "Fotografia, Filme",
            "Filme Internacional, Filme",
            "Trilha Original, Filme",
            "Ator, Ator",
            "Direção, Diretor",
            "Atriz, Ator",
            "Filme, Filme"
        ]

        categorias = []

        for categoria in categorias_basicas:
            # implementar tipo ( DIRECAO, FILME, ATOR/ATRIZ, TRILHA SONORA ....
            categoria, tipo = categoria.split(", ")
            categorias.append(Categoria(categoria))

        # Lista de indicados a Melhor Ator (2024) com nome, ano de nascimento e nacionalidade

        atores_iniciais = [
            # nome, filme, ano_nascimento, nacionalidade
            "Cillian Murphy, Oppenheimer, 1976, Irlandês",
            "Bradley Cooper, Maestro, 1975, Americano",
            "Colman Domingo, Rustin, 1969, Americano",
            "Paul Giamatti, The Holdovers, 1967, Americano",
            "Jeffrey Wright, American Fiction, 1965, Americano",
            "Leonardo DiCaprio, Killers of the Flower Moon, 1974, Americano",
            "Barry Keoghan, Saltburn, 1992, Irlandês",
            "Andrew Scott, All of Us Strangers, 1976, Irlandês",
            "Teo Yoo, Past Lives, 1981, Sul-coreano",
            "Adam Driver, Ferrari, 1983, Americano"
        ]
        
        atores = []
        for s in atores_iniciais:
            nome, filme, ano, nacionalidade = s.split(", ")
            ator = Ator(nome, nacionalidade, str(ano))
            atores.append(ator)

        diretores = []
        
        diretores_iniciais = [
            "Christopher Nolan, 1970",
            "Bradley Cooper, 1975",
            "George C. Wolfe, 1954",
            "Alexander Payne, 1961",
            "Cord Jefferson, 1981",
            "Martin Scorsese, 1942",
            "Emerald Fennell, 1985",
            "Andrew Haigh, 1973",
            "Celine Song, 1988",
            "Michael Mann, 1943"
        ]

        for diretor in diretores_iniciais:
            nome, data_nascimento = diretor.split(", ")
            diretor = Diretor(nome, data_nascimento)
            diretores.append(diretor)
        
        filmes = []
        
        filmes_iniciais = [
            "Oppenheimer, 2023, Christopher Nolan, 23",
            "Maestro, 2023, Bradley Cooper, 23",
            "Rustin, 2023, George C. Wolfe, 23",
            "The Holdovers, 2023, Alexander Payne, 23",
            "American Fiction, 2023, Cord Jefferson, 23",
            "Killers of the Flower Moon, 2023, Martin Scorsese, 23",
            "Saltburn, 2023, Emerald Fennell, 23",
            "All of Us Strangers, 2023, Andrew Haigh, 23",
            "Past Lives, 2023, Celine Song, 23",
            "Ferrari, 2023, Michael Mann, 23"
        ]

        for filme in filmes_iniciais:
            nome, ano, diretor, categoria = filme.split(", ")
            for d in diretores:
                if d.nome == diretor:
                    diretor = d
                    break
            filme = Filme(nome, int(ano), diretor)
            filmes.append(filme)

        membros = []

        return filmes, categorias, atores, diretores, membros

    def carregar_nomeacoes(self, filmes, atores, carregar_dados: bool = False):
        if not carregar_dados:
            return
        for ator in atores:
            self.__categoria_controller.add_nomeacao("20", ator)

        for filme in filmes:
            self.__categoria_controller.add_nomeacao("23", filme)
