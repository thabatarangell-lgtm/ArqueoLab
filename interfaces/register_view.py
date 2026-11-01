import customtkinter as ctk
from tkinter import messagebox

from modules.auth import cadastrar_usuario


class TelaCadastro(ctk.CTkFrame):

    def __init__(self, master, voltar_callback):
        super().__init__(master)

        self.voltar_callback = voltar_callback

        self.criar_interface()

    def criar_interface(self):

        botao_voltar = ctk.CTkButton(
            self,
            text="← Voltar",
            command=self.voltar_callback,
            width=120
        )
        botao_voltar.pack(anchor="w", padx=25, pady=15)

        titulo = ctk.CTkLabel(
            self,
            text="Criar conta",
            font=("Arial", 28, "bold")
        )
        titulo.pack(pady=20)

        self.nome = ctk.CTkEntry(
            self,
            placeholder_text="Nome completo",
            width=350
        )
        self.nome.pack(pady=8)

        self.email = ctk.CTkEntry(
            self,
            placeholder_text="E-mail",
            width=350
        )
        self.email.pack(pady=8)

        self.especialidade = ctk.CTkEntry(
            self,
            placeholder_text="Especialidade arqueológica",
            width=350
        )
        self.especialidade.pack(pady=8)

        self.senha = ctk.CTkEntry(
            self,
            placeholder_text="Senha",
            show="*",
            width=350
        )
        self.senha.pack(pady=8)

        self.confirmar_senha = ctk.CTkEntry(
            self,
            placeholder_text="Confirmar senha",
            show="*",
            width=350
        )
        self.confirmar_senha.pack(pady=8)

        botao = ctk.CTkButton(
            self,
            text="Criar minha conta",
            width=250,
            command=self.cadastrar
        )
        botao.pack(pady=25)

    def cadastrar(self):

        nome = self.nome.get().strip()
        email = self.email.get().strip().lower()
        especialidade = self.especialidade.get().strip()
        senha = self.senha.get()
        confirmar = self.confirmar_senha.get()

        if not nome or not email or not senha:
            messagebox.showwarning(
                "Atenção",
                "Preencha todos os campos obrigatórios."
            )
            return

        if "@" not in email or "." not in email.split("@")[-1]:
            messagebox.showwarning(
                "Atenção",
                "Informe um e-mail válido."
            )
            return

        if len(senha) < 8:
            messagebox.showwarning(
                "Atenção",
                "A senha deve ter pelo menos 8 caracteres."
            )
            return

        if senha != confirmar:
            messagebox.showwarning(
                "Atenção",
                "As senhas não coincidem."
            )
            return

        sucesso, mensagem = cadastrar_usuario(
            nome,
            email,
            especialidade,
            senha
        )

        if sucesso:
            messagebox.showinfo("Sucesso", mensagem)
            self.voltar_callback()
        else:
            messagebox.showerror("Erro", mensagem)