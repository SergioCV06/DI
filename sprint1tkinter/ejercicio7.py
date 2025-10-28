import tkinter as tk

def dibujar():
    x1 = int(entrada_x1.get())
    y1 = int(entrada_y1.get())
    x2 = int(entrada_x2.get())
    y2 = int(entrada_y2.get())
    canvas.create_rectangle(x1, y1, x2, y2)
    canvas.create_oval(x1, y1, x2, y2)

root = tk.Tk()
root.title("Ejercicio 7")

entrada_x1 = tk.Entry(root)
entrada_y1 = tk.Entry(root)
entrada_x2 = tk.Entry(root)
entrada_y2 = tk.Entry(root)

entrada_x1.pack()
entrada_y1.pack()
entrada_x2.pack()
entrada_y2.pack()

boton = tk.Button(root, text="Dibujar", command=dibujar)
boton.pack()

canvas = tk.Canvas(root, width=300, height=300)
canvas.pack()

root.mainloop()
