# Importa a biblioteca requests
import requests

# URL da API que será consultada
url = "https://pokeapi.co/api/v2/pokemon/pikachu"


# Faz uma requisição GET para a API
resposta = requests.get(url)

# Exibe o código de status da resposta
print(resposta.status_code)

# Exibe o conteúdo da resposta em formato de texto
print(resposta.text)



## Abrir o terminal do PowerShell e rodar esse comando para instalar essa biblioteca requests... C:\python314\python.exe -m pip install requests