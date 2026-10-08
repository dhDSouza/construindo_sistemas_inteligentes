"""
Sem utilizar nenhum recurso além do que foi visto na aula, crie um pequeno sistema representando um personagem de RPG.

O personagem deve possuir:

nome
vida
ouro
nivel

Durante a aventura:

ganha ouro
recebe dano
gasta ouro
recupera vida
sobe de nível

Cada acontecimento deve alterar a variável correspondente.

No final, apresente o estado atualizado do personagem.
"""

# Definindo as variáveis do personagem
nome = "Sir. Racha Cuca"
vida = 100
ouro = 50
nivel = 5


# Exibindo o estado inicial do personagem

print("========================")
print("      PERSONAGEM")
print("========================")
print("Nome:", nome)
print("Vida:", vida)
print("Ouro:", ouro)
print("Nível:", nivel)

# Acontecimentos durante a aventura
print()
print("Aventura começou!")
print("Certa vez,", nome, "estava explorando uma caverna e encontrou um baú de tesouro.")
print(nome, "ganhou 100 de ouro!")
ouro += 100  # Ganhou ouro
print()
print("O Troll que vivia na caverna, viu", nome, "roubando o seu tesouro e atacou!")
vida -= 30  # Recebeu dano
print(nome, "recebeu 30 de dano!")
print()
print(nome, "consegiu escapar do Troll com vida, então resolveu ir até a cidade mais próxima para consultar com um curandeiro.")
print(nome, "gastou 20 de ouro para se curar!")
ouro -= 20  # Gastou ouro
print(nome, "recuperou 20 de vida!")
vida += 20  # Recuperou vida
print()
print(nome, "sentia que não estava preparado para enfrentar um Troll das Cavernas, já que o último que enfrentou quase o levou a óbito, então decidiu treinar para se tornar mais forte.")
print(nome, "subiu de nível!")
nivel += 1  # Subiu de nível


# Apresentando o estado atualizado do personagem
print()
print("========================")
print("      PERSONAGEM")
print("========================")
print("Nome:", nome)
print("Vida:", vida)
print("Ouro:", ouro)
print("Nível:", nivel)

# Explicação do código:

"""
Este código implementa um pequeno sistema de RPG com um personagem que possui atributos como nome, vida, ouro e nível. 
Durante a aventura, o personagem pode ganhar ouro, receber dano, gastar ouro, recuperar vida e subir de nível. 
Cada ação altera a variável correspondente, e no final, o estado atualizado do personagem é apresentado.

OBS: O andamento da aventura é um recurso narrativo para demonstrar as alterações nas variáveis do personagem.
Você pode modificar os valores e acontecimentos para criar diferentes cenários e resultados para o personagem. 
"""