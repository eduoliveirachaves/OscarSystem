from typing import List
from models.voto import Voto
from views.membro_view import MembroView
from models.membro import Membro


class MembroController:

    def __init__(self, admin_controller):
        self.__membro_view = MembroView()
        self.__admin_controller = admin_controller
        self.__membros: List[Membro] = []
        self.carregar_dados()

    @property
    def membros(self):
        if len(self.__membros) == 0:
            return ["Nenhum membro cadastrado"]
        return self.__membros

    # refatorar - separar as etapas em novas funcoes
    def iniciar(self):
        opcao = self.__membro_view.mostrar_tela()

        while opcao != "0":
            if opcao == "1":
                autenticado, membro = self.login()
                if autenticado:
                    opcao = self.__membro_view.tela_membro(membro)
                    while opcao != "0":
                        if opcao == "1":
                            categoria = self.__admin_controller.categorias
                            escolhido, categoria = self.__membro_view.tela_voto(membro, categoria)
                            if escolhido == "0":
                                continue

                            self.__membros[membro].add_voto(Voto(membro.id, categoria, escolhido))
                        if opcao == "2":
                            print(self.__membros[membro].votos)

                        opcao = self.__membro_view.mostrar_tela()


            elif opcao == "2":
                nome, data_nascimento, nacionalidade = self.__membro_view.tela_cadastro()
                ID = len(self.__membros) + 1  # usar len temporiariamente so pra fins de teste
                self.__membros.append(Membro(ID, nome, data_nascimento, nacionalidade))

            else:
                print("Opção inválida")

            opcao = self.__membro_view.mostrar_tela()

    def login(self):
        nome, senha = self.__membro_view.tela_login()

        while nome != "voltar tela":
            print(nome)
            for membro in self.__membros:
                if membro.nome == nome and membro.data_nascimento == senha:
                    return True, membro
            else:
                print("Login inválido. Tente novamente.")

            # exibir os membros cadastrados? e pedir somente a data?
            nome, senha = self.__membro_view.tela_login()
        return False, None

    def carregar_dados(self):
        self.__membros.append(Membro(1, "teste", "teste", "Brasil"))
