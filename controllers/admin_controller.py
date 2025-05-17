from typing import List

from controllers.categoria_controller import CategoriaController
from controllers.profissional_controller import ProfissionalController
from controllers.filme_controller import FilmeController
from models.categoria import Categoria
from views.admin_view import AdminView
from models.ator import Ator


class AdminController:

    def __init__(self):
        atores, categorias = self.carregar_dados()
        self.__profissional_controller = ProfissionalController(atores, [])
        self.__filme_controller = FilmeController([])
        self.__categoria_controller = CategoriaController(categorias)
        self.__admin_view = AdminView()

    def iniciar(self):
        opcao = self.__admin_view.mostrar_tela()
        while opcao != "0":
            if opcao == "1":
                self.__filme_controller.iniciar()
            elif opcao == "2":
                self.__profissional_controller.iniciar()
            elif opcao == "3":
                self.__categoria_controller.iniciar()
            else:
                print("Opção inválida")
            opcao = self.__admin_view.mostrar_tela()
        return

    def carregar_dados(self):
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
            #implementar tipo ( DIRECAO, FILME, ATOR/ATRIZ, TRILHA SONORA ....
            categoria, tipo = categoria.split(", ")
            categorias.append(Categoria(categoria))

        # Lista de indicados a Melhor Ator (2024)
        indicados_ator = [
            "Cillian Murphy",
            "Bradley Cooper",
            "Colman Domingo",
            "Paul Giamatti",
            "Jeffrey Wright"
        ]
        atores = []
        for nome in indicados_ator:
            ator = Ator(nome, "Ingles", "2024")
            atores.append(ator)

        return atores, categorias