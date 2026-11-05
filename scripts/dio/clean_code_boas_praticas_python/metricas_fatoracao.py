import pandas as pd                 # Manipulação e análise de dados
import numpy as np                  # Operações matemáticas e numéricas
import matplotlib.pyplot as plt    # Criação de gráficos
import seaborn as sns              # Visualização de dados estatísticos

from sklearn.model_selection import train_test_split  # Separação dos dados para treino e teste
from sklearn.linear_model import LinearRegression      # Modelo de regressão linear

url = "https://raw.githubusercontent.com/ageron/handson-ml/master/datasets/housing/housing.csv"

df = pd.read_csv(url)  # Carrega o arquivo CSV da URL e cria um DataFrame
df = df.dropna()  # Remove as linhas que possuem valores ausentes (NaN)

x = df.drop("median_house_value", axis=1)  # Cria a variável X com as características dos imóveis, removendo a coluna que queremos prever
x = pd.get_dummies(x)  # Converte as colunas categóricas em colunas numéricas (0 e 1), permitindo que sejam utilizadas pelo modelo de Machine Learning
y = df["median_house_value"]  # Cria a variável Y com os valores dos imóveis que o modelo deverá aprender a prever