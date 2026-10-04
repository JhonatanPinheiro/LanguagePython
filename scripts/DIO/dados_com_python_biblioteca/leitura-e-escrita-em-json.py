# Importa a biblioteca json
import json


# Dicionário contendo os dados que serão gravados no arquivo JSON
dados = {

    # Nome do usuário
    "nome": "Jhonatan",

    # Sobrenome do usuário
    "Sobrenome": "Pinheiro",

    # Cidade do usuário
    "Cidade": "Sumaré",

    # Ano de nascimento do usuário
    "Ano Nascimento": "1999"
}


# Abre ou cria o arquivo usuario.json
with open(
    r"C:\Users\jhona\OneDrive\Documentos\Project GitHub\LanguagePython\scripts\dio\dados_com_python_biblioteca\usuario.json",
    "w",
    encoding="utf-8"
) as arquivo:

    # Função json.dump() = grava os dados no arquivo JSON
    json.dump(dados, arquivo)


# Abre o arquivo usuario.json no modo leitura
with open(
    r"C:\Users\jhona\OneDrive\Documentos\Project GitHub\LanguagePython\scripts\dio\dados_com_python_biblioteca\usuario.json",
    "r",
    encoding="utf-8"
) as arquivo:

    # Função json.load() = lê os dados do arquivo JSON
    dados = json.load(arquivo)

    # Exibe os dados no terminal
    print(dados)