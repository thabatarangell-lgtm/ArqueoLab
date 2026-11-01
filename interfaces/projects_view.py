import customtkinter as ctk
from tkinter import messagebox

from modules.projects import cadastrar_projeto
from modules.sites import listar_sitios


class TelaCadastroProjeto(ctk.CTkFrame):

    def __init__(self, master, usuario, voltar_callback):
        super().__init__(master)

        self.usuario = usuario
        self.voltar_callback = voltar_callback

        self.criar_interface()

    def criar_interface(self):

        titulo = ctk.CTkLabel(
            self,
            text="Novo Projeto Arqueológico",
            font=("Arial", 26, "bold")
        )
        titulo.pack(pady=30)

        self.campo_nome = ctk.CTkEntry(
            self,
            placeholder_text="Nome do projeto",
            width=350
        )
        self.campo_nome.pack(pady=10)

        self.campo_descricao = ctk.CTkEntry(
            self,
            placeholder_text="Descrição do projeto",
            width=350
        )
        self.campo_descricao.pack(pady=10)

        sitios = listar_sitios()

        self.opcoes_sitios = [
            f"{s[0]} - {s[1]}" for s in sitios
        ]

        self.seletor_sitio = ctk.CTkComboBox(
            self,
            values=self.opcoes_sitios,
            width=350
        )
        self.seletor_sitio.pack(pady=10)

        if self.opcoes_sitios:
            self.seletor_sitio.set(self.opcoes_sitios[0])

        botao = ctk.CTkButton(
            self,
            text="Cadastrar projeto",
            command=self.salvar
        )
        botao.pack(pady=20)

        voltar = ctk.CTkButton(
            self,
            text="Voltar",
            fg_color="gray",
            command=self.voltar_callback
        )
        voltar.pack(pady=10)

    def salvar(self):

        nome = self.campo_nome.get().strip()
        descricao = self.campo_descricao.get().strip()
        sitio = self.seletor_sitio.get()

        if not nome:
            messagebox.showwarning(
                "Atenção",
                "Informe o nome do projeto."
            )
            return

        if not sitio:
            messagebox.showwarning(
                "Atenção",
                "Selecione um sítio arqueológico."
            )
            return

        sitio_id = int(sitio.split(" - ")[0])

        cadastrar_projeto(
            nome,
            descricao,
            self.usuario["pesquisador_id"],
            sitio_id
        )

        messagebox.showinfo(
            "Sucesso",
            "Projeto cadastrado com sucesso!"
        )

        self.voltar_callback()