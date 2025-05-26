class VencedorCategoria:
    def __init__(self, categoria, vencedor):
        self.categoria = categoria
        self.vencedor = vencedor

    def __str__(self):
        return f"{self.categoria.nome} - {self.vencedor.nome})"
