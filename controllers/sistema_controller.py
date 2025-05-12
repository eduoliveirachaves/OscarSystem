from controllers.admin_controller import AdminController
from controllers.user_controller import UserController
from views import sistema_view
from views.sistema_view import SistemaView


class SistemaController:
    def __init__(self):
        self.__sistema_view = SistemaView()
        # usado pra cadastrar e armazenar os dados
        self.__admin_controller = AdminController()
        # usado pra exibir os dados publicos
        # preciso passar admin_controller pq os dados estao concentrados la
        self.__user_controller = UserController(self.__admin_controller)


    def iniciar(self):
        while True:
            opcao = self.__sistema_view.mostrar_tela()
            if opcao == "1":
                # ver os votos contagem/categorias {ver tambem os filmes listados?} (opcao publica) | LISTAR |
                # votos controller
               self.__user_controller.iniciar()
            elif opcao == "2":
                # area para membros da academia cadastrar - se / entrar / votar / .....
                print("Ainda não implementado")
            elif opcao == "3":
                # area para admin ( nao precisa autenticar - se )
                # DUVIDA: se eu quiser criar uma autenticacao eu posso?
                # CADASTRO / TODAS AS LISTAS
                self.__admin_controller.iniciar()
            elif opcao == "0":
                return
            else:
                print("Opção inválida")







