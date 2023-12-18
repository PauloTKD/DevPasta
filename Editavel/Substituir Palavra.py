import tkinter as tk



#functions
def substituir():
    txt = texto
    frase = str(texto["text"])
    frase = frase.replace(campoPalavra.get(), campoTroca.get())
    texto["text"] = frase

def limpar():
    lista = [campoPalavra, campoTroca]
    for input in lista:
        input.delete(0, tk.END)



#janela
janela = tk.Tk()
janela.geometry("450x320")
janela.title("Age Calculator")
janela.resizable(False,False)
janela.anchor(anchor = 'center')


#tela
letra_escolhida = tk.Label(text = "Escolha a palavra para modificar:", height = 2, font = ("comic sans", 14, "bold"))
letra_escolhida.grid(column = 0, row = 0)

digitado = tk.Label(text = "digite a palavra quer colocar:", height = 2, font = ("comic sans", 14, "bold"))
digitado.grid(column = 0, row = 1)


#texto
texto= tk.Label(text= '"Texto Editavel"'  , height = 2, font = ("comic sans", 14, "bold"))
texto.grid(column = 0, row = 3)

#espaço para dar a entrada
campoPalavra = tk.Entry(width = 12, font = ("comic sans", 14))
campoPalavra.grid(column = 1, row = 0)

campoTroca = tk.Entry(width = 12, font = ("comic sans", 14))
campoTroca.grid(column = 1, row = 1)

#espaço para por o resultado
fetorial= tk.Label(height = 2, font = ("comic sans", 14, "bold"))
fetorial.grid(column = 1, row = 3)

#botao
bValidando = tk.Button(janela, text = "Ok", command = substituir , width = 10, font = ("comic sans", 14))
bValidando.grid(column = 1, row = 7)

bLimpar = tk.Button(janela, text = "Limpar", command = limpar, width = 10, font = ("comic sans", 14))
bLimpar.grid(column = 0, row = 7)

janela.mainloop()