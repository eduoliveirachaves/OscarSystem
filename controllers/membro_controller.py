from typing import List

from models.categoria import Categoria
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
            # 1 - login
            if opcao == "1":
                autenticado, membro = self.login()
                if autenticado:
                    self.home(membro)

            # 2 - cadastro
            elif opcao == "2":
                self.cadastro()

            else:
                print("Opção inválida")

            opcao = self.__membro_view.mostrar_tela()

    # funcao login recebe nome e senha
    # retorna True se login for bem sucedido e False caso contrario
    # caso login for bem sucedido retorna o membro
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

    def cadastro(self):
        nome, data_nascimento, nacionalidade = self.__membro_view.tela_cadastro()
        ID = len(self.__membros) + 1  # usar len temporiariamente so pra fins de teste
        self.__membros.append(Membro(ID, nome, data_nascimento, nacionalidade))

    def home(self, membro: Membro):
        opcao = self.__membro_view.tela_membro(membro)
        while opcao != "0":
            if opcao == "1":
                categoria = self.__admin_controller.categorias
                escolhido, categoria = self.__membro_view.tela_voto(categoria)
                if escolhido == "0":
                    continue

                escolhido = int(escolhido) - 1

                self.votar(membro, categoria, escolhido)
            if opcao == "2":
                print(self.__membros[membro].votos)

            opcao = self.__membro_view.mostrar_tela()

    def votar(self, membro: Membro, categoria: Categoria, escolhido):
        membro.add_voto(Voto(membro.id, categoria, categoria.indicados[escolhido]))
        categoria.add_voto(membro)


    def carregar_dados(self):
        self.__membros.append(Membro(1, "teste", "teste", "Brasil"))
