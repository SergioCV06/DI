import tkinter as tk
from tkinter import messagebox

class RegistroApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Ejercicio 14")

        self.barra_menu = tk.Menu(self.root)
        self.root.config(menu=self.barra_menu)

        self.menu_archivo = tk.Menu(self.barra_menu, tearoff=0)
        self.menu_archivo.add_command(label="Guardar Lista", command=self.guardar_lista)
        self.menu_archivo.add_command(label="Cargar Lista", command=self.cargar_lista)
        self.barra_menu.add_cascade(label="Archivo", menu=self.menu_archivo)

        tk.Label(root, text="Nombre:").pack()
        self.entrada_nombre = tk.Entry(root)
        self.entrada_nombre.pack()

        tk.Label(root, text="Edad:").pack()
        self.scale_edad = tk.Scale(root, from_=0, to=100, orient="horizontal")
        self.scale_edad.pack()

        self.var_genero = tk.StringVar()
        self.var_genero.set("Otro")
        tk.Radiobutton(root, text="Masculino", variable=self.var_genero, value="Masculino").pack()
        tk.Radiobutton(root, text="Femenino", variable=self.var_genero, value="Femenino").pack()
        tk.Radiobutton(root, text="Otro", variable=self.var_genero, value="Otro").pack()

        self.scroll = tk.Scrollbar(root)
        self.scroll.pack(side=tk.RIGHT, fill=tk.Y)

        self.lista_usuarios = tk.Listbox(root, yscrollcommand=self.scroll.set)
        self.lista_usuarios.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        self.scroll.config(command=self.lista_usuarios.yview)

        tk.Button(root, text="Añadir", command=self.añadir_usuario).pack()
        tk.Button(root, text="Eliminar", command=self.eliminar_usuario).pack()
        tk.Button(root, text="Salir", command=self.salir).pack()

    def añadir_usuario(self):
        nombre = self.entrada_nombre.get()
        edad = self.scale_edad.get()
        genero = self.var_genero.get()
        if nombre:
            self.lista_usuarios.insert(tk.END, nombre + ", " + str(edad) + ", " + genero)

    def eliminar_usuario(self):
        seleccion = self.lista_usuarios.curselection()
        if seleccion:
            self.lista_usuarios.delete(seleccion[0])

    def salir(self):
        self.root.quit()

    def guardar_lista(self):
        messagebox.showinfo("Guardar Lista", "Lista guardada")

    def cargar_lista(self):
        messagebox.showinfo("Cargar Lista", "Lista cargada")


root = tk.Tk()
app = RegistroApp(root)
root.mainloop()
