class MembroView:
    def mostrar_tela(self):
        print("Bem vindo ao sistema de votação do Oscar")
        print("1 - Entrar")
        print("2 - Cadastrar-se")
        print("0 - Sair")
        opcao = input("Digite a opção desejada: ")
        return opcao

    def tela_login(self):
        print("Digite seu nome e senha conforme pedido (Senha é a data de nascimento): ")
        nome = input("Nome: ")
        senha = input("Senha: ")
        return nome, senha

    def tela_cadastro(self):
        print("Digite seu nome e data de nascimento:")
        nome = input("nome: ")
        data_nascimento = input("data de nascimento: ")
        nacionalidade = input("Digite sua nacionalidade: ")
        return nome, data_nascimento, nacionalidade
