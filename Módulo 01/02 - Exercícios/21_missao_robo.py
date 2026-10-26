# Exercício 21 — Missão do robô explorador

# Definimos o estado inicial do robô antes de qualquer acontecimento.
nome = "Atlas"
energia = 100
distancia_percorrida = 0
amostras_coletadas = 0
missao_em_andamento = True

# Apresentamos todos os dados iniciais com suas descrições e unidades.
print("FICHA INICIAL")
print("Nome:", nome)
print("Energia:", energia)
print("Distância percorrida:", distancia_percorrida, "metros")
print("Amostras coletadas:", amostras_coletadas)
print("Missão em andamento:", missao_em_andamento)

# Etapa 1: somamos 120 metros e descontamos 20 pontos de energia.
distancia_percorrida = distancia_percorrida + 120
energia = energia - 20
print("Etapa 1 — Distância:", distancia_percorrida, "metros; energia:", energia)

# Etapa 2: somamos três amostras e descontamos 15 pontos de energia.
amostras_coletadas = amostras_coletadas + 3
energia = energia - 15
print("Etapa 2 — Amostras:", amostras_coletadas, "; energia:", energia)

# Etapa 3: a recarga acrescenta 10 pontos à energia atual.
energia = energia + 10
print("Etapa 3 — Energia após a recarga:", energia)

# Etapa 4: somamos mais 80 metros e descontamos 25 pontos de energia.
distancia_percorrida = distancia_percorrida + 80
energia = energia - 25
print("Etapa 4 — Distância:", distancia_percorrida, "metros; energia:", energia)

# Etapa 5: somamos mais duas amostras e descontamos 10 pontos de energia.
amostras_coletadas = amostras_coletadas + 2
energia = energia - 10
print("Etapa 5 — Amostras:", amostras_coletadas, "; energia:", energia)

# Etapa 6: False indica que a missão deixou de estar em andamento.
missao_em_andamento = False
print("Etapa 6 — Missão em andamento:", missao_em_andamento)

# Estado final esperado: energia 40, distância 200, cinco amostras
# e missão em andamento igual a False.
print("FICHA FINAL")
print("Nome:", nome)
print("Energia:", energia)
print("Distância percorrida:", distancia_percorrida, "metros")
print("Amostras coletadas:", amostras_coletadas)
print("Missão em andamento:", missao_em_andamento)

# Parte extra: dividimos a distância total pela duração da missão.
duracao_minutos = 4
distancia_media_por_minuto = distancia_percorrida / duracao_minutos
print("Distância média por minuto:", distancia_media_por_minuto, "metros por minuto")
