# Exercício 17 — Oficina de correção

# Nomes de variáveis não podem conter espaços; usamos snake_case.
nome_curso = "Python básico"

# Números decimais usam ponto. A vírgula de 89,90 formaria uma tupla,
# não o número decimal que representa o valor da mensalidade.
mensalidade = 89.90

# O valor booleano verdadeiro é escrito True, com T maiúsculo.
matricula_ativa = True

# Exibimos o valor da variável cujo nome foi corrigido.
print("Curso:", nome_curso)

# Python diferencia maiúsculas de minúsculas: Mensalidade e mensalidade
# são nomes diferentes. Usamos exatamente o nome definido acima.
print("Mensalidade: R$", mensalidade)
print("Matrícula ativa:", matricula_ativa)

# Conferimos que o valor decimal tem tipo float.
print("Tipo da mensalidade:", type(mensalidade))
