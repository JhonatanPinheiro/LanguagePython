
import pandas as pd  # Importa a biblioteca Pandas para manipulação de dados
import matplotlib.pyplot as plt  # Importa o módulo Pyplot para criar gráficos
import seaborn as sns  # Importa a biblioteca Seaborn para visualização de dados
import plotly.express as px  # Importa o Plotly Express para criar gráficos interativos
from pathlib import Path  # Permite manipular caminhos de arquivos e pastas


def caminho_principal():  # Define a função que retorna o caminho do relatório
    pasta_atual = Path(__file__).resolve().parent  # Define a pasta onde está o arquivo Python
    caminho_relatorio = pasta_atual / "relatorio_dataframe_restaurante.csv"  # Define o caminho do arquivo CSV
    return caminho_relatorio  # Retorna o caminho completo do relatório


def pipeline_resturante():  # Define a função responsável por carregar e processar os dados
    URL = "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/tips.csv"  # Define a URL do arquivo CSV

    df_restaurante = pd.read_csv(URL)  # Lê os dados do CSV e cria um DataFrame
    print(df_restaurante)  # Exibe os dados carregados no terminal

    relatorio_df_restaurante = df_restaurante.rename(columns={  # Renomeia as colunas para português
        "total_bill": "Total da Conta",  # Renomeia a coluna do valor total da conta
        "tip": "Gorjeta",  # Renomeia a coluna das gorjetas
        "sex": "Sexo",  # Renomeia a coluna do sexo
        "smoker": "Fumante",  # Renomeia a coluna que indica se a pessoa fuma
        "day": "Dia",  # Renomeia a coluna do dia
        "time": "Período",  # Renomeia a coluna do período da refeição
        "size": "Quantidade de Pessoas"  # Renomeia a coluna da quantidade de pessoas
    })

    caminho_relatorio = caminho_principal()  # Obtém o caminho para salvar o relatório
    relatorio_df_restaurante.to_csv(caminho_relatorio, index=False)  # Salva o DataFrame em CSV sem o índice

    print("Relatório salvo em:", caminho_relatorio)  # Exibe o caminho onde o relatório foi salvo

    return df_restaurante  # Retorna os dados originais para gerar os gráficos


def gerar_grafico_plt(df_restaurante):  # Define a função que cria um gráfico com Matplotlib
    plt.scatter(df_restaurante["total_bill"], df_restaurante["tip"])  # Cria o gráfico de dispersão entre conta e gorjeta
    plt.title("Valor da conta x Gorjeta")  # Define o título do gráfico
    plt.xlabel("Valor da conta")  # Define o nome do eixo X
    plt.ylabel("Gorjeta")  # Define o nome do eixo Y
    plt.show()  # Exibe o gráfico


def gerar_grafico_sns(df_restaurante):  # Define a função que cria um gráfico com Seaborn
    sns.scatterplot(data=df_restaurante, x="total_bill", y="tip")  # Cria o gráfico usando as colunas da conta e da gorjeta
    plt.show()  # Exibe o gráfico


def gerar_grafico_px(df_restaurante):  # Define a função que cria um gráfico interativo com Plotly
    figura = px.scatter(df_restaurante, x="total_bill", y="tip", color="day", title="Relacao entre conta e gorjeta")  # Cria o gráfico, usando o dia para diferenciar as cores
    figura.show(renderer="browser")  # Abre o gráfico no navegador padrão


df_restaurante = pipeline_resturante()  # Executa o pipeline e armazena os dados retornados
gerar_grafico_plt(df_restaurante)  # Gera o gráfico usando Matplotlib
gerar_grafico_sns(df_restaurante)  # Gera o gráfico usando Seaborn
gerar_grafico_px(df_restaurante)  # Gera o gráfico interativo usando Plotly
