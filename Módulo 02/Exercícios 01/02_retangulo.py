# Exercício 02 — Área de um retângulo
class Retangulo:
    def __init__(self, largura, altura):
        # O enunciado considera medidas positivas.
        self.largura = largura
        self.altura = altura

    def calcular_area(self):
        # return permite guardar ou reutilizar a área em outros cálculos.
        return self.largura * self.altura


primeiro = Retangulo(4, 3)
segundo = Retangulo(5, 2)
# A apresentação fica fora do método de cálculo.
print("Área do primeiro:", primeiro.calcular_area())
print("Área do segundo:", segundo.calcular_area())
