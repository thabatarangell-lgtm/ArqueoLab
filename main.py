from database.connection import criar_banco
from database.models import criar_tabelas

from interfaces.researcher_view import TelaPesquisadores
from interfaces.sites_view import TelaSitios


def iniciar_sistema():

    criar_banco()
    criar_tabelas()

    print("\n===== ARQUEOLAB =====")
    print("1 - Pesquisadores")
    print("2 - Sítios arqueológicos")

    opcao = input("\nEscolha um módulo: ")

    if opcao == "1":
        app = TelaPesquisadores()
        app.mainloop()

    elif opcao == "2":
        app = TelaSitios()
        app.mainloop()

    else:
        print("Opção inválida!")


if __name__ == "__main__":
    iniciar_sistema()