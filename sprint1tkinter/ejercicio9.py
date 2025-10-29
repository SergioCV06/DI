import tkinter as tk
from tkinter import messagebox

def abrir():
    messagebox.showinfo("Abrir", "Abrir")

def acerca_de():
    messagebox.showinfo("Acerca de", "Versión 3.0")

root = tk.Tk()
root.title("Ejercicio 9")

barra_menu = tk.Menu(root)
root.config(menu=barra_menu)

menu_archivo = tk.Menu(barra_menu, tearoff=0)
menu_archivo.add_command(label="Abrir", command=abrir)
menu_archivo.add_command(label="Salir", command=root.quit)
barra_menu.add_cascade(label="Archivo", menu=menu_archivo)

menu_ayuda = tk.Menu(barra_menu, tearoff=0)
menu_ayuda.add_command(label="Acerca de", command=acerca_de)
barra_menu.add_cascade(label="Ayuda", menu=menu_ayuda)

root.mainloop()
