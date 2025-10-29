import tkinter as tk

def mostrar():
    etiqueta_resultado.config(text=entrada.get())

def borrar():
    entrada.delete(0, tk.END)
    etiqueta_resultado.config(text="")

root = tk.Tk()
root.title("Ejercicio 8")

frame_superior = tk.Frame(root)
frame_superior.pack()

etiqueta_texto = tk.Label(frame_superior, text="Texto:")
etiqueta_texto.pack()

entrada = tk.Entry(frame_superior)
entrada.pack()

etiqueta_resultado_texto = tk.Label(frame_superior, text="Resultado:")
etiqueta_resultado_texto.pack()

etiqueta_resultado = tk.Label(frame_superior, text="")
etiqueta_resultado.pack()

frame_inferior = tk.Frame(root)
frame_inferior.pack()

boton_mostrar = tk.Button(frame_inferior, text="Mostrar", command=mostrar)
boton_mostrar.pack()

boton_borrar = tk.Button(frame_inferior, text="Borrar", command=borrar)
boton_borrar.pack()

root.mainloop()