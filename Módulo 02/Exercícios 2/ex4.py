import tkinter as tk

janela = tk.Tk()
janela.title("Calculadora Simples")
janela.geometry("400x200")

lblPrimeiro = tk.Label(janela, text="Primeiro Número:", font=("Arial", 10))
n1 = tk.Entry(janela, width=20)

lblSegundo = tk.Label(janela, text="Segundo Número:", font=("Arial", 10))
n2 = tk.Entry(janela, width=20)

lblPrimeiro.pack(pady=10)
n1.pack(padx=15)

lblSegundo.pack(pady=10)
n2.pack(padx=15)

botoes = tk.Frame(janela)
botoes.pack(pady=10)

resultado = tk.Label(janela, text="Resultado: ", font=("Arial", 10))

def calcular(operacao):
    if operacao == "+":
        resultado.config(text=f"Resultado: {int(n1.get()) + int(n2.get())}", fg="green")
    elif operacao == "-":
        resultado.config(text=f"Resultado: {int(n1.get()) - int(n2.get())}", fg="green")
    elif operacao == "*":
        resultado.config(text=f"Resultado: {int(n1.get()) * int(n2.get())}", fg="green")
    elif operacao == "/":
        if int(n2.get()) == 0:
            resultado.config(text="Não é possível dividir por zero!", fg="red")
        else:
            resultado.config(text=f"Resultado: {int(n1.get()) / int(n2.get())}", fg="green")


btnSoma = tk.Button(botoes, text="+", command=lambda: calcular("+"))
btnSub = tk.Button(botoes, text="-", command=lambda: calcular("-"))
btnMult = tk.Button(botoes, text="*", command=lambda: calcular("*"))
btnDiv = tk.Button(botoes, text="/", command=lambda: calcular("/"))

btnSoma.grid(row=0, column=0, padx=5)
btnSub.grid(row=0, column=1, padx=5)
btnMult.grid(row=0, column=2, padx=5)
btnDiv.grid(row=0, column=3, padx=5)

resultado.pack(pady=10)

janela.mainloop()
