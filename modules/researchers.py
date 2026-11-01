from database.connection import conectar


def cadastrar_pesquisador(nome, email, especialidade):

    conexao = conectar()
    cursor = conexao.cursor()

    try:
        cursor.execute("""
            INSERT INTO pesquisadores
            (nome, email, especialidade)
            VALUES (?, ?, ?)
        """, (nome, email, especialidade))

        conexao.commit()

        print("Pesquisador cadastrado com sucesso!")

    except Exception as erro:
        print(f"Erro ao cadastrar pesquisador: {erro}")

    finally:
        conexao.close()


def listar_pesquisadores():

    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("""
        SELECT id, nome, email, especialidade
        FROM pesquisadores
    """)

    pesquisadores = cursor.fetchall()

    conexao.close()

    return pesquisadores