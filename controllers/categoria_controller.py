from models.categoria import Categoria
from views.categoria_view import CategoriaView


class CategoriaController:

    def __init__(self, categorias: list[Categoria]):
        self.__categorias: list[Categoria] = categorias
        self.__view = CategoriaView()

    def iniciar(self):
        opcao = self.__view.mostrar_tela()

        while opcao != "0":
            if opcao == "1":
                self.visualizar()
            elif opcao == "2":
                nome = self.__view.cadastrar_categoria()
                self.__categorias.append(Categoria(nome, ""))
            elif opcao == "3":
                # self.__view.editar_categoria()
                continue
            else:
                print("Opção inválida")
            opcao = self.__view.mostrar_tela()


    def visualizar(self):
        opcao = self.__view.visualizar()

        while opcao != "0":
            if opcao == "1":
                self.__view.visualizar_todas(self.__categorias)
            elif opcao == "2":
                self.__view.visualizar_indicados(self.__categorias)
            elif opcao == "3":
                self.__view.visualizar_votos(self.__categorias)