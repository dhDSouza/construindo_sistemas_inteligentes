# Exercício 20 — Uma variável, diferentes tipos

# As aspas fazem de "42" um texto (str), mesmo contendo algarismos.
informacao = "42"
print("Valor:", informacao, "Tipo:", type(informacao))

# Sem aspas, 42 é um inteiro (int), que pode participar de cálculos.
informacao = 42
print("Valor:", informacao, "Tipo:", type(informacao))

# O ponto decimal faz de 42.0 um número do tipo float.
informacao = 42.0
print("Valor:", informacao, "Tipo:", type(informacao))

# False é um valor booleano (bool), escrito sem aspas e com F maiúsculo.
informacao = False
print("Valor:", informacao, "Tipo:", type(informacao))

# A variável mantém apenas o último valor atribuído, neste caso False.
# Ela não guarda automaticamente um histórico dos quatro valores.
