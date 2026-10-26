# Exercício 05 — Boletim com decisão

# Lemos as duas notas como números decimais de mesmo peso.
nota_1 = float(input("Primeira nota (0 a 10): "))
nota_2 = float(input("Segunda nota (0 a 10): "))

# Basta uma nota fora da faixa para invalidar o boletim: usamos or.
if nota_1 < 0 or nota_1 > 10 or nota_2 < 0 or nota_2 > 10:
    print("Nota inválida")
else:
    # A média só é calculada quando as duas notas são válidas.
    media = (nota_1 + nota_2) / 2
    print("Média:", media)

    # Começamos pela faixa mais alta para não confundir aprovação
    # com recuperação. A cadeia executa somente um desses blocos.
    if media >= 7:
        print("Aprovado")
    elif media >= 5:
        print("Recuperação")
    else:
        print("Reprovado")

# Nos limites: média 7 aprova; média 5 leva à recuperação.
