# Exercício 02 — Conta da lanchonete

# O preço pode ter casas decimais; a quantidade é um número inteiro.
# Conforme o enunciado, consideramos valores positivos.
preco_lanche = float(input("Preço do lanche em reais (use ponto decimal): "))
quantidade = int(input("Quantidade comprada: "))
total = preco_lanche * quantidade

# >= inclui o total de exatamente 50 reais na regra de desconto.
if total >= 50:
    desconto = total * 0.10
else:
    # Sem desconto, subtraímos zero para manter o valor original.
    desconto = 0.0

# Calculamos o valor final depois de decidir qual desconto aplicar.
valor_final = total - desconto
print("Total antes do desconto: R$", total)
print("Desconto: R$", desconto)
print("Valor final: R$", valor_final)

# Testes: preço 10 e quantidades 4, 5 e 6 resultam em totais 40, 50 e 60.
# Os valores finais esperados são, respectivamente, 40, 45 e 54 reais.
