import tkinter as tk

def cambiar_texto():
    etiqueta3.config(text="Texto cambiado")

root = tk.Tk()
root.title("Ejercicio 1")

etiqueta1 = tk.Label(root, text="Bienvenido")
etiqueta1.pack()

etiqueta2 = tk.Label(root, text="Sergio Castelo Varela")
etiqueta2.pack()

etiqueta3 = tk.Label(root, text="Etiqueta que cambia")
etiqueta3.pack()

boton = tk.Button(root, text="Cambiar", command=cambiar_texto)
boton.pack()

root.mainloop()
