import csv


class Usuario:
    def __init__(self, nombre, edad, genero, avatar=""):
        self.nombre = nombre
        self.edad = edad
        self.genero = genero
        self.avatar = avatar


class GestorUsuarios:
    def __init__(self):
        self._usuarios = []

    def listar(self):
        return self._usuarios

    def obtener(self, indice):
        return self._usuarios[indice]

    def agregar(self, usuario):
        self._usuarios.append(usuario)

    def limpiar(self):
        self._usuarios.clear()

    def guardar_csv(self, ruta):
        with open(ruta, "w", newline="", encoding="utf-8") as f:
            w = csv.writer(f)
            w.writerow(["nombre", "edad", "genero", "avatar"])
            for u in self._usuarios:
                w.writerow([u.nombre, u.edad, u.genero, u.avatar])

    def cargar_csv(self, ruta):
        try:
            with open(ruta, "r", encoding="utf-8") as f:
                reader = csv.reader(f)
                next(reader)
                self.limpiar()
                for row in reader:
                    nombre, edad, genero, avatar = row
                    self.agregar(Usuario(nombre, int(edad), genero, avatar))
        except FileNotFoundError:
            pass
