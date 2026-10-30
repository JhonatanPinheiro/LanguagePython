import sqlite3 
from main_III_path import caminho_principal

def criar_database():
    caminho_banco = caminho_principal() # Recebe o caminho retornado pela função
    conn = sqlite3.connect(caminho_banco) # Conecta ao banco; cria o arquivo se ele ainda não existir
    cursor = conn.cursor()  # Cria o cursor para executar comandos SQL

    # Cria a tabela somente se ela ainda não existir
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS usuarios (
        nome TEXT,
        idade INTEGER
    )
    """)
    
    conn.close()  # Fecha a conexão com o banco
    
    print("Banco e tabela criados com sucesso!")
    print("Caminho do banco:", caminho_banco, "\n")  # Exibe onde o banco foi criado
    
