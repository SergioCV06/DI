from pathlib import Path
from tkinter import messagebox
import threading
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
        self.filtered_indices = []
        self.selected_filtered_index = None

        self.auto_save_on = False
        self.auto_thread = None
        self.auto_stop_event = None

        self.view.add_button.configure(command=self.abrir_ventana_añadir)
        self.view.delete_button.configure(command=self.eliminar_usuario)
        self.view.exit_button.configure(command=self.salir)
        self.view.auto_button.configure(command=self.toggle_auto_guardado)

        self.view.menu_archivo.add_command(label="Guardar", command=self.guardar_csv)
        self.view.menu_archivo.add_command(label="Cargar", command=self.cargar_csv)

        self.view.search_var.trace_add("write", lambda *args: self.aplicar_filtros())
        self.view.genero_combo.configure(command=lambda value: self.aplicar_filtros())

        self.cargar_csv(init=True)
        self.aplicar_filtros()
        self.view.set_status("Listo.")

    def aplicar_filtros(self):
        usuarios = self.model.listar()
        texto = self.view.search_var.get().strip().lower()
        genero_filtro = self.view.genero_combo.get().lower()

        self.filtered_indices = []
        for idx, u in enumerate(usuarios):
            if texto and texto not in u.nombre.lower():
                continue
            if genero_filtro != "todos" and u.genero.lower() != genero_filtro:
                continue
            self.filtered_indices.append(idx)

        usuarios_filtrados = [usuarios[i] for i in self.filtered_indices]
        self.selected_filtered_index = None
        self.view.mostrar_detalles_usuario(None)
        self.view.actualizar_lista_usuarios(usuarios_filtrados, self.seleccionar_usuario_desde_lista, self.editar_usuario_desde_lista)
        self.view.set_status(f"{len(usuarios_filtrados)} usuarios visibles.")

    def seleccionar_usuario_desde_lista(self, idx_filtrado):
        if idx_filtrado < 0 or idx_filtrado >= len(self.filtered_indices):
            return
        self.selected_filtered_index = idx_filtrado
        indice_modelo = self.filtered_indices[idx_filtrado]
        try:
            usuario = self.model.obtener(indice_modelo)
        except:
            self.view.mostrar_detalles_usuario(None)
            return
        avatar_image = self.cargar_avatar(usuario.avatar)
        self.view.mostrar_detalles_usuario(usuario, avatar_image)

    def editar_usuario_desde_lista(self, idx_filtrado):
        if idx_filtrado < 0 or idx_filtrado >= len(self.filtered_indices):
            return
        indice_modelo = self.filtered_indices[idx_filtrado]
        self.abrir_ventana_editar(indice_modelo)

    def abrir_ventana_añadir(self):
        self.add_view = AddUserView(self.master)
        self.add_view.window.title("Añadir Nuevo Usuario")
        self.add_view.guardar_button.configure(command=lambda: self.añadir_usuario(self.add_view))

    def abrir_ventana_editar(self, indice_modelo):
        self.edit_view = AddUserView(self.master)
        self.edit_view.window.title("Editar Usuario")
        usuario = self.model.obtener(indice_modelo)
        self.edit_view.nombre_entry.insert(0, usuario.nombre)
        self.edit_view.edad_entry.insert(0, str(usuario.edad))
        self.edit_view.genero_var.set(usuario.genero.lower())
        if usuario.avatar:
            self.edit_view.avatar_var.set(usuario.avatar)
        self.edit_view.guardar_button.configure(command=lambda: self.guardar_edicion(indice_modelo, self.edit_view))

    def añadir_usuario(self, add_view):
        data = add_view.get_data()

        nombre = data["nombre"].strip()
        if not nombre:
            messagebox.showerror("Error", "El nombre no puede estar vacío.")
            return

        try:
            edad = int(data["edad"])
        except:
            messagebox.showerror("Error", "La edad debe ser un número entero.")
            return

        genero = data["genero"]
        avatar = data["avatar"]

        usuario = Usuario(nombre, edad, genero, avatar)
        self.model.agregar(usuario)

        add_view.window.destroy()
        self.aplicar_filtros()
        self.view.set_status("Usuario añadido correctamente.")

    def guardar_edicion(self, indice_modelo, edit_view):
        data = edit_view.get_data()

        nombre = data["nombre"].strip()
        if not nombre:
            messagebox.showerror("Error", "El nombre no puede estar vacío.")
            return

        try:
            edad = int(data["edad"])
        except:
            messagebox.showerror("Error", "La edad debe ser un número entero.")
            return

        genero = data["genero"]
        avatar = data["avatar"]

        usuario = self.model.obtener(indice_modelo)
        usuario.nombre = nombre
        usuario.edad = edad
        usuario.genero = genero
        usuario.avatar = avatar

        edit_view.window.destroy()
        self.aplicar_filtros()
        self.view.set_status("Usuario editado correctamente.")

    def eliminar_usuario(self):
        if self.selected_filtered_index is None:
            messagebox.showerror("Error", "Selecciona un usuario para eliminar.")
            return
        indice_modelo = self.filtered_indices[self.selected_filtered_index]
        self.model.eliminar(indice_modelo)
        self.selected_filtered_index = None
        self.aplicar_filtros()
        self.view.set_status("Usuario eliminado.")

    def cargar_avatar(self, filename):
        ruta = self.assets_dir / filename
        if not filename or not ruta.exists():
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
        self.view.set_status("Usuarios guardados en CSV.")

    def cargar_csv(self, init=False):
        self.model.cargar_csv(self.csv_path)
        if not init:
            messagebox.showinfo("OK", "Usuarios cargados desde CSV.")
            self.view.set_status("Usuarios cargados desde CSV.")
        self.aplicar_filtros()

    def toggle_auto_guardado(self):
        if not self.auto_save_on:
            self.auto_save_on = True
            self.auto_stop_event = threading.Event()
            self.auto_thread = threading.Thread(target=self.auto_guardado_loop, daemon=True)
            self.auto_thread.start()
            self.view.auto_button.configure(text="Auto-guardar (10s): ON")
            self.view.set_status("Auto-guardado activado.")
        else:
            self.auto_save_on = False
            if self.auto_stop_event is not None:
                self.auto_stop_event.set()
            self.auto_thread = None
            self.view.auto_button.configure(text="Auto-guardar (10s): OFF")
            self.view.set_status("Auto-guardado desactivado.")

    def auto_guardado_loop(self):
        while not self.auto_stop_event.is_set():
            self.auto_stop_event.wait(10)
            if self.auto_stop_event.is_set():
                break
            try:
                self.model.guardar_csv(self.csv_path)
                self.master.after(0, lambda: self.view.set_status("Auto-guardado en CSV."))
            except:
                pass

    def salir(self):
        if self.auto_save_on and self.auto_stop_event is not None:
            self.auto_stop_event.set()
        self.master.destroy()
