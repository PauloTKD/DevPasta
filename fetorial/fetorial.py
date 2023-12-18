import tkinter as tk

def getInput() -> int:
    n = int(campoDigitado.get())
    fat = 1
    i = 2
    while i <= n:
        fat = fat*i
        i += 1
    
    fetorial.config(text=f"O valor de {n} = {fat}")
    
# print("O valor de %d! eh =" %n, fat)
#main()



#janela
janela = tk.Tk()
janela.geometry("400x300")
janela.title("Age Calculator")
janela.resizable(False,False)
janela.anchor(anchor = 'center')


#tela
digitado = tk.Label(text = "Digite um Numero:", height = 2, font = ("comic sans", 14, "bold"))
digitado.grid(column = 0, row = 0)



#espaço para dar a entrada
campoDigitado = tk.Entry(width = 12, font = ("comic sans", 14))
campoDigitado.grid(column = 1, row = 0)


#espaço para por o resultado
fetorial= tk.Label(height = 2, font = ("comic sans", 14, "bold"))
fetorial.grid(column = 1, row = 1)

#botao
bValidando = tk.Button(janela, text = "Ok", command = getInput, width = 10, font = ("comic sans", 14))
bValidando.grid(column = 1, row = 2)



janela.mainloop()