# Exercício 03 — Contador de atendimentos
class Contador:
    def __init__(self):
        self.valor = 0

    def incrementar(self):
        self.valor = self.valor + 1

    def zerar(self):
        self.valor = 0


primeiro = Contador()
segundo = Contador()
for vez in range(3):
    primeiro.incrementar()
segundo.incrementar()
print("Antes de zerar:", primeiro.valor, segundo.valor)
# O método altera apenas o objeto que recebeu a chamada.
primeiro.zerar()
print("Depois de zerar:", primeiro.valor, segundo.valor)
