# Exercício 07 — Benefício no museu

# O enunciado considera uma idade inteira não negativa.
idade = int(input("Idade: "))

# or exige pelo menos uma condição verdadeira para dar a gratuidade.
if idade < 12 or idade >= 60:
    print("Entrada gratuita.")
else:
    # A faixa restante inclui pessoas de 12 a 59 anos.
    print("Valor da entrada: R$", 20.00)

# Testes: 11 e 60 têm gratuidade; 12 e 59 pagam 20 reais.
