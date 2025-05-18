class AdminView:

    def __init__(self):
        pass

    # so este esta estatico embora todos possam ser
    # ainda nao sei se a tela vai possivelmente precisar de alguma variavel da classe
    @staticmethod
    def mostrar_tela():
        print("\nADMIN\n")
        print("1 - Filmes")
        print("2 - Profissionais do Cinema")
        print("3 - Categorias")
        print("4 - Membros")
        print("0 - Voltar")
        opcao = input("\nDigite a opção desejada: ")
        return opcao

    # por ex aqui, eu posso fazer assim e retornar os dados obtidos, mas parece meio "desorganizado"
    # ou apenas fazer os prints aqui e usar o input direto no controller
    # mas desta forma o controller nao faria a funcao da tela de alguma forma?
    # parece que desse jeito tem a vantagem de ser mais "refatoravel" mas ao mesmo tempo maior chance de erros

    def cadastrar_ator(self):
        print("Cadastrar ator")
        print("Digite os dados do ator")
        nome = input("Nome: ")
        data_nascimento = input("Data de nascimento: ")
        nacionalidade = input("Nacionalidade: ")
        return nome, nacionalidade, data_nascimento

    def cadastrar_filme(self, categorias: list):
        print("Cadastrar filme")
        print("Digite os dados do filme")
        nome = input("Nome: ")
        ano_lancamento = input("Data de lançamento: ")
        diretor = input("Diretor: ")

        print("Todas as categorias: ")
        print([str(categoria) for categoria in categorias])
        categoria = input("Categoria (mais de uma separar por virgula ex: 1, 2): ")

        return nome, ano_lancamento, diretor, categoria

    def cadastrar_diretor(self):
        print("Cadastrar diretor")
        print("Digite os dados do diretor")
        nome = input("Nome: ")
        data_nascimento = input("Data de nascimento: ")
        return nome, data_nascimento

    def cadastrar_categoria(self):
        print("Cadastrar categoria")
        print("Digite os dados da categoria")
        nome = input("Nome: ")
        return nome

    def listar_filmes(self, lista_filmes):
        print("Lista de filmes")
        for filme in lista_filmes:
            print(
                f"Nome: {filme.nome} | Data de lançamento: {filme.data_lancamento} | Duração: {filme.duracao} | Categoria: {filme.categoria}"
            )

    # SOBRE AS LISTAGENS admin view x user view
    # serviria nao so pra visualizar pra tambem pra editar/remover
    #

    def listar_categorias(self, categorias):
        for categoria in categorias:
            print(categoria)

    def listar_votantes(self, membros):
        for membro in membros:
            print(membro)

    def listar_atores(self, atores):
        for ator in atores:
            print(ator)

    def listar_diretores(self, diretores):
        for diretor in diretores:
            print(diretor)

    def listar_votos(self, categorias: list):
        for categoria in categorias:
            print([str(x) for x in categoria.votos])

    def listar_votos_por_categoria(self, votos: list):
        pass
