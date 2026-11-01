import customtkinter as ctk

class TelaInicial(ctk.CTkFrame):

    def __init__(self, master, abrir_login, abrir_cadastro):
        super().__init__(master)

        self.abrir_login = abrir_login
        self.abrir_cadastro = abrir_cadastro

        self.criar_interface()

    def criar_interface(self):

        titulo = ctk.CTkLabel(
            self,
            text="ARQUEOLAB",
            font=("Arial", 36, "bold")
        )
        titulo.pack(pady=(100, 10))

        subtitulo = ctk.CTkLabel(
            self,
            text="Sistema de Gestão Arqueológica",
            font=("Arial", 16)
        )
        subtitulo.pack(pady=10)

        botao_entrar = ctk.CTkButton(
            self,
            text="Entrar",
            width=250,
            height=45,
            command=self.abrir_login
        )
        botao_entrar.pack(pady=(40, 10))

        botao_cadastro = ctk.CTkButton(
            self,
            text="Criar conta",
            width=250,
            height=45,
            command=self.abrir_cadastro
        )
        botao_cadastro.pack(pady=10)