import tkinter as tk
from tkinter import messagebox
import random

def jugar(eleccion):
    if puntos_jugador.get() == 3 or puntos_cpu.get() == 3:
        return
    cpu = random.choice(["piedra", "papel", "tijera"])
    eleccion_cpu.set(cpu)
    resultado.set(comprobar_ganador(eleccion, cpu))
    if puntos_jugador.get() == 3:
        messagebox.showinfo("Fin", "Has ganado la partida")
    elif puntos_cpu.get() == 3:
        messagebox.showinfo("Fin", "Has perdido la partida")

def comprobar_ganador(j, c):
    if j == c:
        return "Empate"
    if (j == "piedra" and c == "tijera") or \
       (j == "papel" and c == "piedra") or \
       (j == "tijera" and c == "papel"):
        puntos_jugador.set(puntos_jugador.get() + 1)
        return "Ganas la ronda"
    else:
        puntos_cpu.set(puntos_cpu.get() + 1)
        return "Pierdes la ronda"

def nuevo():
    puntos_jugador.set(0)
    puntos_cpu.set(0)
    resultado.set("")
    eleccion_cpu.set("")

def salir():
    root.quit()

root = tk.Tk()
root.title("Piedra-Papel-Tijera")

puntos_jugador = tk.IntVar()
puntos_cpu = tk.IntVar()
resultado = tk.StringVar()
eleccion_cpu = tk.StringVar()

frame_superior = tk.Frame(root)
frame_superior.pack()
tk.Label(frame_superior, text="Jugador:").pack(side=tk.LEFT)
tk.Label(frame_superior, textvariable=puntos_jugador).pack(side=tk.LEFT)
tk.Label(frame_superior, text="   Máquina:").pack(side=tk.LEFT)
tk.Label(frame_superior, textvariable=puntos_cpu).pack(side=tk.LEFT)

frame_botones = tk.Frame(root)
frame_botones.pack()

img_piedra = tk.PhotoImage(file="piedra.png")
img_papel = tk.PhotoImage(file="papel.png")
img_tijera = tk.PhotoImage(file="tijera.png")

tk.Button(frame_botones, image=img_piedra, command=lambda: jugar("piedra")).pack(side=tk.LEFT)
tk.Button(frame_botones, image=img_papel, command=lambda: jugar("papel")).pack(side=tk.LEFT)
tk.Button(frame_botones, image=img_tijera, command=lambda: jugar("tijera")).pack(side=tk.LEFT)

frame_centro = tk.Frame(root)
frame_centro.pack()
tk.Label(frame_centro, text="Elección de la máquina:").pack()
tk.Label(frame_centro, textvariable=eleccion_cpu).pack()
tk.Label(frame_centro, textvariable=resultado).pack()

frame_inferior = tk.Frame(root)
frame_inferior.pack()
tk.Button(frame_inferior, text="Nueva partida", command=nuevo).pack(side=tk.LEFT)
tk.Button(frame_inferior, text="Salir", command=salir).pack(side=tk.LEFT)

root.mainloop()
