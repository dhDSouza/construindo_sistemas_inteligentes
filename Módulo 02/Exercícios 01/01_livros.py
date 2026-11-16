# Exercício 01 — Cadastro de livros
class Livro:
    def __init__(self, titulo, autor, paginas):
        # self guarda os dados na instância que está sendo inicializada.
        self.titulo = titulo
        self.autor = autor
        self.paginas = paginas


primeiro = Livro("Dom Casmurro", "Machado de Assis", 256)
segundo = Livro("O Pequeno Príncipe", "Antoine de Saint-Exupéry", 96)

print("Antes da alteração:")
for livro in [primeiro, segundo]:
    print(livro.titulo, "|", livro.autor, "| Páginas:", livro.paginas)

# Duas chamadas a Livro(...) criam instâncias independentes.
primeiro.paginas = 280
print("Depois da alteração:")
for livro in [primeiro, segundo]:
    print(livro.titulo, "|", livro.autor, "| Páginas:", livro.paginas)
