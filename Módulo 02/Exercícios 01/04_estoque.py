# Exercício 04 — Controle de estoque
class Produto:
    def __init__(self, nome, preco, estoque):
        self.nome = nome
        self.preco = preco
        self.estoque = estoque

    def repor(self, quantidade):
        if quantidade <= 0:
            return False
        self.estoque = self.estoque + quantidade
        return True

    def vender(self, quantidade):
        # A recusa acontece antes da alteração, preservando o estoque.
        if quantidade <= 0 or quantidade > self.estoque:
            return False
        self.estoque = self.estoque - quantidade
        return True

    def valor_em_estoque(self):
        return self.preco * self.estoque


produto = Produto("Lápis", 5.0, 4)
retorno = produto.vender(2)
print("Venda de 2:", retorno, "| Estoque:", produto.estoque)
retorno = produto.vender(3)
print("Venda de 3:", retorno, "| Estoque:", produto.estoque)
retorno = produto.repor(5)
print("Reposição de 5:", retorno, "| Estoque:", produto.estoque)
retorno = produto.repor(0)
print("Reposição de 0:", retorno, "| Estoque:", produto.estoque)
print("Valor em estoque:", produto.valor_em_estoque())
