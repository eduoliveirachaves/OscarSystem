class EdicoesView:

    def mostrar_tela(self):
        print("\n=== EDIÇÃO ===\n")
        print("1 - Acessar Edição")
        print("2 - Cadastrar Edição")
        print("0 - Voltar")
        return input("\nDigite a opção desejada: ")

    def cadastrar_edicao_tela(self, edicoes: list):
        print("\n=== CADASTRAR EDIÇÃO ===\n")
        print("Digite o ano da edição")
        print("Exemplo: 2020")
        print(f"Edicoes cadastradas: {edicoes}")
        print("\n0 - Voltar")
        ano = input("Ano: ")
        if ano == "0":
            return "0"

        if 1900 <= int(ano) > 2030:
            return None
        return ano

    def escolher_edicao_tela(self, edicoes):
        print("\n=== Edições Cadastradas ===\n")
        if not edicoes:
            print("Nenhuma edição cadastrada.")
            return None
        for edicao in edicoes:
            print(f"Oscar - {edicao.ano}")
        print("\n0 - Voltar")

        opcao = input("\nDigite a opção desejada (ano): ")

        if opcao == "0":
            return "0"

        if not opcao.isdigit():
            print("ID INVÁLIDO. Tente novamente.")
            return None

        if int(opcao) not in [edicao.ano for edicao in edicoes]:
            print("EDIÇÃO INVÁLIDA. Tente novamente.")
            return None

        return opcao
