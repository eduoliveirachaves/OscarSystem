from models.categoria import Categoria
from views.categoria_view import CategoriaView


class CategoriaController:
    def __init__(self, categorias: list[Categoria]):
        self.__categorias: list[Categoria] = categorias
        self.__view = CategoriaView()

    @property
    def categorias(self):
        return self.__categorias

    def iniciar(self):
        opcao = self.__view.mostrar_tela()

        while opcao != "0":
            if opcao == "1":
                self.visualizar()
            elif opcao == "2":
                self.cadastrar()
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
                self.__view.visualizar_todas(self.__categorias)
            elif opcao == "2":
                self.__view.visualizar_indicados(self.__categorias)

            opcao = self.__view.visualizar()

    def cadastrar(self):
        nome = self.__view.cadastrar_categoria()
        self.__categorias.append(Categoria(nome))

    def editar(self):
        opcao = self.__view.editar_tela()

        while opcao != "0":
            if opcao == "1":
                self.__view.editar_nome(self.__categorias)
            elif opcao == "2":
                self.__view.remover_indicados(self.__categorias)
            else:
                print("Opção inválida")
            opcao = self.__view.mostrar_tela()

    def add_nomeacao(self, categorias_raw: list, nomeacao):
        # converter string em lista de inteiros
        if isinstance(categorias_raw, str):
            categorias_raw = [int(c.strip()) for c in categorias_raw.split(",") if c.strip().isdigit()]

        for categoria_id in categorias_raw:

            categoria_obj = next(
                (cat_existente for cat_existente in self.__categorias if cat_existente.id == categoria_id),
                None
            )

            if categoria_obj is None:
                print(f"ERRO: Categoria ID '{categoria_id}' não encontrada. Verifique se foi cadastrada.")
                return False
            nomeacao.add_categoria_concorrendo(categoria_obj)
            categoria_obj.add_indicado(nomeacao)

        return True


