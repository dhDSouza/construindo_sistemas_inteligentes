# Exercício 05 — Empréstimo de um livro
class Livro:
    def __init__(self, titulo):
        self.titulo = titulo
        self.emprestado = False

    def emprestar(self):
        if self.emprestado:
            return False
        self.emprestado = True
        return True

    def devolver(self):
        if not self.emprestado:
            return False
        self.emprestado = False
        return True


livro = Livro("Dom Casmurro")
for tentativa in range(2):
    retorno = livro.emprestar()
    print("Empréstimo:", retorno, "| Emprestado:", livro.emprestado)
for tentativa in range(2):
    retorno = livro.devolver()
    print("Devolução:", retorno, "| Emprestado:", livro.emprestado)
# As tentativas recusadas não modificam o estado do livro.
