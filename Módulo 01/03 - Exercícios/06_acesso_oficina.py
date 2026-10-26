# Exercício 06 — Acesso à oficina

# Consideramos idade não negativa e resposta exatamente sim ou nao.
idade = int(input("Idade: "))
inscricao = input("Possui inscrição? (sim/nao): ")

# and exige que a idade mínima E a inscrição sejam atendidas.
# == compara o texto recebido com a resposta que confirma a inscrição.
if idade >= 14 and inscricao == "sim":
    print("Entrada permitida.")
else:
    print("Entrada não permitida.")

# Testes: 14/sim permite; 14/nao, 13/sim e 13/nao não permitem.
