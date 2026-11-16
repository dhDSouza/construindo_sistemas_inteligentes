# Exercício 07 — Relatório de produtos
# A classe é repetida para que este arquivo execute de forma independente.
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
        if quantidade <= 0 or quantidade > self.estoque:
            return False
        self.estoque = self.estoque - quantidade
        return True

    def valor_em_estoque(self):
        return self.preco * self.estoque


def mostrar_relatorio(produtos):
    # Os acumuladores começam em zero em cada chamada, inclusive com [].
    total = 0
    sem_estoque = 0
    for produto in produtos:
        valor = produto.valor_em_estoque()
        print(produto.nome, "| Estoque:", produto.estoque, "| Valor:", valor)
        total = total + valor
        if produto.estoque == 0:
            sem_estoque = sem_estoque + 1
    print("Valor total em estoque:", total)
    print("Produtos sem estoque:", sem_estoque)


produtos = [
    Produto("Caderno", 10.0, 2),
    Produto("Caneta", 3.0, 0),
    Produto("Borracha", 2.0, 5)
]
mostrar_relatorio(produtos)
print("Relatório com lista vazia:")
mostrar_relatorio([])
