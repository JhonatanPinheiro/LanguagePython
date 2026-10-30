import pandas as pd  # Importa a biblioteca Pandas para manipulação e análise de dados

# Cria um dicionário com os produtos e seus respectivos preços
dados = {
    "produto": ["Notbook","Notbook", "Mouse", "Teclado"],  # Lista com os nomes dos produtos
    "preco": [2000,4000, 120, 200]  # Lista com os preços dos produtos
}

df = pd.DataFrame(dados)  # Converte o dicionário em um DataFrame (tabela de dados)
print(dados)  # Exibe o dicionário original, não o DataFrame

# Abre o arquivo CSV e carrega seus dados em um DataFrame
df_relatorio_dados_em_csv = pd.read_csv("dados.csv")

# Seleciona a coluna "produto" do DataFrame carregado do arquivo CSV
df_produto = df_relatorio_dados_em_csv["produto"]

# Seleciona a coluna "preco" do DataFrame carregado do arquivo CSV
df_preco = df_relatorio_dados_em_csv["preco"]

# Conta a quantidade de valores não nulos na coluna de produtos
quantidade_produto_df = df_produto.count()

# Conta a quantidade de valores não nulos na coluna de preços
quantidade_preco_df = df_preco.count()

# Exibe a quantidade de valores encontrados em cada coluna
print("Quantidade de Produto:", quantidade_produto_df)
print("Quantidade de Preco:", quantidade_preco_df)

# Exibe os valores das colunas de produtos e preços
print(df_produto, df_preco)

# Apresenta estatísticas descritivas das colunas numéricas do DataFrame df
print(df.describe())

# Estou agrupando as infomacoes do produto e já apllicando a media no valor (2 Notbook / 2) -> Funcao que faz essa media mean
print(df.groupby("produto").mean())
