import customtkinter as ctk
from tkinter import messagebox

from modules.auth import fazer_login


class TelaLogin(ctk.CTkFrame):

    def __init__(self, master, voltar_callback, login_sucesso_callback):
        super().__init__(master)

        self.voltar_callback = voltar_callback
        self.login_sucesso_callback = login_sucesso_callback

        self.criar_interface()

    def criar_interface(self):

        titulo = ctk.CTkLabel(
            self,
            text="Entrar no ArqueoLab",
            font=("Arial", 28, "bold")
        )
        titulo.pack(pady=30)

        self.email = ctk.CTkEntry(
            self,
            placeholder_text="E-mail",
            width=300
        )
        self.email.pack(pady=10)

        self.senha = ctk.CTkEntry(
            self,
            placeholder_text="Senha",
            show="*",
            width=300
        )
        self.senha.pack(pady=10)

        botao = ctk.CTkButton(
            self,
            text="Entrar",
            command=self.entrar
        )
        botao.pack(pady=20)

        voltar = ctk.CTkButton(
            self,
            text="Voltar",
            command=self.voltar_callback,
            fg_color="gray"
        )
        voltar.pack(pady=10)

    def entrar(self):

        email = self.email.get().strip()
        senha = self.senha.get()

        if not email or not senha:
            messagebox.showwarning(
                "Atenção",
                "Preencha o e-mail e a senha."
            )
            return

        usuario = fazer_login(email, senha)

        if usuario:
            messagebox.showinfo(
                "Login realizado",
                f"Bem-vindo(a), {usuario['nome']}!"
            )

            self.login_sucesso_callback(usuario)

        else:
            messagebox.showerror(
                "Erro",
                "E-mail ou senha incorretos."
            )