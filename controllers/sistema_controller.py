from controllers.admin_controller import AdminController
from controllers.user_controller import UserController
from controllers.membro_controller import MembroController
from controllers.votacao_controller import VotacaoController
from views import sistema_view
from views.sistema_view import SistemaView


class SistemaController:
    def __init__(self, carregar_dados: bool=False):
        self.__sistema_view = SistemaView()
        # usado pra cadastrar e armazenar os dados
        self.__admin_controller = AdminController(carregar_dados)
        # usado pra exibir os dados publicos
        # Sistema de votacao em si com a area do membro da academia onde ele pode cadastrar
        # logar, navegar por categorias, ver detalhes etc
        # preciso passar admin_controller pq os dados estao concentrados la (tirando membro controller que possui os dados da votacao)
        self.__user_controller = UserController(self.__admin_controller)
        self.__votacao_controller = VotacaoController([])


    def iniciar(self):
        while True:
            opcao = self.__sistema_view.mostrar_tela()
            if opcao == "1":
                # ver os votos contagem/categorias {ver tambem os filmes listados?} (opcao publica) | LISTAR |
                # votos controller
               self.__user_controller.iniciar()
            elif opcao == "2":
                # area para membros da academia cadastros/editar/listar/ etc...
                self.__admin_controller.iniciar()

            elif opcao == "3":
                self.__votacao_controller.iniciar()
            elif opcao == "0":
                return
            else:
                print("Opção inválida")










