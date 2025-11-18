import customtkinter as ctk
import tkinter


class AddUserView:
    def __init__(self, master):
        self.window = ctk.CTkToplevel(master)
        self.window.title("Añadir Nuevo Usuario")
        self.window.geometry("380x560")
        self.window.resizable(False, False)
        self.window.grab_set()

        self.window.columnconfigure(0, weight=1)

        self.nombre_label = ctk.CTkLabel(self.window, text="Nombre:")
        self.nombre_label.grid(row=0, column=0, padx=20, pady=(20, 5), sticky="w")

        self.nombre_entry = ctk.CTkEntry(self.window)
        self.nombre_entry.grid(row=1, column=0, padx=20, pady=5, sticky="ew")

        self.edad_label = ctk.CTkLabel(self.window, text="Edad:")
        self.edad_label.grid(row=2, column=0, padx=20, pady=(15, 5), sticky="w")

        self.edad_entry = ctk.CTkEntry(self.window)
        self.edad_entry.grid(row=3, column=0, padx=20, pady=5, sticky="ew")

        self.genero_label = ctk.CTkLabel(self.window, text="Género:")
        self.genero_label.grid(row=4, column=0, padx=20, pady=(15, 5), sticky="w")

        self.genero_var = tkinter.StringVar(value="Otro")

        self.genero_frame = ctk.CTkFrame(self.window)
        self.genero_frame.grid(row=5, column=0, padx=20, pady=5, sticky="w")

        self.genero_m = ctk.CTkRadioButton(self.genero_frame, text="Masculino", variable=self.genero_var, value="Masculino")
        self.genero_m.grid(row=0, column=0, padx=5, pady=2)

        self.genero_f = ctk.CTkRadioButton(self.genero_frame, text="Femenino", variable=self.genero_var, value="Femenino")
        self.genero_f.grid(row=1, column=0, padx=5, pady=2)

        self.genero_o = ctk.CTkRadioButton(self.genero_frame, text="Otro", variable=self.genero_var, value="Otro")
        self.genero_o.grid(row=2, column=0, padx=5, pady=2)

        self.avatar_label = ctk.CTkLabel(self.window, text="Avatar:")
        self.avatar_label.grid(row=6, column=0, padx=20, pady=(15, 5), sticky="w")

        self.avatar_var = tkinter.StringVar(value="avatar1.png")

        self.avatar_frame = ctk.CTkFrame(self.window)
        self.avatar_frame.grid(row=7, column=0, padx=20, pady=5, sticky="w")

        self.avatar1 = ctk.CTkRadioButton(self.avatar_frame, text="Avatar 1", variable=self.avatar_var, value="avatar1.png")
        self.avatar1.grid(row=0, column=0, padx=5, pady=2)

        self.avatar2 = ctk.CTkRadioButton(self.avatar_frame, text="Avatar 2", variable=self.avatar_var, value="avatar2.png")
        self.avatar2.grid(row=1, column=0, padx=5, pady=2)

        self.buttons_frame = ctk.CTkFrame(self.window)
        self.buttons_frame.grid(row=8, column=0, padx=20, pady=20, sticky="ew")
        self.buttons_frame.columnconfigure(0, weight=1)
        self.buttons_frame.columnconfigure(1, weight=1)

        self.guardar_button = ctk.CTkButton(self.buttons_frame, text="Guardar")
        self.guardar_button.grid(row=0, column=0, padx=10, pady=5, sticky="ew")

        self.cancelar_button = ctk.CTkButton(self.buttons_frame, text="Cancelar", command=self.window.destroy)
        self.cancelar_button.grid(row=0, column=1, padx=10, pady=5, sticky="ew")

    def get_data(self):
        return {
            "nombre": self.nombre_entry.get(),
            "edad": self.edad_entry.get(),
            "genero": self.genero_var.get(),
            "avatar": self.avatar_var.get()
        }


