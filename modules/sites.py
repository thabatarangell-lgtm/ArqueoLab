from database.connection import conectar


def cadastrar_sitio(nome, localizacao, descricao):

    conexao = conectar()
    cursor = conexao.cursor()

    try:
        cursor.execute("""
            INSERT INTO sitios (nome, localizacao, descricao)
            VALUES (?, ?, ?)
        """, (nome, localizacao, descricao))

        conexao.commit()

        print("Sítio cadastrado com sucesso!")
        return True

    except Exception as erro:
        print(f"Erro ao cadastrar sítio: {erro}")
        return False

    finally:
        conexao.close()


def listar_sitios():

    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("""
        SELECT id, nome, localizacao, descricao
        FROM sitios
    """)

    sitios = cursor.fetchall()

    conexao.close()

    return sitios