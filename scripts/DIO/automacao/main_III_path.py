from pathlib import Path  # Permite manipular caminhos de arquivos e pastas

def caminho_principal():
    pasta_atual = Path(__file__).resolve().parent # Define a pasta onde este arquivo Python está localizado
    caminho_banco = pasta_atual / "dados.db" # Define o caminho completo do banco dentro da pasta automacao
    return caminho_banco  # Retorna o caminho para outros arquivos Python

def caminho_logs():
    pasta_atual = Path(__file__).resolve().parent
    pasta_logs = pasta_atual / "logs"
    return pasta_logs