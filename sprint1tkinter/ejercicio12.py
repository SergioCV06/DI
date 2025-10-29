import tkinter as tk
from tkinter import messagebox

def añadir_usuario():
    nombre = entrada_nombre.get()
    edad = scale_edad.get()
    genero = var_genero.get()
    if nombre:
        lista_usuarios.insert(tk.END, nombre + ", " + str(edad) + ", " + genero)

def eliminar_usuario():
    seleccion = lista_usuarios.curselection()
    if seleccion:
        lista_usuarios.delete(seleccion[0])

def guardar():
    messagebox.showinfo("Guardar Lista", "Lista guardada")

def cargar():
    messagebox.showinfo("Cargar Lista", "Lista cargada")

root = tk.Tk()
root.title("Ejercicio 12")

barra_menu = tk.Menu(root)
root.config(menu=barra_menu)

menu_archivo = tk.Menu(barra_menu, tearoff=0)
menu_archivo.add_command(label="Guardar Lista", command=guardar)
menu_archivo.add_command(label="Cargar Lista", command=cargar)
barra_menu.add_cascade(label="Archivo", menu=menu_archivo)

tk.Label(root, text="Nombre:").pack()
entrada_nombre = tk.Entry(root)
entrada_nombre.pack()

tk.Label(root, text="Edad:").pack()
scale_edad = tk.Scale(root, from_=0, to=100, orient="horizontal")
scale_edad.pack()

var_genero = tk.StringVar()
var_genero.set("Otro")

tk.Radiobutton(root, text="Masculino", variable=var_genero, value="Masculino").pack()
tk.Radiobutton(root, text="Femenino", variable=var_genero, value="Femenino").pack()
tk.Radiobutton(root, text="Otro", variable=var_genero, value="Otro").pack()

boton_añadir = tk.Button(root, text="Añadir", command=añadir_usuario)
boton_añadir.pack()

scroll = tk.Scrollbar(root)
scroll.pack(side=tk.RIGHT, fill=tk.Y)

lista_usuarios = tk.Listbox(root, yscrollcommand=scroll.set)
lista_usuarios.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
scroll.config(command=lista_usuarios.yview)

boton_eliminar = tk.Button(root, text="Eliminar", command=eliminar_usuario)
boton_eliminar.pack()

boton_salir = tk.Button(root, text="Salir", command=root.quit)
boton_salir.pack()

root.mainloop()
