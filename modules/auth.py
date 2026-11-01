import hashlib
import secrets
import hmac

from database.connection import conectar


def gerar_hash_senha(senha, salt=None):

    if salt is None:
        salt = secrets.token_hex(16)

    hash_senha = hashlib.pbkdf2_hmac(
        "sha256",
        senha.encode("utf-8"),
        bytes.fromhex(salt),
        200000
    )

    return salt, hash_senha.hex()


def cadastrar_usuario(nome, email, especialidade, senha):

    conexao = conectar()
    cursor = conexao.cursor()

    try:
        salt, senha_hash = gerar_hash_senha(senha)

        cursor.execute("""
            INSERT INTO pesquisadores (
                nome, email, especialidade
            )
            VALUES (?, ?, ?)
        """, (nome, email, especialidade))

        pesquisador_id = cursor.lastrowid

        cursor.execute("""
            INSERT INTO usuarios (
                pesquisador_id, email, senha_hash
            )
            VALUES (?, ?, ?)
        """, (pesquisador_id, email, f"{salt}${senha_hash}"))

        conexao.commit()

        return True, "Conta criada com sucesso!"

    except Exception:
        conexao.rollback()
        return False, "Não foi possível criar a conta. Verifique se o e-mail já está cadastrado."

    finally:
        conexao.close()


def fazer_login(email, senha):

    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("""
        SELECT usuarios.id,
               usuarios.pesquisador_id,
               usuarios.senha_hash,
               pesquisadores.nome
        FROM usuarios
        JOIN pesquisadores
        ON usuarios.pesquisador_id = pesquisadores.id
        WHERE usuarios.email = ?
    """, (email,))

    usuario = cursor.fetchone()
    conexao.close()

    if usuario is None:
        return None

    try:
        salt, hash_original = usuario[2].split("$")

        _, hash_digitado = gerar_hash_senha(senha, salt)

        if hmac.compare_digest(hash_original, hash_digitado):
            return {
                "usuario_id": usuario[0],
                "pesquisador_id": usuario[1],
                "nome": usuario[3]
            }

    except (ValueError, TypeError):
        return None

    return None