import pandas as pd  # Importa a biblioteca Pandas
from pathlib import Path  # Importa Path para manipular caminhos de arquivos
import openpyxl

def caminho_principal_clientes_crm():  # Define a função que retorna o caminho do arquivo CSV
    pasta_atual = Path(__file__).resolve().parent  # Define a pasta onde está o arquivo Python
    caminho_relatorio = pasta_atual / "clientes_crm.csv"  # Define o caminho do arquivo CSV
    return caminho_relatorio  # Retorna o caminho completo do arquivo

def caminho_principal_interacoes_cliente():  # Define a função que retorna o caminho do arquivo Excel
    pasta_atual = Path(__file__).resolve().parent  # Define a pasta onde está o arquivo Python
    caminho_relatorio = pasta_atual / "interacoes_clientes.xlsx"  # Define o caminho do arquivo Excel
    return caminho_relatorio  # Retorna o caminho completo do arquivo


# Importar as bases de dados
df_clientes_cr = pd.read_csv(caminho_principal_clientes_crm())  # Lê os dados do CSV
df_interacoes_clientes = pd.read_excel(caminho_principal_interacoes_cliente())  # Lê os dados do Excel

df_clientes_cr_tratada = df_clientes_cr.copy()  # Cria uma cópia dos dados originais
df_interacoes_clientes_tratada = df_interacoes_clientes.copy()  # Cria uma cópia dos dados originais

# Tratando as colunas selecionadas para um padrão df_clientes_cr_tratada
df_clientes_cr_tratada[["segmento cliente", "status cliente", "canal aquisicao"]] = (df_clientes_cr_tratada[["segmento cliente", "status cliente", "canal aquisicao"]].apply(lambda coluna: coluna.astype("string").str.strip().str.upper()))
df_clientes_cr_tratada[["nome","email","segmento cliente","status cliente","canal aquisicao"]] = df_clientes_cr_tratada[["nome","email","segmento cliente","status cliente","canal aquisicao"]].fillna("NAO INFORMADO")
df_clientes_cr_tratada[["data cadastro","ultima compra data"]]= df_clientes_cr_tratada[["data cadastro","ultima compra data"]].fillna("-")
df_clientes_cr_tratada["valor total"] = df_clientes_cr_tratada["valor total"].str.replace("R$", "", regex=False)
df_clientes_cr_tratada["valor total"] = df_clientes_cr_tratada["valor total"].str.replace(".", "", regex=False)
df_clientes_cr_tratada["valor total"] = df_clientes_cr_tratada["valor total"].str.replace(",", ".", regex=False)
df_clientes_cr_tratada["valor total"] = df_clientes_cr_tratada["valor total"].fillna(0)
df_clientes_cr_tratada["idade"] = df_clientes_cr_tratada["idade"].str.strip()
df_clientes_cr_tratada[["valor total", "idade"]] = (df_clientes_cr_tratada[["valor total", "idade"]].apply(pd.to_numeric, errors="coerce"))


# Tratando as colunas selecionadas para um padrão df_interacoes_clientes_tratada
df_interacoes_clientes_tratada[["canal interacao", "tipo interacao", "satisfacao cliente", "status resolucao"]] = (df_interacoes_clientes_tratada[["canal interacao", "tipo interacao", "satisfacao cliente", "status resolucao"]].apply(lambda coluna: coluna.astype("string").str.strip().str.upper()))
df_interacoes_clientes_tratada[["canal interacao","tipo interacao","status resolucao"]] = df_interacoes_clientes_tratada[["canal interacao","tipo interacao","status resolucao"]].fillna("NAO INFORMADO")
df_interacoes_clientes_tratada[["data interacao","duracao minutos","satisfacao cliente"]]= df_interacoes_clientes_tratada[["data interacao","duracao minutos","satisfacao cliente"]].fillna("-")



df_clientes_cr_tratada['valor total'] = df_clientes_cr_tratada.groupby('segmento cliente')['valor total'].transform(lambda x: x.fillna(x.median()))  # Preenche valores ausentes com a mediana de cada segmento
df_clientes_cr_tratada['idade'] = df_clientes_cr_tratada.groupby('canal aquisicao')['idade'].transform(lambda x: x.fillna(x.median()))  # Preenche idades ausentes com a mediana de cada canal
#------------------------------------------------------------------------------------------------------------------------------------------------------------------#

# print(df_clientes_cr_tratada[["valor total", "idade"]].sample(10)) #Vendo os dados (10 registros) do dataframe de forma aleatoria
# print(df_clientes_cr_tratada.isna().sum()) # Verificando qtd dos null em um dataframe
# print(df_clientes_cr_tratada)
# print(df_clientes_cr_tratada["data cadastro"].sample(10))
# print(df_clientes_cr_tratada["ultima compra data"].sample(10))

df_clientes_cr_tratada["data cadastro"] = pd.to_datetime(df_clientes_cr_tratada["data cadastro"],format="mixed", errors="coerce", dayfirst=True)
df_clientes_cr_tratada["ultima compra data"] = pd.to_datetime(df_clientes_cr_tratada["ultima compra data"], format="mixed", errors="coerce", dayfirst=True)


df_interacoes_clientes_tratada["data interacao"] = df_interacoes_clientes_tratada["data interacao"].str.strip()
df_interacoes_clientes_tratada["data interacao"] = pd.to_datetime(df_interacoes_clientes_tratada["data interacao"], format="mixed", errors="coerce", dayfirst=True)

# df_clientes_cr_tratada.columns = df_clientes_cr_tratada.columns.str.upper() #Deixando as colunas em MAIUSCULOS

df_clientes_cr_tratada.columns = df_clientes_cr_tratada.columns.str.replace(' ', '_') # Substitui os espaços por underline nos nomes das colunas dos clientes
df_interacoes_clientes_tratada.columns = df_interacoes_clientes_tratada.columns.str.replace(' ', '_') # Substitui os espaços por underline nos nomes das colunas das interações

#Alterando o nome da coluna
df_clientes_cr_tratada = df_clientes_cr_tratada.rename(columns={"cliente_id":"id_cliente","ultima_compra_data":"data_ultima_compra"})


# print(df_clientes_cr_tratada.info())
df_clientes_cr_tratada["nome"] = df_clientes_cr_tratada["nome"].astype("string")
# print(df_clientes_cr_tratada.info())
print(df_clientes_cr_tratada.describe())
print(df_interacoes_clientes_tratada.describe())