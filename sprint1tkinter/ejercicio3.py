import tkinter as tk

def saludar():
    nombre = entrada.get()
    etiqueta.config(text="Hola " + nombre)

root = tk.Tk()
root.title("Ejercicio 3")

entrada = tk.Entry(root)
entrada.pack()

boton = tk.Button(root, text="Saludar", command=saludar)
boton.pack()

etiqueta = tk.Label(root, text="")
etiqueta.pack()

root.mainloop()
