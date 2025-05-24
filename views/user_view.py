from models.categoria import Categoria


class UserView:

    def mostrar_tela(self):
        print("\n=== Oscar ===\n")

        print("1 - Dados Gerais")
        print("2 - Selecionar Edicao")

        print("\n0 - Voltar")
        opcao = input("\nDigite a opção desejada: ")
        return opcao

    def menu_relatorios_gerais(self):
        print("\n==== RELATÓRIOS GERAIS ====\n")
        print("1 - Indicações por ano e categoria")
        print("2 - Votos por categoria e ano")
        print("3 - Vencedores por categoria e edição")
        print("4 - Vencedores por nacionalidade")
        print("5 - Top 3 filmes mais premiados")
        print("0 - Voltar\n")
        return input("Escolha uma opção: ")

    def selecionar_edicao_tela(self, edicoes):
        print("\n=== Edições Disponiveis ===\n")
        for edicao in edicoes:
            print(f"Oscar - {edicao.ano}")

        edicao = input("Digite o ano da edição: ")

        return edicao

    def ano_desejado_tela(self, edicoes):
        print("\nQual ano você quer ver os indicados?")
        print("\nEdições disponíveis:", ", ".join(str(e.ano) for e in edicoes))

        ano = input("Digite o ano: ")
        return int(ano)

    def categoria_desejada_tela(self, categorias):
        print("Qual categoria você quer ver os indicados?")
        for categoria in categorias:
            print(f"{categoria.id} - {categoria.nome}")
        categoria = input("Digite o ID da categoria: ")
        return int(categoria)

    def visualizar_indicados(self, categoria: Categoria, ano: int):
        print(f"\nIndicados da categoria {categoria} no ano {ano}:\n")

        if len(categoria.indicados) == 0:
            print("Nenhum indicado disponível para visualização.")
            return

        for indicado in categoria.indicados:
            print(indicado)

        input("Pressione ENTER para continuar...")
        return
