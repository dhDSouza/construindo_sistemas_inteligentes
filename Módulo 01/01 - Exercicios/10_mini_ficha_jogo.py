"""
Crie um personagem contendo pelo menos:

nome
classe
nivel
vida
ataque
defesa
possui_magia

Depois calcule uma variável:

poder_total

utilizando:

ataque + defesa

Mostre uma ficha organizada no terminal.

Exemplo de formato:

========================
      PERSONAGEM
========================
Nome:
Classe:
Nível:
Vida:
Ataque:
Defesa:
Poder Total:
Possui magia:
========================
"""

# Definindo as variáveis do personagem
nome = "Arthas"
classe = "Cavaleiro"
nivel = 10
vida = 1500
ataque = 200
defesa = 150
possui_magia = True

# Calculando o poder total
poder_total = ataque + defesa

# Apresentando a ficha do personagem
print("========================")
print("      PERSONAGEM")
print("========================")
print(f"Nome: {nome}")
print(f"Classe: {classe}")
print(f"Nível: {nivel}")
print(f"Vida: {vida}")
print(f"Ataque: {ataque}")
print(f"Defesa: {defesa}")
print(f"Poder Total: {poder_total}")
print(f"Possui magia: {possui_magia}")
print("========================")

# Explicação do código:

"""
O código acima define várias variáveis que representam as características de um personagem em um jogo. 
Ele calcula o poder total do personagem somando os valores de ataque e defesa. 
Em seguida, exibe uma ficha organizada no terminal com todas as informações do personagem, incluindo nome, classe, nível, vida, ataque, defesa, poder total e se possui magia.
"""