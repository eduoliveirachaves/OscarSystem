from views.membro_view import MembroView
from models.membro import Membro


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

    # refatorar - separar as etapas em novas funcoes
    def iniciar(self):
        opcao = self.__votante_view.mostrar_tela()

        while opcao != "0":
            if opcao == "1":
                # exibir os membros cadastrados? e pedir somente a data?
                nome, senha = self.__votante_view.tela_login()

                if nome in self.__admin_controller.votantes:
                    if senha == self.__admin_controller.votantes[nome].data_nascimento:
                        print("\nLogin efetuado com sucesso\n")
                        opcao = self.__votante_view.tela_membro(self.__admin_controller.votantes[nome])

                        while opcao != "0":
                            if opcao == "1":
                                caself.__votante_view.tela_votar(self.__admin_controller.votantes[nome],
                                                               self.__admin_controller.categorias)
                            elif opcao == "2":
                                self.__votante_view.tela_votos_realizados(self.__admin_controller.votantes[nome])
                            else:
                                print("Opção inválida")
                            opcao = self.__votante_view.tela_membro(self.__admin_controller.votantes[nome])

                    else:
                        print("Credencial incorreta")
            elif opcao == "2":
                nome, data_nascimento, nacionalidade = self.__votante_view.tela_cadastro()
                ID = len(self.__admin_controller.votantes) + 1  # usar len temporiariamente so pra fins de teste
                self.__admin_controller.votantes.append(Membro(ID, nome, data_nascimento, nacionalidade))
            else:
                print("Opção inválida")

            opcao = self.__votante_view.mostrar_tela()
