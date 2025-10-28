import tkinter as tk

def cambiar_color():
    root.config(bg=color.get())

root = tk.Tk()
root.title("Ejercicio 5")

color = tk.StringVar()
color.set("white")

radio1 = tk.Radiobutton(root, text="Rojo", variable=color, value="red", command=cambiar_color)
radio2 = tk.Radiobutton(root, text="Verde", variable=color, value="green", command=cambiar_color)
radio3 = tk.Radiobutton(root, text="Azul", variable=color, value="blue", command=cambiar_color)

radio1.pack()
radio2.pack()
radio3.pack()

root.mainloop()