from models.categoria import Categoria
from models.membro import Membro


class MembroView:
    def mostrar_tela(self):
        print("\nMembros da Academia\n")
        print("1 - Visualizar membros")
        print("2 - Cadastrar membros")
        print("3 - Editar membros")
        print("0 - Voltar")
        opcao = input("\nDigite a opção desejada: ")
        return opcao

    def tela_cadastro(self):
        print("Digite seu nome e data de nascimento:")
        nome = input("nome: ")
        data_nascimento = input("data de nascimento: ")
        nacionalidade = input("Digite sua nacionalidade: ")
        return nome, data_nascimento, nacionalidade

    def visualizar_membros(self, membros: list):
        if len(membros) == 0:
            print("\nNenhum membro cadastrado")
            return

        for membro in membros:
            print(membro)



