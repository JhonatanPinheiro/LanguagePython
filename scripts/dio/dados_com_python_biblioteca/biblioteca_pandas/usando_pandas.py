import pandas as pd

dados = {
    "produto": ["Notbook","Mouse","Teclado"],
    "preco": [3500,120,200]
}

df = pd.DataFrame(dados)
print(dados)

df.to_csv("dados.csv", index=False) #Criando um csv usando o pandas

df_relatorio_dados_em_csv = pd.read_csv("dados.csv") #Abrindo o arquivo e gerando o DataFrame
print(df_relatorio_dados_em_csv)