# Exercício 19 — Orçamento do passeio

# O ônibus tem custo fixo; ingresso e lanche são cobrados por aluno.
quantidade_alunos = 20
custo_onibus = 600.00
preco_ingresso = 15.00
preco_lanche = 10.00

# Multiplicamos os preços individuais pela quantidade de alunos.
custo_ingressos = preco_ingresso * quantidade_alunos
custo_lanches = preco_lanche * quantidade_alunos

# Incluímos o ônibus uma única vez e dividimos o total pela turma.
custo_total = custo_onibus + custo_ingressos + custo_lanches
valor_por_aluno = custo_total / quantidade_alunos

# Para 20 alunos: ingressos 300.0, lanches 200.0, total 1100.0,
# e valor por aluno 55.0.
print("ORÇAMENTO INICIAL")
print("Quantidade de alunos:", quantidade_alunos)
print("Ônibus: R$", custo_onibus)
print("Todos os ingressos: R$", custo_ingressos)
print("Todos os lanches: R$", custo_lanches)
print("Custo total: R$", custo_total)
print("Valor por aluno: R$", valor_por_aluno)

# Segundo cenário: mudamos somente a quantidade de alunos.
quantidade_alunos = 25

# Repetimos as mesmas fórmulas para recalcular os custos com a nova turma.
custo_ingressos = preco_ingresso * quantidade_alunos
custo_lanches = preco_lanche * quantidade_alunos
custo_total = custo_onibus + custo_ingressos + custo_lanches
valor_por_aluno = custo_total / quantidade_alunos

# Para 25 alunos: ingressos 375.0, lanches 250.0, total 1225.0,
# e valor por aluno 49.0.
print("ORÇAMENTO ATUALIZADO")
print("Quantidade de alunos:", quantidade_alunos)
print("Ônibus: R$", custo_onibus)
print("Todos os ingressos: R$", custo_ingressos)
print("Todos os lanches: R$", custo_lanches)
print("Custo total: R$", custo_total)
print("Valor por aluno: R$", valor_por_aluno)

# O total aumenta porque mais alunos compram ingressos e lanches.
# O valor individual diminui porque os mesmos 600 reais do ônibus
# são divididos entre mais pessoas; ingresso e lanche continuam iguais.
