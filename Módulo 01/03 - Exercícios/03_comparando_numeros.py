# Exercício 03 — Comparando números

# int() transforma cada texto digitado em um número inteiro.
primeiro_numero = int(input("Primeiro número inteiro: "))
segundo_numero = int(input("Segundo número inteiro: "))

# A cadeia escolhe apenas uma das três possibilidades.
if primeiro_numero > segundo_numero:
    print("O primeiro número é maior.")
elif segundo_numero > primeiro_numero:
    print("O segundo número é maior.")
else:
    # Se nenhum é maior que o outro, os dois são iguais.
    print("Os dois números são iguais.")
