# Exercício 08 — Conta com operações validadas
class Conta:
    def __init__(self, titular):
        self.titular = titular
        self.saldo = 0

    def depositar(self, valor):
        if valor <= 0:
            return False
        self.saldo = self.saldo + valor
        return True

    def sacar(self, valor):
        if valor <= 0 or valor > self.saldo:
            return False
        self.saldo = self.saldo - valor
        return True


primeira = Conta("Ana")
segunda = Conta("Bruno")
retorno = primeira.depositar(50)
print("Depósito de 50:", retorno, "| Saldo:", primeira.saldo)
retorno = primeira.sacar(20)
print("Saque de 20:", retorno, "| Saldo:", primeira.saldo)
retorno = primeira.sacar(40)
print("Saque de 40:", retorno, "| Saldo:", primeira.saldo)
retorno = primeira.depositar(-10)
print("Depósito de -10:", retorno, "| Saldo:", primeira.saldo)
# A segunda conta possui seu próprio saldo, que continua em zero.
print("Saldo da segunda conta:", segunda.saldo)
