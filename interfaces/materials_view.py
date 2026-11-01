import customtkinter as ctk
from tkinter import messagebox

from modules.materials import cadastrar_material, listar_materiais
from modules.projects import listar_projetos


def abrir_materiais():

    janela = ctk.CTk()
    janela.title("ArqueoLab - Materiais Arqueológicos")
    janela.geometry("800x650")

    titulo = ctk.CTkLabel(
        janela,
        text="Materiais Arqueológicos",
        font=("Arial", 24, "bold")
    )
    titulo.pack(pady=20)

    campo_nome = ctk.CTkEntry(
        janela,
        placeholder_text="Nome do material",
        width=300
    )
    campo_nome.pack(pady=8)

    campo_tipo = ctk.CTkEntry(
        janela,
        placeholder_text="Tipo do material",
        width=300
    )
    campo_tipo.pack(pady=8)

    campo_descricao = ctk.CTkEntry(
        janela,
        placeholder_text="Descrição",
        width=300
    )
    campo_descricao.pack(pady=8)

    campo_data = ctk.CTkEntry(
        janela,
        placeholder_text="Data da descoberta (DD/MM/AAAA)",
        width=300
    )
    campo_data.pack(pady=8)

    projetos = listar_projetos()

    opcoes_projetos = [
        f"{projeto[0]} - {projeto[1]}"
        for projeto in projetos
    ]

    seletor_projeto = ctk.CTkComboBox(
        janela,
        values=opcoes_projetos,
        width=300
    )
    seletor_projeto.pack(pady=8)

    lista = ctk.CTkTextbox(
        janela,
        width=650,
        height=180
    )
    lista.pack(pady=15)

    def atualizar_lista():

        lista.delete("1.0", "end")

        materiais = listar_materiais()

        for material in materiais:
            lista.insert(
                "end",
                f"ID: {material[0]}\n"
                f"Nome: {material[1]}\n"
                f"Tipo: {material[2]}\n"
                f"Descrição: {material[3]}\n"
                f"Data: {material[4]}\n"
                f"Projeto: {material[5]}\n\n"
            )

    def salvar_material():

        nome = campo_nome.get()
        tipo = campo_tipo.get()
        descricao = campo_descricao.get()
        data = campo_data.get()
        projeto_selecionado = seletor_projeto.get()

        if not nome or not tipo:
            messagebox.showwarning(
                "Atenção",
                "Preencha o nome e o tipo do material."
            )
            return

        projeto_id = None

        if projeto_selecionado:
            projeto_id = int(projeto_selecionado.split(" - ")[0])

        cadastrar_material(
            nome,
            tipo,
            descricao,
            data,
            projeto_id
        )

        messagebox.showinfo(
            "Sucesso",
            "Material cadastrado!"
        )

        campo_nome.delete(0, "end")
        campo_tipo.delete(0, "end")
        campo_descricao.delete(0, "end")
        campo_data.delete(0, "end")

        atualizar_lista()

    botao_salvar = ctk.CTkButton(
        janela,
        text="Cadastrar material",
        command=salvar_material
    )
    botao_salvar.pack(pady=10)

    atualizar_lista()

    janela.mainloop()