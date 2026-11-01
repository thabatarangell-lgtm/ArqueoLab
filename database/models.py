from database.connection import conectar


def criar_tabelas():
    conexao = conectar()
    cursor = conexao.cursor()

    # Tabela de pesquisadores
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS pesquisadores (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            email TEXT UNIQUE,
            especialidade TEXT
        )
    """)

    # Tabela de sítios arqueológicos
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS sitios (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            localizacao TEXT,
            descricao TEXT
        )
    """)

    # Tabela de projetos
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS projetos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            descricao TEXT,
            pesquisador_id INTEGER,
            sitio_id INTEGER,

            FOREIGN KEY (pesquisador_id)
                REFERENCES pesquisadores(id),

            FOREIGN KEY (sitio_id)
                REFERENCES sitios(id)
       )
    """)

    conexao.commit()
    conexao.close()

    print("Tabelas criadas com sucesso!")