class AdminView:

    def __init__(self):
        pass

    # so este esta estatico embora todos possam ser
    # ainda nao sei se a tela vai possivelmente precisar de alguma variavel da classe
    @staticmethod
    def mostrar_tela():
        print("ADMIN")
        print("1 - Cadastrar ator")
        print("2 - Cadastrar filme")
        print("3 - Cadastrar diretor")
        print("0 - Voltar")
        opcao = input("Digite a opção desejada: ")
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

    def cadastrar_filme(self):
        print("Cadastrar filme")
        print("Digite os dados do filme")
        nome = input("Nome: ")
        ano_lancamento = input("Data de lançamento: ")
        diretor = input("Diretor: ")
        categoria = input("Categoria (mais de uma separar por virgula ex: Filme, Ator Coadjuvante): ")
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

    def listar_categorias(self):
        pass

    def listar_votantes(self):
        pass

    def listar_atores(self):
        pass

    def listar_diretores(self):
        pass

    def listar_votos(self):
        pass

    def listar_votos_por_categoria(self):
        pass

