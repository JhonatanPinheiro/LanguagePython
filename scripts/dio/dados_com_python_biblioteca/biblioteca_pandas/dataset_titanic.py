import pandas as pd

url = "https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv"

df_titanic = pd.read_csv(url)

#print(df_titanic)

#print(df_titanic.head()) # Mostra apenas as primeiras linha do nosso dataframe

#print(df_titanic.info())  # Exibe informações gerais do DataFrame, como quantidade de linhas, colunas, valores não nulos e tipos de dados.
#print(df_titanic.describe())  # Exibe estatísticas descritivas das colunas numéricas, como contagem, média, desvio padrão, valor mínimo, máximo e quartis.

#print(df_titanic.isnull().sum())

# Remove as linhas que possuem pelo menos um valor ausente (NaN) e armazena o resultado em um novo DataFrame.
#df_titanic_limpo_valores_null = df_titanic.dropna(
# Exibe as primeiras 100 linhas do DataFrame após a remoção dos valores ausentes.
#print(df_titanic_limpo_valores_null.head(100))



df_titanic_age = df_titanic["Age"].fillna("Sem Idade Informada")  # Preenche os valores ausentes (NaN) da coluna "Age" com o texto "Sem Idade Informada" e armazena o resultado em uma nova Series.
print(df_titanic_age.isnull().sum())  # Conta e exibe quantos valores ausentes ainda existem após o preenchimento.
print(df_titanic_age)  # Exibe os valores da coluna "Age", incluindo o texto usado para substituir os valores ausentes.