import tkinter as tk
from Pessoa import Pessoa
from datetime import datetime as dt
from tkinter import messagebox as mb

#metodo limpar
def limpar():
    lista = [campoNome, campoAno]

    for input in lista:
        input.delete(0, tk.END)

#metedodo calcular
def getInput():
    try:
        humano = Pessoa(campoNome.get(), int(campoAno.get()))
        mb.showinfo(title = "Resultado", message = f'ola {humano.nome}, voce tem {humano.idade()}')
    except ValueError:
        mb.showerror(title = 'Erro', message ='informe um ano ANIMAL')


#janela

janela = tk.Tk()
janela.geometry("320x300")
janela.title("Age Calculator")
janela.resizable(False,False)
janela.anchor(anchor = 'center')


nome = tk.Label(text = "Nome:", height = 2, font = ("comic sans", 14, "bold"))
nome.grid(column = 0, row = 1)

ano = tk.Label(text = "Ano:", height = 2, font = ("comic sans", 14, "bold"))
ano.grid(column = 0, row = 4)

#Entradas

campoNome = tk.Entry(width = 12, font = ("comic sans", 14))
campoNome.grid(column = 1, row = 1)

campoAno = tk.Entry(width = 12, font = ("comic sans", 14))
campoAno.grid(column = 1, row = 4)

#Butões

bCalcular = tk.Button(janela, text = "OK", command = getInput, width = 10, font = ("comic sans", 14))
bCalcular.grid(column = 1, row = 5)

bLimpar = tk.Button(janela, text = "Limpar", command = limpar, width = 10, font = ("comic sans", 14))
bLimpar.grid(column = 0, row = 5)


janela.mainloop()