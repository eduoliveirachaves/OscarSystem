class FilmePremiado:
    def __init__(self, titulo, premios):
        self.titulo = titulo
        self.premios = premios

    def __str__(self):
        return f"{self.titulo} ({self.premios})"
