class ProfissionalView:
    def mostrar_tela(self):
        print("\nProfissionais do Cinema\n")
        print("1 - Visualizar profissionais")
        print("2 - Cadastrar profissional")
        print("3 - Editar profissional")
        print("0 - Voltar")
        opcao = input("\nDigite a opção desejada: ")
        return opcao

    def tela_visualizar(self):
        print("\nProfissionais do Cinema\n")
        print("1 - Visualizar todos")
        print("2 - Visualizar atores")
        print("3 - Visualizar diretores")
        print("0 - Voltar")

    def visualizar_todos(self, atores, diretores):
        self.visualizar_atores(atores)
        self.visualizar_diretores(diretores)

    def visualizar_atores(self, atores):
        for ator in atores:
            print(ator)

    def visualizar_diretores(self, diretores):
        for diretor in diretores:
            print(diretor)

    def tela_cadastro(self):
        print("\nCadastro de profissional\n")
        print("Que tipo de profissional é?")
        print("1 - Atores")
        print("2 - Diretores")
        tipo = input("Ator ou Diretor: ")
        return tipo

    def cadastrar_ator(self):
        print("\nCadastrar ator\n")
        print("Digite os dados do ator")
        nome = input("Nome: ")
        data_nascimento = input("Data de nascimento: ")
        nacionalidade = input("Nacionalidade: ")
        return nome, nacionalidade, data_nascimento

    def cadastrar_diretor(self):
        print("\nCadastrar diretor\n")
        print("Digite os dados do diretor")
        nome = input("Nome: ")
        data_nascimento = input("Data de nascimento: ")
        return nome, data_nascimento