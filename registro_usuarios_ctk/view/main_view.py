import customtkinter as ctk


class MainView:
    def __init__(self, master):
        self.master = master

        self.master.rowconfigure(0, weight=1)
        self.master.columnconfigure(0, weight=1)
        self.master.columnconfigure(1, weight=2)

        self.lista_usuarios_frame = ctk.CTkFrame(self.master)
        self.lista_usuarios_frame.grid(row=0, column=0, sticky="nsew", padx=10, pady=10)

        self.lista_usuarios_scrollable = ctk.CTkScrollableFrame(
            self.lista_usuarios_frame, label_text="Usuarios"
        )
        self.lista_usuarios_scrollable.pack(fill="both", expand=True, padx=5, pady=5)

        self.detalle_frame = ctk.CTkFrame(self.master)
        self.detalle_frame.grid(row=0, column=1, sticky="nsew", padx=10, pady=10)
        self.detalle_frame.columnconfigure(0, weight=1)

        self.nombre_label = ctk.CTkLabel(self.detalle_frame, text="Nombre:", anchor="w")
        self.nombre_label.grid(row=0, column=0, pady=5, sticky="w")

        self.edad_label = ctk.CTkLabel(self.detalle_frame, text="Edad:", anchor="w")
        self.edad_label.grid(row=1, column=0, pady=5, sticky="w")

        self.genero_label = ctk.CTkLabel(self.detalle_frame, text="Género:", anchor="w")
        self.genero_label.grid(row=2, column=0, pady=5, sticky="w")

        self.avatar_label = ctk.CTkLabel(self.detalle_frame, text="[Sin avatar]", anchor="w")
        self.avatar_label.grid(row=3, column=0, pady=10, sticky="w")

    def actualizar_lista_usuarios(self, usuarios, on_seleccionar_callback):
        for widget in self.lista_usuarios_scrollable.winfo_children():
            widget.destroy()

        for i, usuario in enumerate(usuarios):
            btn = ctk.CTkButton(
                self.lista_usuarios_scrollable,
                text=usuario.nombre,
                command=lambda idx=i: on_seleccionar_callback(idx)
            )
            btn.pack(fill="x", padx=5, pady=2)

    def mostrar_detalles_usuario(self, usuario):
        if usuario is None:
            self.nombre_label.configure(text="Nombre:")
            self.edad_label.configure(text="Edad:")
            self.genero_label.configure(text="Género:")
            self.avatar_label.configure(text="[Sin avatar]")
            return

        self.nombre_label.configure(text=f"Nombre: {usuario.nombre}")
        self.edad_label.configure(text=f"Edad: {usuario.edad}")
        self.genero_label.configure(text=f"Género: {usuario.genero}")

        if usuario.avatar:
            self.avatar_label.configure(text=f"Avatar: {usuario.avatar}")
        else:
            self.avatar_label.configure(text="[Sin avatar]")
