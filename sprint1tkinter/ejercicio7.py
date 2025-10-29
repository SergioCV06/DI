import tkinter as tk

def dibujar():
    canvas.delete("all")
    x1 = int(entrada_x1.get())
    y1 = int(entrada_y1.get())
    x2 = int(entrada_x2.get())
    y2 = int(entrada_y2.get())
    figura = opcion.get()
    if figura == "rectangulo":
        canvas.create_rectangle(x1, y1, x2, y2)
    if figura == "circulo":
        canvas.create_oval(x1, y1, x2, y2)

root = tk.Tk()
root.title("Ejercicio 7")

opcion = tk.StringVar()
opcion.set("rectangulo")

tk.Radiobutton(root, text="Rectángulo", variable=opcion, value="rectangulo").pack()
tk.Radiobutton(root, text="Círculo", variable=opcion, value="circulo").pack()

tk.Label(root, text="x1").pack()
entrada_x1 = tk.Entry(root)
entrada_x1.pack()

tk.Label(root, text="y1").pack()
entrada_y1 = tk.Entry(root)
entrada_y1.pack()

tk.Label(root, text="x2").pack()
entrada_x2 = tk.Entry(root)
entrada_x2.pack()

tk.Label(root, text="y2").pack()
entrada_y2 = tk.Entry(root)
entrada_y2.pack()

tk.Button(root, text="Dibujar", command=dibujar).pack()

canvas = tk.Canvas(root, width=400, height=400)
canvas.pack()

root.mainloop()