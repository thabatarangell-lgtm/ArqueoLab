import customtkinter as ctk
from tkinter import messagebox

from modules.researchers import (
    cadastrar_pesquisador,
    listar_pesquisadores
)


class TelaPesquisadores(ctk.CTkFrame):

    def __init__(self, master, voltar_callback):
        super().__init__(master)

        self.voltar_callback = voltar_callback

        self.criar_interface()

    def criar_interface(self):

        botao_voltar = ctk.CTkButton(
            self,
            text="← Voltar ao menu",
            command=self.voltar_callback,
            width=150
        )
        botao_voltar.pack(anchor="w", padx=25, pady=15)

        titulo = ctk.CTkLabel(
            self,
            text="Cadastro de Pesquisadores",
            font=("Arial", 26, "bold")
        )
        titulo.pack(pady=20)

        self.nome = ctk.CTkEntry(
            self,
            placeholder_text="Nome do pesquisador",
            width=350
        )
        self.nome.pack(pady=10)

        self.email = ctk.CTkEntry(
            self,
            placeholder_text="E-mail",
            width=350
        )
        self.email.pack(pady=10)

        self.especialidade = ctk.CTkEntry(
            self,
            placeholder_text="Especialidade",
            width=350
        )
        self.especialidade.pack(pady=10)

        botao = ctk.CTkButton(
            self,
            text="Cadastrar pesquisador",
            command=self.cadastrar
        )
        botao.pack(pady=15)

        self.lista = ctk.CTkTextbox(
            self,
            width=600,
            height=200
        )
        self.lista.pack(pady=15)

        self.atualizar_lista()

    def cadastrar(self):

        nome = self.nome.get().strip()
        email = self.email.get().strip()
        especialidade = self.especialidade.get().strip()

        if not nome:
            messagebox.showwarning(
                "Atenção",
                "O nome é obrigatório!"
            )
            return

        if not email or "@" not in email:
            messagebox.showwarning(
                "Atenção",
                "Informe um e-mail válido!"
            )
            return

        cadastrar_pesquisador(
            nome,
            email,
            especialidade
        )

        self.nome.delete(0, "end")
        self.email.delete(0, "end")
        self.especialidade.delete(0, "end")

        self.atualizar_lista()

    def atualizar_lista(self):

        self.lista.configure(state="normal")
        self.lista.delete("1.0", "end")

        pesquisadores = listar_pesquisadores()

        for pesquisador in pesquisadores:

            id, nome, email, especialidade = pesquisador

            self.lista.insert(
                "end",
                f"ID: {id}\n"
                f"Nome: {nome}\n"
                f"E-mail: {email}\n"
                f"Especialidade: {especialidade}\n"
                "-----------------------------\n"
            )

        self.lista.configure(state="disabled")