import tkinter as tk

def actualizar(valor):
    etiqueta.config(text=valor)

root = tk.Tk()
root.title("Ejercicio 11")

scale = tk.Scale(root, from_=0, to=100, orient="horizontal", command=actualizar)
scale.pack()

etiqueta = tk.Label(root, text="0")
etiqueta.pack()

root.mainloop()