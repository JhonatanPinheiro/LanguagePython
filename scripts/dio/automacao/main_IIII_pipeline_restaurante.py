import pandas as pd
from pathlib import Path  # Permite manipular caminhos de arquivos e pastas

def caminho_principal():
    pasta_atual = Path(__file__).resolve().parent  # Define a pasta do arquivo Python
    caminho_relatorio = pasta_atual / "relatorio_gorjetas.csv"  # Define o caminho do CSV
    return caminho_relatorio  # Retorna o caminho completo do relatório


def pipeline_resturante():
    URL = "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/tips.csv"

    df_restaurante = pd.read_csv(URL)  # Lê os dados do restaurante

    total_gorjetas = df_restaurante["tip"].sum()  # Soma todas as gorjetas

    # Cria um DataFrame com o total das gorjetas
    relatorio = pd.DataFrame({
        "total_gorjetas": [total_gorjetas]
    })

    caminho_relatorio = caminho_principal()  # Obtém o caminho para salvar o CSV
    relatorio.to_csv(caminho_relatorio, index=False)  # Salva sem o índice

    print("Pipeline executado com sucesso!")
    print("Arquivo salvo em:", caminho_relatorio)
    print("Total de gorjetas:", total_gorjetas)
    print(relatorio)


pipeline_resturante()  # Executa o pipeline