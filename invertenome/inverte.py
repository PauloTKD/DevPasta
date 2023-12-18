import tkinter as tk


#janela
janela = tk.Tk()
janela.geometry("400x300")
janela.title("Age Calculator")
janela.resizable(False,False)
janela.anchor(anchor = 'center')

#function

def getInput():
    isso= campoDigitado.get()
    txt = isso [::-1]
    inverted.config(text = txt)
    


#tela
digitado = tk.Label(text = "Digite uma palavra:", height = 2, font = ("comic sans", 14, "bold"))
digitado.grid(column = 0, row = 0)

inverted= tk.Label(height = 2, font = ("comic sans", 14, "bold"))
inverted.grid(column = 1, row = 1)


campoDigitado = tk.Entry(width = 12, font = ("comic sans", 14))
campoDigitado.grid(column = 1, row = 0)


#botao
bValidando = tk.Button(janela, text = "Validando", command = getInput, width = 10, font = ("comic sans", 14))
bValidando.grid(column = 1, row = 2)


janela.mainloop()