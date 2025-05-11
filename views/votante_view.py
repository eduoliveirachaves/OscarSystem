def tela_inicial():
    print("Bem vindo ao sistema de votação do Oscar")
    print("1 - Entrar")
    print("2 - Cadastrar-se")
    print("0 - Sair")
    opcao = input("Digite a opção desejada: ")
    return opcao

def tela_login():
    print("Digite seu nome e senha conforme pedido (Senha é a data de nascimento): ")
    nome = input("Nome: ")
    senha = input("Senha: ")
    return nome, senha

def tela_cadastro():
    print("Digite seu nome e data de nascimento:")
    login = input("nome: ")
    senha = input("data de nascimento: ")
    nacionalidade = input("Digite sua nacionalidade: ")
    return login, senha, nacionalidade



class VotanteView:
    def __init__(self):
        pass

