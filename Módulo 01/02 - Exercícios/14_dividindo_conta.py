# Exercício 14 — Dividindo a conta

# Guardamos os preços em reais e a quantidade inteira de amigos.
preco_pizza = 48.00
preco_bebida = 12.00
quantidade_amigos = 4

# Somamos os dois produtos para obter o total da compra.
total_conta = preco_pizza + preco_bebida

# Dividimos o total igualmente entre os quatro amigos.
valor_por_pessoa = total_conta / quantidade_amigos

# Resultados esperados: total de 60.0 e pagamento de 15.0 por pessoa.
print("Total da conta: R$", total_conta)
print("Valor por pessoa: R$", valor_por_pessoa)
print("Tipo do valor por pessoa:", type(valor_por_pessoa))

# A divisão com / entre esses números produz float, mesmo sem centavos.
