# Exercício 06 — Turmas independentes
class Turma:
    def __init__(self, nome):
        self.nome = nome
        # Uma lista nova é criada a cada inicialização de uma turma.
        self.alunos = []

    def matricular(self, nome_aluno):
        self.alunos.append(nome_aluno)

    def quantidade_alunos(self):
        return len(self.alunos)


manha = Turma("Manhã")
noite = Turma("Noite")
manha.matricular("Ana")
manha.matricular("Bruno")
noite.matricular("Carla")
for turma in [manha, noite]:
    print(turma.nome, "| Alunos:", turma.alunos,
          "| Quantidade:", turma.quantidade_alunos())
