import customtkinter as ctk
from tkinter import messagebox

from modules.sites import (
    cadastrar_sitio,
    listar_sitios
)


class TelaSitios(ctk.CTkFrame):

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
            text="Cadastro de Sítios Arqueológicos",
            font=("Arial", 25, "bold")
        )
        titulo.pack(pady=20)

        self.nome = ctk.CTkEntry(
            self,
            placeholder_text="Nome do sítio",
            width=350
        )
        self.nome.pack(pady=8)

        self.localizacao = ctk.CTkEntry(
            self,
            placeholder_text="Localização",
            width=350
        )
        self.localizacao.pack(pady=8)

        self.descricao = ctk.CTkTextbox(
            self,
            width=350,
            height=100
        )
        self.descricao.pack(pady=8)

        botao = ctk.CTkButton(
            self,
            text="Cadastrar sítio",
            command=self.cadastrar
        )
        botao.pack(pady=15)

        self.lista = ctk.CTkTextbox(
            self,
            width=650,
            height=220
        )
        self.lista.pack(pady=15)

        self.atualizar_lista()

    def cadastrar(self):

        nome = self.nome.get().strip()
        localizacao = self.localizacao.get().strip()
        descricao = self.descricao.get("1.0", "end").strip()

        if not nome or not localizacao:
            messagebox.showwarning(
                "Atenção",
                "Nome e localização são obrigatórios!"
            )
            return

        sucesso = cadastrar_sitio(
            nome,
            localizacao,
            descricao
        )

        if sucesso:
            messagebox.showinfo(
                "Sucesso",
                "Sítio cadastrado!"
            )

            self.nome.delete(0, "end")
            self.localizacao.delete(0, "end")
            self.descricao.delete("1.0", "end")

            self.atualizar_lista()

    def atualizar_lista(self):

        self.lista.configure(state="normal")
        self.lista.delete("1.0", "end")

        sitios = listar_sitios()

        for sitio in sitios:

            id, nome, localizacao, descricao = sitio

            self.lista.insert(
                "end",
                f"ID: {id}\n"
                f"Nome: {nome}\n"
                f"Localização: {localizacao}\n"
                f"Descrição: {descricao}\n"
                "-----------------------------\n"
            )

        self.lista.configure(state="disabled")