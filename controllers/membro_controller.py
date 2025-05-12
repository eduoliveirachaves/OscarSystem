from views.membro_view import MembroView
from models.votante import Votante


class MembroController:
    def __init__(self, admin_controller):
        self.__votante_view = MembroView()
        self.__admin_controller = admin_controller
        self.__membros = []

    @property
    def membros(self):
        if len(self.__membros) == 0:
            return ["Nenhum membro cadastrado"]
        return self.__membros

    def iniciar(self):
        opcao = self.__votante_view.mostrar_tela()

        while opcao != "0":
            if opcao == "1":
                #exibir os membros cadastrados? e pedir a data?
                nome, senha = self.__votante_view.tela_login()
            elif opcao == "2":
                nome, data_nascimento, nacionalidade = self.__votante_view.tela_cadastro()
                self.__admin_controller.votantes.append(Votante(nome, data_nascimento, nacionalidade))


            else:
                print("Opção inválida")

            opcao = self.__votante_view.mostrar_tela()
