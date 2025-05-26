from models.categoria import Categoria


class RelatoriosView:

    def mostrar_tela(self):
        print("\n==== RELATÓRIOS ====\n")
        print("1 - Indicações por ano e categoria")
        print("2 - Votos por ano e categoria")
        print("3 - Vencedores por categoria e edição")
        print("4 - Vencedores por nacionalidade")
        print("5 - Top 3 filmes mais premiados")
        print("\n0 - Voltar\n")
        return input("Escolha uma opção: ")

    def selecionar_edicao_tela(self, edicoes):
        print("\n=== Edições Disponiveis ===\n")
        for edicao in edicoes:
            print(f"Oscar - {edicao.ano}")

        edicao = input("Digite o ano da edição: ")

        return edicao


    def categoria_desejada_tela(self, categorias):
        print("Qual categoria você quer ver os indicados?")
        for categoria in categorias:
            print(f"{categoria.id} - {categoria.nome}")
        categoria = input("Digite o ID da categoria: ")
        return int(categoria)

    def visualizar_indicados(self, categoria: Categoria, ano: int):
        print(f"\nIndicados da categoria {categoria.nome} no ano {ano}:\n")

        if len(categoria.indicados) == 0:
            print("Nenhum indicado disponível para visualização.")
            return

        for indicado in categoria.indicados:
            print(indicado)

        input("Pressione ENTER para continuar...")
        return

    def edicao_ou_categoria_tela(self):
        print("\n=== Relatórios ===\n")
        print("1 - De Todas as Categorias")
        print("2 - De uma categoria específica")
        print("0 - Voltar")
        return input("Escolha uma opção: ")

    def mostrar_vencedores(self, ano, vencedores):
        print(f"\n=== Vencedores {ano} ===\n")
        if not vencedores:
            print("Nenhum vencedor encontrado.")
            return

        for vencedor in vencedores:
            print(f"{vencedor.categoria.nome} - {vencedor.vencedor.nome} ({vencedor.ano})")

        input("Pressione ENTER para continuar...")

    def solicitar_nacionalidade(self):
        print("\n=== Vencedores por Nacionalidade ===\n")
        nacionalidade = input("Digite a nacionalidade (ou '0' para voltar): ")
        if nacionalidade == "0":
            return None
        return nacionalidade

    def mostrar_top_filmes(self, filmes_premiados):
        print("\n=== Top Filmes Mais Premiados ===\n")
        if not filmes_premiados:
            print("Nenhum filme premiado encontrado.")
            return

        for filme in filmes_premiados:
            print(f"{filme.titulo} - {filme.premios} prêmios")

        input("Pressione ENTER para continuar...")

    def mostrar_vencedores_nacionalidade(self, ano, vencedores, nacionalidade):
        print(f"\n=== Vencedores {ano} - Nacionalidade: {nacionalidade} ===\n")
        if not vencedores:
            print("Nenhum vencedor encontrado.")
            return

        for vencedor in vencedores:
            print(f"{vencedor.categoria.nome} - {vencedor.vencedor.nome} ({vencedor.ano})")

        input("Pressione ENTER para continuar...")
