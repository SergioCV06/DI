import tkinter as tk

def actualizar():
    seleccion = ""
    if var1.get() == 1:
        seleccion += "Leer "
    if var2.get() == 1:
        seleccion += "Deporte "
    if var3.get() == 1:
        seleccion += "Música "
    etiqueta.config(text=seleccion)

root = tk.Tk()
root.title("Ejercicio 4")

var1 = tk.IntVar()
var2 = tk.IntVar()
var3 = tk.IntVar()

check1 = tk.Checkbutton(root, text="Leer", variable=var1, command=actualizar)
check2 = tk.Checkbutton(root, text="Deporte", variable=var2, command=actualizar)
check3 = tk.Checkbutton(root, text="Música", variable=var3, command=actualizar)

check1.pack()
check2.pack()
check3.pack()

etiqueta = tk.Label(root, text="")
etiqueta.pack()

root.mainloop()
