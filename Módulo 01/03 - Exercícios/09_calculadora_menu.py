# Exercício 09 — Calculadora com menu

# Convertemos os operandos para float para aceitar números decimais.
numero_1 = float(input("Primeiro número (use ponto decimal): "))
numero_2 = float(input("Segundo número (use ponto decimal): "))

# A opção permanece como texto e será comparada com textos entre aspas.
print("=== CALCULADORA ===")
print("1 - Somar")
print("2 - Subtrair")
print("3 - Multiplicar")
print("4 - Dividir")
opcao = input("Escolha uma opção: ")

# Cada bloco calcula somente a operação escolhida.
if opcao == "1":
    resultado = numero_1 + numero_2
    print("Resultado:", resultado)
elif opcao == "2":
    resultado = numero_1 - numero_2
    print("Resultado:", resultado)
elif opcao == "3":
    resultado = numero_1 * numero_2
    print("Resultado:", resultado)
elif opcao == "4":
    # Verificamos o divisor antes de tentar executar a divisão.
    if numero_2 == 0:
        print("Não é possível dividir por zero")
    else:
        resultado = numero_1 / numero_2
        print("Resultado:", resultado)
else:
    # Qualquer texto diferente das quatro opções chega a este bloco.
    print("Opção inválida")
