import tkinter as tk

def mostrar_fruta():
    seleccion = lista.curselection()
    if seleccion:
        fruta = lista.get(seleccion[0])
        etiqueta.config(text=fruta)

root = tk.Tk()
root.title("Ejercicio 6")

lista = tk.Listbox(root)
lista.insert(0, "Manzana")
lista.insert(1, "Banana")
lista.insert(2, "Naranja")
lista.pack()

boton = tk.Button(root, text="Mostrar", command=mostrar_fruta)
boton.pack()

etiqueta = tk.Label(root, text="")
etiqueta.pack()

root.mainloop()
