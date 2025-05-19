from models.membro import Membro
from views.membro_view import MembroView


class MembroController:

    def __init__(self, membros: list[Membro]):
        self.__view = MembroView()
        self.__membros = membros

    @property
    def membros(self):
        return self.__membros


    def iniciar(self):
        opcao = self.__view.mostrar_tela()

        while opcao != "0":
            if opcao == "1":
                self.visualizar()
            elif opcao == "2":
                self.cadastrar()
            elif opcao == "3":
                self.cadastrar()
            else:
                print("Opção inválida")

            opcao = self.__view.mostrar_tela()

    def visualizar(self):
        self.__view.visualizar_membros(self.__membros)

    def cadastrar(self):
        nome, data, nacionalidade = self.__view.tela_cadastro()

        membro = self.add_membro(nome, data, nacionalidade)

        return membro

    def editar(self):
        pass

    def add_membro(self, nome, data, nacionalidade):
        membro = Membro(nome, data, nacionalidade)
        self.__membros.append(membro)
        return membro



