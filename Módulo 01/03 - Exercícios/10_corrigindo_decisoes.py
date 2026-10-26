# Exercício 10 — Corrigindo decisões

# Correção 1: input() devolve str; int() converte a idade para permitir
# sua comparação numérica com o inteiro 16.
idade = int(input("Idade: "))
autorizacao = input("Possui autorização? (sim/nao): ")

# Correção 2: == compara a autorização com "sim"; = serve para atribuir.
# Correção 3: os dois-pontos encerram a linha que inicia o bloco do if.
# and exige idade mínima e autorização ao mesmo tempo.
if idade >= 16 and autorizacao == "sim":
    # Correção 4: quatro espaços colocam esta instrução dentro do if.
    print("Participação permitida.")
else:
    # O else fica alinhado com o if, e seu conteúdo também é indentado.
    print("Participação não permitida.")

# Consideramos idade não negativa e respostas sim ou nao.
# Testes: 16/sim permite; 15/sim e 16/nao não permitem.
