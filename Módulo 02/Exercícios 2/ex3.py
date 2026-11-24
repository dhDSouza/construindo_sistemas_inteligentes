import tkinter as tk

janela = tk.Tk()
janela.geometry("400x220")
janela.title("Formulário de Cadastro")

lblNome = tk.Label(janela, text="Nome:")
nome = tk.Entry(janela, width=30)

lblIdade = tk.Label(janela, text="Idade:")
idade = tk.Entry(janela, width=30)

lblEmail = tk.Label(janela, text="Email:")
email = tk.Entry(janela, width=30)

resultado = tk.Label(janela, text="clique em cadastrar", font=("Arial", 12))

def cadastrar():
    if nome.get().strip() == "" or idade.get().strip() == "" or email.get().strip() == "":
        resultado.config(text="Todos os campos são obrigatórios!", fg="red")
    elif not idade.get().isdigit() or int(idade.get()) < 0:
        resultado.config(text="Idade inválida!", fg="red")
    else:
        resultado.config(text="Cadastro com sucesso!", fg="green")

btnConfirmar = tk.Button(janela, text="Confirmar", command=cadastrar)

lblNome.grid(row=0, column=0)
nome.grid(row=0, column=1)
lblIdade.grid(row=1, column=0)
idade.grid(row=1, column=1)
lblEmail.grid(row=2, column=0)
email.grid(row=2, column=1)
btnConfirmar.grid(row=3, column=0, columnspan=2)
resultado.grid(row=4, column=0, columnspan=2)

janela.mainloop()
