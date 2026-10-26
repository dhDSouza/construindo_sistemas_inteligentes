# Exercício 18 — Guardando o valor anterior

# Iniciamos o saldo e guardamos seu valor atual em outra variável.
saldo = 80
saldo_anterior = saldo

# Descontamos 25: o saldo passa a 55.
saldo = saldo - 25

# Acrescentamos 10: o saldo passa a 65.
saldo = saldo + 10

# Previsões: saldo anterior de 80 e saldo atual de 65.
print("Saldo anterior:", saldo_anterior)
print("Saldo atual:", saldo)

# saldo_anterior recebeu o inteiro 80 no momento da atribuição.
# Atribuir novos valores a saldo não altera saldo_anterior:
# a atribuição não cria uma ligação de atualização entre as variáveis.

# Acrescentamos a despesa solicitada: o saldo atual passa a 50.
saldo = saldo - 15

# Previsões após a despesa: saldo anterior de 80 e saldo atual de 50.
print("Saldo anterior após a nova despesa:", saldo_anterior)
print("Saldo atual após a despesa de 15:", saldo)
