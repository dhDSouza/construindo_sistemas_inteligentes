# Desafio extra — Loja do aventureiro

# O nome é texto; o ouro é uma quantidade inteira de moedas.
nome_aventureiro = input("Nome do aventureiro: ")
ouro = int(input("Quantidade de ouro: "))

# Validamos o saldo antes de mostrar o menu ou pedir uma opção.
if ouro < 0:
    print("Quantidade de ouro inválida")
else:
    print("=== LOJA DO AVENTUREIRO ===")
    print("Aventureiro:", nome_aventureiro)
    print("1 - Poção de vida: 25 moedas")
    print("2 - Escudo: 60 moedas")
    print("3 - Espada: 100 moedas")
    opcao = input("Escolha um item: ")

    # Rejeitamos opções desconhecidas antes de consultar item e preço.
    if opcao != "1" and opcao != "2" and opcao != "3":
        print("Item inválido")
    else:
        # Para uma opção válida, guardamos o item e o preço correspondente.
        if opcao == "1":
            item = "Poção de vida"
            preco = 25
        elif opcao == "2":
            item = "Escudo"
            preco = 60
        else:
            item = "Espada"
            preco = 100

        # >= permite comprar também com o valor exato do item.
        if ouro >= preco:
            # Descontamos moedas somente após confirmar saldo suficiente.
            ouro = ouro - preco
            print("Item adquirido:", item)
            print("Saldo restante:", ouro, "moedas")
        else:
            # Calculamos a diferença sem alterar o saldo do aventureiro.
            moedas_faltantes = preco - ouro
            print("Ouro insuficiente. Faltam", moedas_faltantes, "moedas.")

# Testes: 40/1 deixa 15; 60/2 deixa 0; 90/3 informa que faltam 10.
# Com opção 4 não há compra; com ouro -1 o atendimento para na validação.
