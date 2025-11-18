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
