# Limpe a coluna valor_venda: remova "R$", remova pontos, troque vírgula por ponto e converta para número com pd.to_numeric(errors="coerce")
# Converta a coluna data_venda para datetime com pd.to_datetime(format="mixed", dayfirst=True)
# Qual é a receita total? (soma dos valores numéricos)
# A vendedora Renata ficou com valor NaN. Por quê?
# Reposta: # Porque o valor original era "Não registrado", que não pode ser convertido, git add para número. O errors="coerce" transformou em NaN em vez de dar erro.

import pandas as pd
from datetime import datetime

df = pd.DataFrame({
    "vendedora": ["Lúcia", "Marta", "Lúcia", "Renata", "Marta"],
    "valor_venda": ["R$ 3.500,00", "R$ 1.200,50", "R$ 8.000,00", "Não registrado", "R$ 4.750,25"],
    "data_venda": ["15/01/2024", "20/01/2024", "2024-02-10", "05/03/2024", "March 15, 2024"]
})


df["valor_venda"] = df["valor_venda"].fillna(0).str.replace({"R$":"", ".":"", ",":"."}) #Realizando o ETL dos dados do dataframe da coluna valor_venda
# df["valor_venda"] = df["valor_venda"].apply(pd.to_numeric,errors="coerce")
df["valor_venda"] = pd.to_numeric(df["valor_venda"], errors="coerce").fillna(0)
df["data_venda"] = pd.to_datetime(df["data_venda"],format="mixed",errors="coerce",dayfirst=False)

df["receita_parcelado"] = df["valor_venda"].sum() / len(df)
df["quantidade_total_parcela"] = df["receita_parcelado"].count() / len(df)


receita_total = df["valor_venda"].sum()
total_quantidade_parcela = df["valor_venda"].count()


df.loc[len(df)] = {
    "vendedora":"Acumulado da Parcela",
    "valor_venda":0,
    "data_venda": f"Data Registro: {datetime.now():%d/%m/%Y %H:%M:%S}",
    "receita_parcelado": receita_total,
    "quantidade_total_parcela": total_quantidade_parcela

}


print(df)
# print(df.info())
# print(df["valor_venda"].sample(5))
