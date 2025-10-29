import tkinter as tk

def clic(event):
    canvas.create_oval(event.x - 10, event.y - 10, event.x + 10, event.y + 10)

def tecla(event):
    if event.keysym == "c":
        canvas.delete("all")

root = tk.Tk()
root.title("Ejercicio 13")

canvas = tk.Canvas(root, width=400, height=400)
canvas.pack()

canvas.bind("<Button-1>", clic)
root.bind("<KeyPress>", tecla)

root.mainloop()