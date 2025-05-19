from typing import List

from models.categoria import Categoria
from models.diretor import Diretor
from models.filme import Filme
from views.profissional_view import ProfissionalView


class FilmeView:

    def __init__(self):
        self.profissionais_view = ProfissionalView()

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
            categorias_str = ', '.join([cat.nome for cat in filme.categorias])
            print(f"Título: {filme.nome}")
            print(f"Ano: {filme.ano_lancamento}")
            print(f"Diretor: {filme.diretor.nome}")
            print(f"Categorias: {categorias_str}")
            print("-" * 30)

    def cadastrar_filme(self, diretores: List[Diretor], categorias: List[Categoria]):
        print("\n=== Cadastrar Filme ===")
        nome = input("Título: ").strip()
        ano_lancamento = input("Ano de lançamento: ").strip()

        diretor_obj = self.tela_selecao_diretor(diretores)

        if not diretor_obj:
            return None

        categorias_input = self.tela_selecao_categoria(categorias)

        return {
            "nome": nome,
            "ano": ano_lancamento,
            "diretor": diretor_obj,
            "categorias_raw": categorias_input
        }

    def tela_selecao_diretor(self, diretores: List[Diretor]):
        diretor_id, nome, data_nascimento = None, None, None
        while True:
            print("\nSeleção de Diretor:")
            print("1 - Selecionar diretor existente")
            print("2 - Cadastrar novo diretor")
            print("0 - Cancelar")
            opcao = input(">> ").strip()
            if opcao == "1":
                print("\nSelecione o diretor:")
                if not diretores:
                    print("Nenhum diretor cadastrado.")
                    continue
                print(", ".join(str(x) for x in diretores))
                print("0 - Cancelar")
                diretor_id = input("Digite o ID do diretor existente: ").strip()
                if diretor_id == "0":
                    continue
                return {"nome": None, "data": None, "id": diretor_id}
            elif opcao == "2":
                diretor_nome, diretor_data_nascimento = self.profissionais_view.cadastrar_diretor()
                return {"nome": diretor_nome, "data": diretor_data_nascimento, "id": "novo"}
            elif opcao == "0":
                return None

    def tela_selecao_categoria(self, categorias: List[Categoria]):
        print("\nSelecione as categorias:")
        print(", ".join(str(x) for x in categorias))
        print("\nDigite os IDs das categorias (ex: 1,2,3):")
        categorias_input = input(">> ").strip()

        return categorias_input

