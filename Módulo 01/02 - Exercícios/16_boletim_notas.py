# Exercício 16 — Boletim de notas

# Guardamos o nome e cada nota separadamente para permitir alterações.
nome_aluno = "Ana"
nota_1 = 7.5
nota_2 = 8.0
nota_3 = 9.5
quantidade_atividades = 3

# Como todas as atividades têm o mesmo peso, somamos e dividimos por três.
soma_notas = nota_1 + nota_2 + nota_3
media = soma_notas / quantidade_atividades

# Exibimos o primeiro cenário: média esperada de aproximadamente 8.33.
print("BOLETIM ORIGINAL")
print("Aluno:", nome_aluno)
print("Nota 1:", nota_1)
print("Nota 2:", nota_2)
print("Nota 3:", nota_3)
print("Média:", media)

# Segundo cenário: alteramos apenas a segunda nota, conforme o enunciado.
nota_2 = 6.5

# Precisamos executar os cálculos novamente: variáveis não são fórmulas
# que se atualizam sozinhas quando outra variável muda.
soma_notas = nota_1 + nota_2 + nota_3
media = soma_notas / quantidade_atividades

# A nova média esperada é aproximadamente 7.83.
print("BOLETIM COM A SEGUNDA NOTA ALTERADA")
print("Aluno:", nome_aluno)
print("Nota 1:", nota_1)
print("Nota 2:", nota_2)
print("Nota 3:", nota_3)
print("Média:", media)
