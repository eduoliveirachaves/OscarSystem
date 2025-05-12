from models.categoria import Categoria
from models.membro import Membro


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

    def tela_membro(self, membro: Membro):
        print(f"Bem vindo {membro.nome}\n")
        print("1 - Votar")
        print("2 - Visualizar Votos")  # ja feitos
        print("0 - Voltar")
        opcao = input("Digite a opção desejada: ")
        return opcao

    def tela_votos_realizados(self, membro: Membro):
        pass

    def tela_escolher_categoria(self, categorias: list):
        for categoria in categorias:  # exibindo todas, MUDAR PRA exibir somente as que nao votou ainda
            print(categoria)

        categoria = input("Digite a categoria que deseja votar (numero): ")
        return categoria

    def tela_realizar_escolha(self, categoria: Categoria):
        print(f"Você escolheu a categoria {categoria.nome}")
        for indicado in categoria.indicados:
            print(indicado)

        opcao = input("Deseja votar em algum indicado? (s/n): ")
        return opcao

    def tela_votar(self, membro: Membro, categorias: list):
        categoria = self.tela_escolher_categoria(categorias)

