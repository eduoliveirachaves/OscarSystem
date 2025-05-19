class SistemaView:

    def mostrar_tela(self):
        print("\n=== BEM VINDO AO SISTEMA DO OSCAR ===\n")
        print("Selecione uma edicao (ex: 2024) para acessar:")
        print("Edicao 2024")
        print("Edicao 2023")
        print("Edicao 2022")
        print("Cadastrar edicao (digite um ano novo)")
        print("\n0 - Sair")

        opcao = input("\nDigite a opção desejada: ")

        return opcao

    def home_tela(self, ano: int):
        print(f"\n=== OSCAR {ano} ===\n")
        print("1 - Relatórios")
        print("2 - Membros da Academia")
        print("0 - Sair")
        opcao = input("\nDigite a opção desejada: ")
        return opcao



