
import requests  # Importa a biblioteca para realizar requisições HTTP

URL = "https://api.agify.io/?name=ana"  # Define a URL da API

try:
    resposta = requests.get(URL, timeout=10)  # Faz a requisição com limite de espera de 10 segundos
    resposta.raise_for_status()  # Gera uma exceção se houver erro HTTP

    dados = resposta.json()  # Converte a resposta JSON em um objeto Python

except requests.exceptions.Timeout:  # Captura erros de tempo de espera
    print("Erro: a API excedeu os 10 segundos de espera.")

except requests.exceptions.HTTPError as erro:  # Captura erros HTTP, como 404, 429 ou 500
    if resposta.status_code == 429:  # Verifica se o limite de requisições foi atingido
        print("Limite de requisições atingido. Tente novamente mais tarde.")
        print("Resposta da API:", resposta.text)  # Exibe a mensagem enviada pela API
    else:
        print("Erro HTTP:", erro)  # Exibe os detalhes do erro HTTP
        print("Resposta da API:", resposta.text)  # Exibe o conteúdo retornado pela API

except requests.exceptions.ConnectionError:  # Captura erros de conexão
    print("Erro: não foi possível conectar à API.")

except requests.exceptions.RequestException as erro:  # Captura outros erros de requisição
    print("Erro na requisição:", erro)

except ValueError:  # Captura erros ao interpretar o JSON
    print("Erro: a resposta não contém um JSON válido.")

else:
    print("Consulta realizada com sucesso!")  # Executa somente se não houver exceções
    print("Dados recebidos:", dados)  # Exibe os dados retornados pela API
    print("Status HTTP:", resposta.status_code)  # Exibe o código de status HTTP
