from database.connection import conectar


def cadastrar_projeto(nome, descricao, pesquisador_id, sitio_id):

    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("""
        INSERT INTO projetos (
            nome,
            descricao,
            pesquisador_id,
            sitio_id
        )
        VALUES (?, ?, ?, ?)
    """, (nome, descricao, pesquisador_id, sitio_id))

    conexao.commit()
    conexao.close()

    print("Projeto cadastrado com sucesso!")


def listar_projetos():

    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("""
        SELECT
            projetos.id,
            projetos.nome,
            projetos.descricao,
            pesquisadores.nome,
            sitios.nome
        FROM projetos

        LEFT JOIN pesquisadores
        ON projetos.pesquisador_id = pesquisadores.id

        LEFT JOIN sitios
        ON projetos.sitio_id = sitios.id
    """)
    
    

    projetos = cursor.fetchall()

    conexao.close()

    return projetos

def listar_projetos_por_pesquisador(pesquisador_id):

    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("""
        SELECT id, nome, descricao
        FROM projetos
        WHERE pesquisador_id = ?
    """, (pesquisador_id,))

    projetos = cursor.fetchall()

    conexao.close()

    return projetos