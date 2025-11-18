from pathlib import Path
from tkinter import messagebox
import customtkinter as ctk
from PIL import Image

from model.usuario_model import GestorUsuarios, Usuario
from view.main_view import MainView, AddUserView


class AppController:
    def __init__(self, master):
        self.master = master
        self.model = GestorUsuarios()
        self.view = MainView(master)

        self.base_dir = Path(__file__).resolve().parent.parent
        self.assets_dir = self.base_dir / "assets"
        self.csv_path = self.base_dir / "usuarios.csv"

        self.avatar_cache = {}

        self.view.add_button.configure(command=self.abrir_ventana_añadir)
        self.view.exit_button.configure(command=self.salir)

        self.view.menu_archivo.add_command(label="Guardar", command=self.guardar_csv)
        self.view.menu_archivo.add_command(label="Cargar", command=self.cargar_csv)

        self.cargar_csv(init=True)
        self.refrescar_lista_usuarios()

    def refrescar_lista_usuarios(self):
        self.view.actualizar_lista_usuarios(self.model.listar(), self.seleccionar_usuario)

    def seleccionar_usuario(self, indice):
        try:
            usuario = self.model.obtener(indice)
        except:
            self.view.mostrar_detalles_usuario(None)
            return

        avatar_image = self.cargar_avatar(usuario.avatar)
        self.view.mostrar_detalles_usuario(usuario, avatar_image)

    def abrir_ventana_añadir(self):
        self.add_view = AddUserView(self.master)
        self.add_view.guardar_button.configure(command=lambda: self.añadir_usuario(self.add_view))

    def añadir_usuario(self, add_view):
        data = add_view.get_data()

        if not data["nombre"].strip():
            messagebox.showerror("Error", "El nombre no puede estar vacío.")
            return

        try:
            edad = int(data["edad"])
        except:
            messagebox.showerror("Error", "La edad debe ser un número entero.")
            return

        usuario = Usuario(data["nombre"], edad, data["genero"], data["avatar"])
        self.model.agregar(usuario)

        self.refrescar_lista_usuarios()
        add_view.window.destroy()

    def cargar_avatar(self, filename):
        ruta = self.assets_dir / filename
        if not ruta.exists():
            return None

        if filename in self.avatar_cache:
            return self.avatar_cache[filename]

        img = Image.open(ruta)
        ctk_img = ctk.CTkImage(light_image=img, dark_image=img, size=(140, 140))
        self.avatar_cache[filename] = ctk_img
        return ctk_img

    def guardar_csv(self):
        self.model.guardar_csv(self.csv_path)
        messagebox.showinfo("OK", "Usuarios guardados en CSV.")

    def cargar_csv(self, init=False):
        self.model.cargar_csv(self.csv_path)
        if not init:
            messagebox.showinfo("OK", "Usuarios cargados desde CSV.")
        self.refrescar_lista_usuarios()

    def salir(self):
        self.master.destroy()
