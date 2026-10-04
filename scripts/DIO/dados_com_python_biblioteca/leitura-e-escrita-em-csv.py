# Importa a biblioteca csv
import csv


# Lista contendo os dados que serão gravados no arquivo CSV
dados = [

    # Cabeçalho do arquivo CSV
    ["nome", "idade", "cidade"],

    # Dados da primeira pessoa
    ["Ana", 25, "São Paulo"],

    # Dados da segunda pessoa
    ["Marla", 28, "Belo Horizonte"]
]


# Abre ou cria o arquivo pessoas.csv
with open(
    r"C:\Users\jhona\OneDrive\Documentos\Project GitHub\LanguagePython\scripts\dio\dados_com_python_biblioteca\pessoas.csv",
    "w",
    newline="",
    encoding="utf-8"
) as arquivo:

    # Função csv.writer() = cria um escritor para o arquivo CSV
    writer = csv.writer(arquivo)

    # Função writerows() = escreve várias linhas no arquivo
    writer.writerows(dados)


# Abre o arquivo pessoas.csv no modo leitura
with open(
    r"C:\Users\jhona\OneDrive\Documentos\Project GitHub\LanguagePython\scripts\dio\dados_com_python_biblioteca\pessoas.csv",
    "r",
    encoding="utf-8"
) as arquivo:

    # Função csv.reader() = cria um leitor para o arquivo CSV
    leitor = csv.reader(arquivo)

    # Percorre cada linha do arquivo
    for linha in leitor:

        # Exibe cada linha no terminal
        print(linha)