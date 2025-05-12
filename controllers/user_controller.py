from controllers.admin_controller import AdminController
from views.user_view import UserView


class UserController:
    def __init__(self, admin_controller: AdminController):
        ## get data
        self.__admin_controller = admin_controller
        self.__user_view = UserView()

    # IDEIA: depois de exibir (so o nome) eu posso perguntar se deseja detalhes sobre alguma
    # como indicados naquela categoria ou detalhes sobre o ator etc...

    # funcao basica pra mostrar as informacoes e aguardar o input do usuario para entao exibir determinada informacao
    def iniciar(self):
        opcao = self.__user_view.mostrar_tela()
        while opcao != "0":
            if opcao == "1":
                self.__user_view.visualizar_filmes(self.__admin_controller.filmes)
            elif opcao == "2":
                self.__user_view.visualizar_categorias(self.__admin_controller.categorias)
            elif opcao == "3":
                self.__user_view.visualizar_atores(self.__admin_controller.atores)
            elif opcao == "4":
                self.__user_view.visualizar_diretores(self.__admin_controller.diretores)
            elif opcao == "5":
                self.__user_view.visualizar_membros(self.__admin_controller.votantes)
            else:
                print("Opção inválida")
            opcao = self.__user_view.mostrar_tela()
        return


