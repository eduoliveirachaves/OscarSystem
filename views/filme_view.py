from typing import List

from models import diretor
from models.categoria import Categoria
from models.diretor import Diretor
from models.filme import Filme
from views.profissional_view import ProfissionalView


class FilmeView:

    def __init__(self):
        self.__profissionais_view = ProfissionalView()

    def mostrar_tela(self):
        print("\n=== Filmes ===")
        print("1 - Visualizar filmes")
        print("2 - Cadastrar filme")
        print("3 - Editar filme")
        print("0 - Voltar")
        opcao = input(">> ")
        return opcao

    def visualizar_filmes(self, filmes: List[Filme]):
        if not filmes:
            print("\nNenhum filme cadastrado.")
            return

        print("\n--- Lista de Filmes ---")
        for filme in filmes:
            categorias_str = ', '.join([cat.nome for cat in filme.categorias_concorrendo])
            print(f"Título: {filme.titulo}")
            print(f"Ano: {filme.ano_lancamento}")
            print(f"Diretor: {filme.diretor.nome}")
            print(f"Categorias: {categorias_str}")
            print("-" * 30)

    def cadastrar_filme(self, diretores: List[Diretor], categorias: List[Categoria]):
        diretor_data_nascimento, diretor_nome, diretor_id = None, None, None
        print("\n=== Cadastrar Filme ===")
        nome = input("Título: ").strip()
        ano_lancamento = input("Ano de lançamento: ").strip()



        while True not in ["1", "2", "0"]:
            print("\nSeleção de Diretor:")
            print("1 - Selecionar diretor existente")
            print("2 - Cadastrar novo diretor")
            print("0 - Cancelar")
            opcao_diretor = input(">> ").strip()
            if opcao_diretor == "1":
                print("\nSelecione o diretor:")
                if not diretores:
                    print("Nenhum diretor cadastrado.")
                    continue
                print(", ".join(str(x) for x in diretores))
                print("0 - Cancelar")
                diretor_id = input("Digite o ID do diretor existente: ").strip()
                if diretor_id == "0":
                    diretor_id = None
                    continue
            elif opcao_diretor == "2":
                diretor_nome, diretor_data_nascimento = self.__profissionais_view.cadastrar_diretor()
                diretor_id = "novo"
                break
            elif opcao_diretor == "0":
                return None

        print("\nSelecione as categorias:")
        print(", ".join(str(x) for x in categorias))
        print("\nDigite os IDs das categorias (ex: 1,2,3):")
        categorias_input = input(">> ").strip()

        return {
            "nome": nome,
            "ano": ano_lancamento,
            "diretor": {"id": diretor_id, "nome": diretor_nome, "data": diretor_data_nascimento},
            "categorias_raw": categorias_input
        }

