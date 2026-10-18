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
df_clientes_cr_tratada[["valor total", "idade"]] = (df_clientes_cr_tratada[["valor total", "idade"]].apply(pd.to_numeric, errors="coerce"))


# Tratando as colunas selecionadas para um padrão df_interacoes_clientes_tratada
df_interacoes_clientes_tratada[["canal interacao", "tipo interacao", "satisfacao cliente", "status resolucao"]] = (df_interacoes_clientes_tratada[["canal interacao", "tipo interacao", "satisfacao cliente", "status resolucao"]].apply(lambda coluna: coluna.astype("string").str.strip().str.upper()))
df_interacoes_clientes_tratada[["canal interacao","tipo interacao","status resolucao"]] = df_interacoes_clientes_tratada[["canal interacao","tipo interacao","status resolucao"]].fillna("NAO INFORMADO")
df_interacoes_clientes_tratada[["data interacao","duracao minutos","satisfacao cliente"]]= df_interacoes_clientes_tratada[["data interacao","duracao minutos","satisfacao cliente"]].fillna("-")

#------------------------------------------------------------------------------------------------------------------------------------------------------------------#

print(df_clientes_cr_tratada[["valor total", "idade"]].sample(10))