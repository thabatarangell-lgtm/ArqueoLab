
import customtkinter as ctk

from database.connection import criar_banco
from database.models import criar_tabelas

from interfaces.auth_view import TelaInicial
from interfaces.login_view import TelaLogin
from interfaces.register_view import TelaCadastro
from interfaces.projects_view import TelaCadastroProjeto

from modules.projects import listar_projetos_por_pesquisador


class ArqueoLab(ctk.CTk):

    def __init__(self):
        super().__init__()

        self.title("ArqueoLab | Sistema de Gestão Arqueológica")
        self.geometry("950x650")

        ctk.set_appearance_mode("light")
        ctk.set_default_color_theme("green")

        self.tela_atual = None

        self.mostrar_tela_inicial()

    def limpar_tela(self):
        if self.tela_atual:
            self.tela_atual.destroy()

    def mostrar_tela_inicial(self):
        self.limpar_tela()

        self.tela_atual = TelaInicial(
            self,
            self.abrir_login,
            self.abrir_cadastro
        )

        self.tela_atual.pack(fill="both", expand=True)

    def abrir_login(self):
        self.limpar_tela()

        self.tela_atual = TelaLogin(
            self,
            self.mostrar_tela_inicial,
            self.abrir_selecao_projeto
        )

        self.tela_atual.pack(fill="both", expand=True)

    def abrir_cadastro(self):
        self.limpar_tela()

        self.tela_atual = TelaCadastro(
            self,
            self.mostrar_tela_inicial
        )

        self.tela_atual.pack(fill="both", expand=True)

    def abrir_selecao_projeto(self, usuario):
        self.limpar_tela()

        self.tela_atual = ctk.CTkFrame(self)
        self.tela_atual.pack(fill="both", expand=True)

        ctk.CTkLabel(
            self.tela_atual,
            text=f"Bem-vindo(a), {usuario['nome']}!",
            font=("Arial", 28, "bold")
        ).pack(pady=30)

        ctk.CTkLabel(
            self.tela_atual,
            text="Selecione um dos seus projetos",
            font=("Arial", 16)
        ).pack(pady=10)

        projetos = listar_projetos_por_pesquisador(
            usuario["pesquisador_id"]
        )

        if projetos:
            for projeto in projetos:
                ctk.CTkButton(
                    self.tela_atual,
                    text=projeto[1],
                    width=350
                ).pack(pady=8)

        else:
            ctk.CTkLabel(
                self.tela_atual,
                text="Você ainda não possui projetos cadastrados."
            ).pack(pady=20)

        # Botão para cadastrar um novo projeto
        ctk.CTkButton(
            self.tela_atual,
            text="+ Novo Projeto",
            width=250,
            height=40,
            command=lambda: self.abrir_cadastro_projeto(usuario)
        ).pack(pady=20)

        # Botão para sair
        ctk.CTkButton(
            self.tela_atual,
            text="Sair da conta",
            fg_color="gray",
            command=self.mostrar_tela_inicial
        ).pack(pady=15)

    def abrir_cadastro_projeto(self, usuario):
        self.limpar_tela()

        self.tela_atual = TelaCadastroProjeto(
            self,
            usuario,
            lambda: self.abrir_selecao_projeto(usuario)
        )

        self.tela_atual.pack(fill="both", expand=True)


def iniciar_sistema():
    criar_banco()
    criar_tabelas()

    app = ArqueoLab()
    app.mainloop()


if __name__ == "__main__":
    iniciar_sistema()
