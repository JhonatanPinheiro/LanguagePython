import sqlite3  # Importa a biblioteca sqlite3 para trabalhar com banco SQLite


# Criando ou conectando ao banco
# Se o arquivo dados.db não existir, o Python cria automaticamente.
# O banco será criado exatamente no caminho informado abaixo.
conexao = sqlite3.connect(
    r"C:\Users\jhona\OneDrive\Documentos\Project GitHub\LanguagePython\scripts\dio\dados_com_python_biblioteca\dados.db"
)


# Cria um cursor.
# O cursor é usado para executar comandos SQL no banco de dados.
cursor = conexao.cursor()


# Executa um comando SQL para criar a tabela usuarios.
# IF NOT EXISTS evita erro caso a tabela já exista.
cursor.execute("""
               CREATE TABLE IF NOT EXISTS usuarios(

                   nome TEXT,
                   idade INTEGER

               )
               """)


# Insere um usuário na tabela usuarios.
# Os ? são utilizados para receber os valores de forma segura.
cursor.execute("INSERT INTO usuarios VALUES (?,?)",
               ('Ana', 25)
               )


# Confirma e salva as alterações realizadas no banco de dados.
conexao.commit()


# Executa um comando SQL para buscar todos os registros da tabela usuarios.
cursor.execute("SELECT * FROM usuarios")


# Recupera todos os registros encontrados pelo SELECT.
# fetchall() retorna todos os registros encontrados.
dados = cursor.fetchall()


# Exibe os dados recuperados do banco.
print(dados)

