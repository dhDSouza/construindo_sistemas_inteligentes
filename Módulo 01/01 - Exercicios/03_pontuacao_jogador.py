"""
Um jogador inicia uma partida com:

250 pontos

Durante a partida:

ganha 120 pontos
perde 50 pontos
ganha 30 pontos

Crie uma variável chamada pontos e atualize seu valor a cada acontecimento.

Ao final mostre:

Pontuação final: ...

Não realize o cálculo manualmente antes.

O programa deverá fazer todas as alterações.
"""

# Inicializando a pontuação do jogador
pontos = 250

# Ganha 120 pontos
pontos += 120

# Perde 50 pontos
pontos -= 50

# Ganha 30 pontos
pontos += 30

# Exibindo a pontuação final
print("Pontuação final:", pontos)

# Explicação do código:

"""
O código acima simula a pontuação de um jogador durante uma partida. 
Inicialmente, o jogador começa com 250 pontos. 
Em seguida, o programa atualiza a pontuação do jogador com base nos acontecimentos da partida:

1. O jogador ganha 120 pontos, então a pontuação é atualizada para 370 pontos (250 + 120).
2. O jogador perde 50 pontos, então a pontuação é atualizada para 320 pontos (370 - 50).
3. O jogador ganha 30 pontos, então a pontuação final é atualizada para 350 pontos (320 + 30).
O resultado final é exibido na tela, mostrando que o jogador finalmente tem 350 pontos.

Para realizar essas operações, utilizamos operadores de atribuição (`+=` e `-=`) que permitem atualizar o valor da variável `pontos` de forma concisa.
Como alternativa, poderíamos ter usado a forma tradicional de atribuição, como `pontos = pontos + 120`, mas o uso dos operadores de atribuição torna o código mais limpo e legível.

"""