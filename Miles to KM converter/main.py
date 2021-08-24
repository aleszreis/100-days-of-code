from tkinter import *

# Janela
window = Tk()
window.title("Miles to KM converter")
window.config(padx=20, pady=20)

# Entrada
entry = Entry(width=7)
entry.grid(column=1, row=0)

# Linha 1:
linha1 = Label(text="Miles")
linha1.grid(column=2, row=0)

# Linha 2
label1 = Label(text="is equal to")
label1.grid(column=0, row=1)
label2 = Label(text=0)
label2.grid(column=1, row=1)
label3 = Label(text="km")
label3.grid(column=2, row=1)

# Botão
def calculate():
    return label2.config(text=float(entry.get()) * 1.609)


button = Button(text="Calculate!", command=calculate)
button.grid(column=1, row=2)


# Fim da janela
window.mainloop()