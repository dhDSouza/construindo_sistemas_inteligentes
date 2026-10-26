# Exercício 08 — Pedido de livros

# Cada execução começa com oito exemplares disponíveis.
estoque = 8
quantidade = int(input("Quantidade de livros que deseja retirar: "))

# Primeiro rejeitamos pedidos sem uma quantidade positiva.
if quantidade <= 0:
    print("Pedido inválido: a quantidade deve ser maior que zero.")
elif quantidade > estoque:
    # Um pedido positivo ainda pode ultrapassar o estoque.
    print("Não há exemplares suficientes.")
else:
    # Só alteramos o estoque no caminho que confirma o pedido.
    estoque = estoque - quantidade
    print("Pedido confirmado.")
    print("Quantidade restante:", estoque)

# Testes: 0 é inválido; 9 excede o estoque; 3 deixa 5; 8 deixa 0.
