class DataLoader:
    def __init__(self):
        pass

    @staticmethod
    def carregar_dados(ano):
        if ano == 2024:
            return DataLoader.carregar_dados_2024()
        elif ano == 2023:
            return DataLoader.carregar_dados_2023()
        elif ano == 2022:
            return DataLoader.carregar_dados_2022()
        else:
            return {"sucess": False}

    @staticmethod
    def carregar_dados_2024():
        filmes = ["Oppenheimer, 2023, Christopher Nolan, 23",
                  "Maestro, 2023, Bradley Cooper, 23",
                  "Rustin, 2023, George C. Wolfe, 23",
                  "The Holdovers, 2023, Alexander Payne, 23",
                  "American Fiction, 2023, Cord Jefferson, 23",
                  "Killers of the Flower Moon, 2023, Martin Scorsese, 23",
                  "Saltburn, 2023, Emerald Fennell, 23",
                  "All of Us Strangers, 2023, Andrew Haigh, 23",
                  "Past Lives, 2023, Celine Song, 23",
                  "Ferrari, 2023, Michael Mann, 23"]

        atores = ["Cillian Murphy, Oppenheimer, 1976, Irlandês",
                  "Bradley Cooper, Maestro, 1975, Americano",
                  "Colman Domingo, Rustin, 1969, Americano",
                  "Paul Giamatti, The Holdovers, 1967, Americano",
                  "Jeffrey Wright, American Fiction, 1965, Americano",
                  "Leonardo DiCaprio, Killers of the Flower Moon, 1974, Americano",
                  "Barry Keoghan, Saltburn, 1992, Irlandês",
                  "Andrew Scott, All of Us Strangers, 1976, Irlandês",
                  "Teo Yoo, Past Lives, 1981, Sul-coreano",
                  "Adam Driver, Ferrari, 1983, Americano"]

        diretores = ["Christopher Nolan, 1970", "Bradley Cooper, 1975", "George C. Wolfe, 1954",
                     "Alexander Payne, 1961", "Cord Jefferson, 1981", "Martin Scorsese, 1942",
                     "Emerald Fennell, 1985", "Andrew Haigh, 1973", "Celine Song, 1988", "Michael Mann, 1943"]

        categorias = ["Ator Coadjuvante, Ator", "Animação, Filme", "Curta de animação, Filme",
                      "Figurino, Filme", "Roteiro Original, Filme", "Roteiro Adaptado, Filme",
                      "Maquiagem e cabelo, Filme", "Edição, Filme", "Atriz Coadjuvante, Ator",
                      "Direção de Arte, Filme", "Canção Original, Filme", "Curta documentário, Filme",
                      "Documentário, Filme", "Som, Filme", "Efeitos Visuais, Filme", "Curta Live Action, Filme",
                      "Fotografia, Filme", "Filme Internacional, Filme", "Trilha Original, Filme",
                      "Ator, Ator", "Direção, Diretor", "Atriz, Ator", "Filme, Filme"]

        membros = ["membro1", "membro2", "membro3"]
        return {"success": True, "filmes": filmes, "atores": atores, "diretores": diretores,
                "categorias": categorias,
                "membros": membros}

    @staticmethod
    def carregar_dados_2023():
        filmes = ["Everything Everywhere All at Once, 2022, Daniels, 23",
                  "The Banshees of Inisherin, 2022, Martin McDonagh, 23",
                  "Top Gun: Maverick, 2022, Joseph Kosinski, 23",
                  "Tar, 2022, Todd Field, 23",
                  "Avatar: The Way of Water, 2022, James Cameron, 23"]

        atores = ["Michelle Yeoh, Everything Everywhere All at Once, 1962, Malaia",
                  "Colin Farrell, The Banshees of Inisherin, 1976, Irlandês",
                  "Brendan Gleeson, The Banshees of Inisherin, 1955, Irlandês",
                  "Cate Blanchett, Tar, 1969, Australiana"]

        diretores = ["Daniels, 1987", "Martin McDonagh, 1970", "Joseph Kosinski, 1974",
                     "Todd Field, 1964", "James Cameron, 1954"]

        categorias = ["Ator Coadjuvante, Ator", "Animação, Filme", "Curta de animação, Filme",
                      "Figurino, Filme", "Roteiro Original, Filme", "Roteiro Adaptado, Filme",
                      "Maquiagem e cabelo, Filme", "Edição, Filme", "Atriz Coadjuvante, Ator",
                      "Direção de Arte, Filme", "Canção Original, Filme", "Curta documentário, Filme",
                      "Documentário, Filme", "Som, Filme", "Efeitos Visuais, Filme", "Curta Live Action, Filme",
                      "Fotografia, Filme", "Filme Internacional, Filme", "Trilha Original, Filme",
                      "Ator, Ator", "Direção, Diretor", "Atriz, Ator", "Filme, Filme"]

        membros = ["membro4", "membro5", "membro6"]
        return {"success": True, "filmes": filmes, "atores": atores, "diretores": diretores,
                "categorias": categorias,
                "membros": membros}

    @staticmethod
    def carregar_dados_2022():
        filmes = ["Dune, 2021, Denis Villeneuve, 23",
                  "The Power of the Dog, 2021, Jane Campion, 23",
                  "Belfast, 2021, Kenneth Branagh, 23",
                  "CODA, 2021, Sian Heder, 23",
                  "King Richard, 2021, Reinaldo Marcus Green, 23"]

        atores = ["Will Smith, King Richard, 1968, Americano",
                  "Benedict Cumberbatch, The Power of the Dog, 1976, Britânico",
                  "Kodi Smit-McPhee, The Power of the Dog, 1996, Australiano"]

        diretores = ["Denis Villeneuve, 1967", "Jane Campion, 1954", "Kenneth Branagh, 1960",
                     "Sian Heder, 1977", "Reinaldo Marcus Green, 1981"]

        categorias = ["Ator Coadjuvante, Ator", "Animação, Filme", "Curta de animação, Filme",
                      "Figurino, Filme", "Roteiro Original, Filme", "Roteiro Adaptado, Filme",
                      "Maquiagem e cabelo, Filme", "Edição, Filme", "Atriz Coadjuvante, Ator",
                      "Direção de Arte, Filme", "Canção Original, Filme", "Curta documentário, Filme",
                      "Documentário, Filme", "Som, Filme", "Efeitos Visuais, Filme", "Curta Live Action, Filme",
                      "Fotografia, Filme", "Filme Internacional, Filme", "Trilha Original, Filme",
                      "Ator, Ator", "Direção, Diretor", "Atriz, Ator", "Filme, Filme"]

        membros = ["membro7", "membro8", "membro9"]
        return {"success": True, "filmes": filmes, "atores": atores, "diretores": diretores,
                "categorias": categorias,
                "membros": membros}
