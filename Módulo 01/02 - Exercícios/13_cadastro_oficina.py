# Exercício 13 — Cadastro de uma oficina

# str representa texto: usamos esse tipo para o nome e a sala.
nome_oficina = "Robótica para iniciantes"
sala = "Laboratório 2"

# int representa um número inteiro, adequado à contagem de vagas.
quantidade_vagas = 24

# float representa um número decimal; em Python, usamos ponto decimal.
duracao_horas = 2.5

# bool representa True (verdadeiro) ou False (falso).
# True indica que as inscrições estão abertas.
inscricoes_abertas = True

# Mostramos o título e uma informação por linha.
print("CADASTRO DA OFICINA")
print("Nome:", nome_oficina)
print("Sala:", sala)
print("Vagas:", quantidade_vagas)
print("Duração em horas:", duracao_horas)
print("Inscrições abertas:", inscricoes_abertas)

# type() informa o tipo do valor armazenado em cada variável.
print("Tipo do nome:", type(nome_oficina))
print("Tipo da sala:", type(sala))
print("Tipo das vagas:", type(quantidade_vagas))
print("Tipo da duração:", type(duracao_horas))
print("Tipo das inscrições abertas:", type(inscricoes_abertas))
