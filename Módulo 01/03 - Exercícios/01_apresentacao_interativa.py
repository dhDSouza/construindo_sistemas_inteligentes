# Exercício 01 — Apresentação interativa

# input() devolve texto, adequado para o nome e a cidade.
nome = input("Nome: ")
cidade = input("Cidade: ")

# Convertemos a idade para inteiro para poder somar um ano.
idade = int(input("Idade em anos: "))
idade_proximo_aniversario = idade + 1

# Exibimos os dados recebidos e o resultado do cálculo.
print("=== APRESENTAÇÃO ===")
print("Nome:", nome)
print("Cidade:", cidade)
print("Idade atual:", idade)
print("Idade no próximo aniversário:", idade_proximo_aniversario)
