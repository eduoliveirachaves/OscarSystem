from datetime import datetime


class MembroView:
    def mostrar_tela(self):
        print("\n=== MEMBROS DA ACADEMIA ===\n")
        print("1 - Visualizar membros")
        print("2 - Cadastrar membros")
        print("3 - Editar membros")
        print("0 - Voltar")
        opcao = input("\nDigite a opção desejada: ")
        return opcao

    def tela_cadastro(self):
        print("Digite seu nome e data de nascimento:")

        while True:
            nome = input("Nome: ").strip()
            if nome:
                break
            print("Nome não pode estar vazio.")

        while True:
            data_nascimento = input("Data de nascimento (dd/mm/aaaa): ").strip()
            try:
                datetime.strptime(data_nascimento, "%d/%m/%Y")
                break
            except ValueError:
                print("Formato de data inválido. Use dd/mm/aaaa.")

        while True:
            nacionalidade = input("Digite sua nacionalidade: ").strip()
            if nacionalidade:
                break
            print("Nacionalidade não pode estar vazia.")

        return nome, data_nascimento, nacionalidade


    def visualizar_membros(self, membros: list):
        print("\n--- Lista de Membros ---\n")
        print("Nome - Nacionalidade - Data de Nascimento")
        if len(membros) == 0:
            print("\nNenhum membro cadastrado")
            return

        for membro in membros:
            print(membro)



