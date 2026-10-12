import pandas as pd  # Importa a biblioteca Pandas para manipulação de dados

# Define a URL do arquivo CSV com os dados do Titanic
url = "https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv"

# Lê os dados do arquivo CSV e cria um DataFrame
df_titanic = pd.read_csv(url)

# Cria a coluna "Age_log" aplicando uma função lambda aos valores da coluna "Age"
# A função lambda retorna o próprio valor recebido, sem realizar alterações
df_titanic["Age_log"] = df_titanic["Age"].apply(lambda x: x)

# Normaliza os valores da coluna "Fare" para uma escala entre 0 e 1, usando a técnica Min-Max
df_titanic["Fare_normalized"] = (
    (df_titanic["Fare"] - df_titanic["Fare"].min()) /
    (df_titanic["Fare"].max() - df_titanic["Fare"].min())
)

# Exibe o DataFrame completo com as novas colunas
print(df_titanic)
