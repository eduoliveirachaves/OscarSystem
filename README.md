# 🎬 Sistema de Votação do Oscar - Projeto Orientado a Objetos em Python

Um sistema desenvolvido em Python com foco em programação orientada a objetos, destinado ao gerenciamento de indicações e votos para o Oscar, promovendo um processo organizado e transparente.

## 📌 Descrição do Projeto

Este sistema simula o funcionamento interno da votação da premiação do Oscar. Ele permite que membros da Academia cadastrem e votem em filmes, atores e diretores indicados em diversas categorias.

O sistema permite:
- Cadastro de filmes, categorias, atores, diretores e membros da Academia
- Registro de indicações e votos
- Geração de relatórios sobre indicações, votos, vencedores e filmes mais premiados

## 🧱 Funcionalidades Principais

### 🗃️ Cadastros
- **Membros da Academia**: ID, nome, data de nascimento e nacionalidade
- **Filmes**: Título, diretor, ano de lançamento e categorias indicadas
- **Atores**: Indicados apenas para a categoria *Melhor Ator*
- **Diretores**: Indicados apenas para a categoria *Melhor Direção*
- **Categorias**: Possibilidade de cadastrar novas categorias

### 🗳️ Votação
- Apenas membros cadastrados da Academia podem votar
- Cada membro pode votar uma única vez por categoria
- Votos são registrados por categoria e indicado

### 📊 Relatórios
- Listar indicações por ano ou categoria
- Visualizar quantidade de votos por indicado, categoria e ano
- Exibir vencedores de cada categoria (mais votados)
- Filtrar vencedores por nacionalidade
- Listar os 3 filmes mais premiados

## 🏗️ Arquitetura

O sistema segue o padrão arquitetural **MVC (Model-View-Controller)**:

- **Model**: Entidades principais como Filme, Membro, Categoria, Voto etc.
- **View**: Interfaces baseadas em terminal (CLI)
- **Controller**: Lógica de negócio e controle da aplicação

Também são utilizados:
- **Herança e classes abstratas**
- **Associação, agregação e composição**
- **Tratamento de exceções** para entradas inválidas e regras de votação


### Estrutura de Pastas

```
.
├── models/            # Classes das entidades (Model)
├── controllers/       # Lógica de controle (Controller)
├── views/             # Interfaces de terminal (View)
├── data/              # (Opcional) Armazenamento de dados
├── utils/             # Funções auxiliares
└── main.py            # Ponto de entrada do sistema
```

## 🛠️ Exemplos de Uso

- Cadastrar um filme e indicá-lo para várias categorias
- Registrar um membro da Academia e permitir que ele vote
- Gerar relatório de vencedores por ano
- Listar os 3 filmes com maior número de premiações
- Filtrar vencedores por nacionalidade (ex: brasileiros)

## 🔮 Melhorias Futuras

- Interface gráfica (GUI) ou Web 
- Armazenamento em banco de dados
- Autenticação de membros

