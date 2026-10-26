# Exercício 04 — Termômetro da sala

# float() permite informar temperaturas com casas decimais.
temperatura = float(input("Temperatura da sala em graus Celsius: "))

# Testamos as faixas em ordem crescente e exibimos só uma classificação.
if temperatura < 18:
    print("Ambiente frio")
elif temperatura < 26:
    # Chegar aqui significa que a temperatura já é maior ou igual a 18.
    print("Ambiente agradável")
else:
    # As duas condições anteriores falsas deixam a faixa a partir de 26.
    print("Ambiente quente")

# Nos limites: 18 é agradável e 26 é quente.
