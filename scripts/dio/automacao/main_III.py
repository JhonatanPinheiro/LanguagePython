# Capturar dados da API
# Tratar os dados
# Inserir esses dados dentro de um banco de dados

import sqlite3  # Importa a biblioteca para trabalhar com SQLite
import logging # Permite registrar mensagens de log
from main_III_cron import dt_execucao_script
from main_III_database import criar_database
from main_III_path import caminho_principal
from main_III_logger import execucao_log

#dt_execucao_script()
execucao_log() # Inicia o registro dos logs

caminho_banco = caminho_principal()
criar_database()

conn = sqlite3.connect(caminho_banco)  # Abre a conexão com o banco
cursor = conn.cursor()  # Cria o cursor para executar comandos SQL


lista_usuarios = {
    "nome": ["Jhonatan", "Maria", "Patricia", "Layara"],
    "idade": [27, 19, 29, 27]
}

for i in range(len(lista_usuarios["nome"])):
    nome = lista_usuarios["nome"][i]
    idade = lista_usuarios["idade"][i]
    
    # Verifica se o nome e a idade já estão cadastrados
    cursor.execute(
        "SELECT 1 FROM usuarios WHERE nome = ? AND idade = ?",
        (nome,idade)
    )
    
    if cursor.fetchone() is None: # Se não encontrar duplicidade
        cursor.execute("INSERT INTO usuarios (nome, idade) VALUES (?, ?)",
                       (nome, idade)
        )
        
        print(f"Usuarios: {nome}, idade: {idade} , inserido com sucesso!")
        
    else:
        print(f"Usuarios: {nome}, idade: {idade} , Erro! Usuário já cadastrado/Existente no banco de dados")
    
    conn.commit() # Salva as inserções realizadas
    
    
conn.commit()


print("\nUsuarios inserido no banco de dados com sucesso!\n")

print(100*'-')
print("Resultado da Consulta dos dados:")
cursor.execute("""SELECT * FROM usuarios ORDER BY nome, idade ASC;""")
dados_usuarios = cursor.fetchall()

for dado_usuario in dados_usuarios:
    print(dado_usuario)


conn.commit()
print(100*'-')


conn.close()  # Fecha a conexão com o banco






