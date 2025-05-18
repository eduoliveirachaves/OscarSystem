from typing import List

from models.categoria import Categoria


class VotacaoView:

    def __init__(self):
        pass


    def mostrar_tela(self):
        print("Bem vindo ao sistema de votação do Oscar\n")
        print("1 - Ja sou cadastrado")
        print("2 - Não sou cadastrado")
        print("3 - Visualizar votos") # so pra poder visualizar todos os votos
        print("0 - Sair")
        opcao = input("\nDigite a opção desejada: ")
        return opcao

    def membro_login_tela(self):
        print("\nBem vindo de volta!")
        nome = input("Digite seu nome: ")
        data_nascimento = input("Digite sua data de nascimento: ")
        return nome, data_nascimento

    def menu_membro_tela(self, nome: str):
        print(f"\n=== MENU DE MEMBROS ===" )
        print(f"Membro: {nome}\n")

        print("1 - Visualizar votos")
        print("2 - Votar")
        print("0 - Voltar")
        opcao = input("\nDigite a opção desejada: ")
        return opcao



    def escolher_categoria_tela(self, categorias: List[Categoria], nome: str):
        print("\n--- TELA DE VOTACAO ---\n")
        print(f"Em que categoria você gostaria de votar {nome} ?")
        for categoria in categorias:
            print(f"{categoria.id} - {categoria.nome}")

        return input("Digite o ID da categoria: ")

    def escolher_indicado_tela(self, categoria: Categoria):
        print(f"\nIndicados na categoria {categoria.nome}: \n")
        for indicado in categoria.indicados:
            print(indicado)

        return input("Digite o ID do indicado: ")

    def visualizar_votos_tela(self, votos):
        print("\n--- Votos ---\n")

        if not votos:
            print("Nenhum voto registrado")
            return

        for voto in votos:
            print(voto)