class MainView:
    def __init__(self, master):
        self.master = master

        self.menubar = tkinter.Menu(master)
        master.config(menu=self.menubar)

        self.menu_archivo = tkinter.Menu(self.menubar, tearoff=0)
        self.menubar.add_cascade(label="Archivo", menu=self.menu_archivo)

        self.master.rowconfigure(0, weight=1)
        self.master.rowconfigure(1, weight=0)
        self.master.columnconfigure(0, weight=1)
        self.master.columnconfigure(1, weight=1)

        self.left_frame = ctk.CTkFrame(self.master)
        self.left_frame.grid(row=0, column=0, sticky="nsew", padx=10, pady=10)

        self.right_frame = ctk.CTkFrame(self.master)
        self.right_frame.grid(row=0, column=1, sticky="nsew", padx=10, pady=10)

        self.bottom_frame = ctk.CTkFrame(self.master)
        self.bottom_frame.grid(row=1, column=0, columnspan=2, sticky="ew", padx=10, pady=(0, 10))
        self.bottom_frame.columnconfigure(0, weight=1)
        self.bottom_frame.columnconfigure(1, weight=1)

        self.lista_usuarios_scrollable = ctk.CTkScrollableFrame(
            self.left_frame, label_text="Usuarios"
        )
        self.lista_usuarios_scrollable.pack(fill="both", expand=True, padx=10, pady=10)

        self.detalles_contenido = ctk.CTkFrame(self.right_frame)
        self.detalles_contenido.pack(fill="both", expand=True, padx=10, pady=10)
        self.detalles_contenido.columnconfigure(0, weight=1)

        self.detalles_titulo = ctk.CTkLabel(self.detalles_contenido, text="Detalles del Usuario", font=("Arial", 18))
        self.detalles_titulo.grid(row=0, column=0, pady=(10, 10))

        self.avatar_label = ctk.CTkLabel(self.detalles_contenido, text="")
        self.avatar_label.grid(row=1, column=0, pady=(10, 20))

        self.nombre_label = ctk.CTkLabel(self.detalles_contenido, text="Nombre:")
        self.nombre_label.grid(row=2, column=0, pady=5, sticky="w")

        self.edad_label = ctk.CTkLabel(self.detalles_contenido, text="Edad:")
        self.edad_label.grid(row=3, column=0, pady=5, sticky="w")

        self.genero_label = ctk.CTkLabel(self.detalles_contenido, text="Género:")
        self.genero_label.grid(row=4, column=0, pady=5, sticky="w")

        self.add_button = ctk.CTkButton(self.bottom_frame, text="Añadir Usuario")
        self.add_button.grid(row=0, column=0, padx=10, pady=10, sticky="w")

        self.exit_button = ctk.CTkButton(self.bottom_frame, text="Salir")
        self.exit_button.grid(row=0, column=1, padx=10, pady=10, sticky="e")

        self.avatar_image = None

    def actualizar_lista_usuarios(self, usuarios, on_seleccionar_callback):
        for widget in self.lista_usuarios_scrollable.winfo_children():
            widget.destroy()
        for i, usuario in enumerate(usuarios):
            btn = ctk.CTkButton(
                self.lista_usuarios_scrollable,
                text=usuario.nombre,
                command=lambda idx=i: on_seleccionar_callback(idx)
            )
            btn.pack(fill="x", padx=10, pady=5)

    def mostrar_detalles_usuario(self, usuario, avatar_image=None):
        if usuario is None:
            self.nombre_label.configure(text="Nombre:")
            self.edad_label.configure(text="Edad:")
            self.genero_label.configure(text="Género:")
            self.avatar_label.configure(image=None, text="")
            self.avatar_image = None
            return

        self.nombre_label.configure(text=f"Nombre: {usuario.nombre}")
        self.edad_label.configure(text=f"Edad: {usuario.edad}")
        self.genero_label.configure(text=f"Género: {usuario.genero}")

        if avatar_image:
            self.avatar_image = avatar_image
            self.avatar_label.configure(image=self.avatar_image, text="")
        else:
            self.avatar_label.configure(image=None, text="")
            self.avatar_image = None
