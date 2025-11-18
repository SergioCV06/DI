class Usuario:
    def __init__(self, nombre, edad, genero, avatar=""):
        self.nombre = nombre
        self.edad = edad
        self.genero = genero
        self.avatar = avatar

    def __repr__(self):
        return f"Usuario({self.nombre}, {self.edad}, {self.genero}, {self.avatar})"


class GestorUsuarios:
    def __init__(self):
        self._usuarios = []
        self._cargar_datos_de_ejemplo()

    def _cargar_datos_de_ejemplo(self):
        self._usuarios.append(Usuario("Ana García", 25, "Femenino", "avatar1.png"))
        self._usuarios.append(Usuario("Luis Pérez", 30, "Masculino", "avatar2.png"))
        self._usuarios.append(Usuario("Sofía Romero", 22, "Femenino", ""))

    def listar(self):
        return self._usuarios

    def obtener(self, indice):
        return self._usuarios[indice]
