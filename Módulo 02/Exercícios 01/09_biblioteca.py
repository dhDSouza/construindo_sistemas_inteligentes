# Desafio extra — Biblioteca com menu
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


livros = [
    Livro("Dom Casmurro"),
    Livro("O Pequeno Príncipe"),
    Livro("A Moreninha")
]

while True:
    print("\n1 - Mostrar livros e disponibilidade")
    print("2 - Emprestar um livro")
    print("3 - Devolver um livro")
    print("0 - Sair")
    opcao = input("Opção: ")

    if opcao == "0":
        print("Biblioteca encerrada.")
        break
    elif opcao == "1":
        for livro in livros:
            if livro.emprestado:
                print(livro.titulo, "- Emprestado")
            else:
                print(livro.titulo, "- Disponível")
    elif opcao == "2" or opcao == "3":
        titulo = input("Título: ")
        encontrado = None
        # A comparação é exata: inclui maiúsculas, acentos e espaços.
        for livro in livros:
            if livro.titulo == titulo:
                encontrado = livro
                break

        if encontrado is None:
            print("Livro não encontrado")
        elif opcao == "2":
            # O menu consulta o retorno; a regra pertence ao método.
            if encontrado.emprestar():
                print("Empréstimo realizado.")
            else:
                print("Livro já emprestado.")
        else:
            if encontrado.devolver():
                print("Devolução realizada.")
            else:
                print("Livro já disponível.")
    else:
        print("Opção desconhecida.")
