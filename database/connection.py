import sqlite3
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
DATABASE_PATH = BASE_DIR / "storage" / "arqueolbase.db"

def conectar():
    conexao = sqlite3.connect(DATABASE_PATH)
    return conexao

def criar_banco():
    conexao = conectar()
    conexao.close()
    
    print("Banco de dados criado")
    
    