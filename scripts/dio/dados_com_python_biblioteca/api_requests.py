# Importa a biblioteca requests
import requests

# Importa a biblioteca json
import json


# URL da API que será consultada
url = "https://pokeapi.co/api/v2/pokemon/pikachu"


# Faz uma requisição GET para a API
resposta = requests.get(url)


# Converte a resposta da API para um objeto Python
dados = resposta.json()


# Abre ou cria o arquivo dados_api_pokemon.json
with open(
    r"C:\Users\jhona\OneDrive\Documentos\Project GitHub\LanguagePython\scripts\dio\dados_com_python_biblioteca\dados_api_pokemon.json",
    "w",
    encoding="utf-8"
) as arquivo:

    # Função json.dump() = grava os dados no arquivo JSON
    json.dump(dados, arquivo, indent=4)


# Exibe o código de status da resposta
print(resposta.status_code)


# Exibe o conteúdo da resposta em formato de texto
print(resposta.text)


# Para instalar a biblioteca requests no Python 3.14,
# execute no PowerShell:
# C:\python314\python.exe -m pip install requests