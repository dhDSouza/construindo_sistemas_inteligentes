# Exercício 15 — Estoque da biblioteca

# Previsão inicial: 40 livros disponíveis.
livros_disponiveis = 40
print("Quantidade inicial:", livros_disponiveis)

# Somamos os livros novos ao valor atual. Previsão: 52 livros.
livros_disponiveis = livros_disponiveis + 12
print("Após receber 12 livros novos:", livros_disponiveis)

# Subtraímos o primeiro empréstimo. Previsão: 43 livros.
livros_disponiveis = livros_disponiveis - 9
print("Após emprestar 9 livros:", livros_disponiveis)

# Somamos os livros devolvidos. Previsão: 47 livros.
livros_disponiveis = livros_disponiveis + 4
print("Após receber 4 devoluções:", livros_disponiveis)

# Subtraímos o segundo empréstimo. Previsão: 41 livros.
livros_disponiveis = livros_disponiveis - 6
print("Após emprestar mais 6 livros:", livros_disponiveis)

# Cada atribuição usa o valor atual e guarda o resultado na mesma variável.
