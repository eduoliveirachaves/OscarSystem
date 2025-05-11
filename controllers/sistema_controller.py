from controllers.admin_controller import AdminController
from views import sistema_view
from views.sistema_view import SistemaView


class SistemaController:
    def __init__(self):
        self.__sistema_view = SistemaView()
        self.__admin_controller = AdminController()


    def iniciar(self):
        while True:
            opcao = self.__sistema_view.mostrar_tela()
            if opcao == "1":
                # ver os votos contagem/categorias {ver tambem os filmes listados?} (opcao publica) | LISTAR |
                print("Visualizando votos....")
                # votos controller
            elif opcao == "2":
                # area para membros da academia cadastrar - se / entrar / votar / .....
                print("Ainda não implementado")
            elif opcao == "3":
                # area para admin ( nao precisa autenticar - se )
                # cadastro de filmes / listagem / categorias / tudo
                self.__admin_controller.iniciar()
            elif opcao == "0":
                return
            else:
                print("Opção inválida")







