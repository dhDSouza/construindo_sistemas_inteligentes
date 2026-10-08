""" 
Um personagem possui inicialmente:

200 pontos de vida

Durante uma batalha:

recebe 45 de dano
recebe 30 de dano
recupera 20 pontos de vida

Crie uma variável vida e atualize seu valor depois de cada acontecimento.

Mostre somente a quantidade final de vida.
"""

# Inicializando a variável
vida = 200

# Atualizando a vida após receber dano e recuperar pontos
vida -= 45  # Recebe 45 de dano
vida -= 30  # Recebe 30 de dano
vida += 20  # Recupera 20 pontos de vida

# Exibindo a quantidade final de vida
print("Quantidade final de vida:", vida)

# Explicação do código:

"""
O código acima simula a atualização da quantidade de vida de um personagem durante uma batalha.
Inicialmente, a variável `vida` é definida com o valor de 200 pontos.
Em seguida, a vida do personagem é atualizada conforme os acontecimentos da batalha: ele recebe 45 pontos de dano, depois mais 30 pontos de dano, e finalmente recupera 20 pontos de vida.
A cada atualização, a variável `vida` é modificada utilizando operadores de atribuição (`-
"""