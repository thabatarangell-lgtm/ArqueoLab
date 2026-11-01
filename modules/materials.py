from database.connection import conectar


def cadastrar_material(nome, tipo, descricao, data_descoberta, projeto_id):

    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("""
        INSERT INTO materiais (
            nome,
            tipo,
            descricao,
            data_descoberta,
            projeto_id
        )
        VALUES (?, ?, ?, ?, ?)
    """, (nome, tipo, descricao, data_descoberta, projeto_id))

    conexao.commit()
    conexao.close()

    print("Material cadastrado com sucesso!")


def listar_materiais():

    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("""
        SELECT
            materiais.id,
            materiais.nome,
            materiais.tipo,
            materiais.descricao,
            materiais.data_descoberta,
            projetos.nome
        FROM materiais
        LEFT JOIN projetos
        ON materiais.projeto_id = projetos.id
    """)

    materiais = cursor.fetchall()

    conexao.close()

    return materiais