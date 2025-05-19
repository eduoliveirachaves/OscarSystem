class UserView:

    def mostrar_tela(self):
        print("\n=== Oscar ===\n")

        print("1 - Dados Gerais")
        print("2 - Selecionar Edicao")

        print("0 - Voltar")
        opcao = input("\nDigite a opção desejada: ")
        print("")
        return opcao

    def dados_gerais_tela(self):
        print("IMPLMENTAR")
        return

    def selecionar_edicao_tela(self, edicoes):
        print("\n=== Edições Disponiveis ===\n")
        for edicao in edicoes:
            print(f"Oscar - {edicao.ano}")

        edicao = input("Digite o ano da edição: ")

        return edicao

