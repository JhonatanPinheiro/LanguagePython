import pandas as pd  # Importa a biblioteca Pandas
from pathlib import Path  # Importa Path para manipular caminhos de arquivos
import openpyxl
import matplotlib.pyplot as plt  # Biblioteca responsável pela exibição dos gráficos

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
df_clientes_cr_tratada["nome"] = df_clientes_cr_tratada["nome"].astype("string")

# print(df_clientes_cr_tratada.info())
# print(df_clientes_cr_tratada.info())
# print(df_clientes_cr_tratada.describe())
# print(df_interacoes_clientes_tratada.describe())

# print(df_interacoes_clientes.loc[2039])  # Busca a linha pelo rótulo do índice 2039.
# O .loc[] utiliza o índice (rótulo) para localizar os dados.

# print(df_interacoes_clientes.loc[0:5])  # Busca as linhas pelos índices de 0 até 5, incluindo o índice 5.
# O .loc[] inclui o último índice informado no intervalo.

# print(df_interacoes_clientes.iloc[2039])  # Busca a linha que está na posição 2039 do DataFrame.
# O .iloc[] utiliza a posição numérica da linha, começando em 0.

# print(df_interacoes_clientes.iloc[34:40])  # Busca as linhas das posições 34 até 39.
# O .iloc[] não inclui a posição final 40 no intervalo.

df_clientes_cr_tratada[df_clientes_cr_tratada['status_cliente'] == 'ATIVO'] # Realizando o filtro dos Dataframe para pegr os ATIVOS
# print(df_clientes_cr_tratada[df_clientes_cr_tratada['status_cliente'] == 'ATIVO']) # Realizando o filtro dos Dataframe para pegr os ATIVOS


# print(df_clientes_cr_tratada[( (df_clientes_cr_tratada["segmento_cliente"] == "VIP") | (df_clientes_cr_tratada["segmento_cliente"] == "NAO INFORMADO" )) & (df_clientes_cr_tratada["status_cliente"] == "ATIVO")] ) # Realizando o filtro usando pandas dos segmento_cliente  = "VIP" OU segmento_cliente = "NAO INFORMADO" E status_cliente = "ATIVO"
# print( df_clientes_cr_tratada[(df_clientes_cr_tratada["segmento_cliente"] == "VIP") & (df_clientes_cr_tratada["status_cliente"] == "ATIVO")] ) # Verifica se o segmento é VIP # Verifica se o status é ATIVO]

# df_clientes_cr_tratada[df_clientes_cr_tratada['segmento_cliente'].isin(['VIP','PREMIUM'])]
# print(df_clientes_cr_tratada[df_clientes_cr_tratada['segmento_cliente'].isin(['VIP','PREMIUM'])])

df_clientes_cr_tratada.query("(status_cliente == 'ATIVO' or segmento_cliente == 'VIP') and (canal_aquisicao.str.contains('cebo', case=False, na=False))")  # Realizando o filtro através do método query

# print(df_clientes_cr_tratada.query("status_cliente == 'ATIVO' or segmento_cliente == 'VIP' ") )

# Padronizando o nome da coluna que relaciona as duas bases
df_interacoes_clientes_tratada = df_interacoes_clientes_tratada.rename(
    columns={"cliente_id": "id_cliente"}
)

# Realizando o LEFT JOIN: mantém todos os clientes, mesmo sem interações
df_left = pd.merge(df_clientes_cr_tratada,df_interacoes_clientes_tratada, on="id_cliente", how="left")

# Realizando o INNER JOIN: mantém somente clientes com interações correspondentes
df_inner = pd.merge(df_clientes_cr_tratada,df_interacoes_clientes_tratada, on="id_cliente", how="inner")

# Unificando as bases (neste exemplo, utilizando LEFT JOIN)
df_unificado = pd.merge(df_clientes_cr_tratada,df_interacoes_clientes_tratada, on="id_cliente", how="left")

# Visualizando as informações do DataFrame unificado
# df_unificado.info()

# Exibindo os dados unificados
# print(df_unificado)

df_analitico = df_unificado.copy()
df_analitico['ano'] = df_analitico['data_cadastro'].dt.year
df_analitico['mes'] = df_analitico['data_cadastro'].dt.month
df_analitico['dia_nmr'] = df_analitico['data_cadastro'].dt.day
# pd.set_option("display.max_columns", None)
# print(df_analitico)

# Agrupando as interações e calculando a satisfação média
# print(df_unificado.groupby("tipo_interacao")["satisfacao_cliente"].mean().sort_values())

df_analitico['perfil_tempo'] = df_analitico['dia_nmr'].apply(lambda x : 'novo' if x <= 1500 else 'antigo')
# print(df_analitico)

# Removendo clientes duplicados pelo ID
df_clientes_cr_tratada = df_clientes_cr_tratada.drop_duplicates(
    subset='id_cliente',
    keep='first'
)

# Contabilizando a quantidade de clientes por segmento
df_clientes_cr_tratada['segmento_cliente'].value_counts().plot(
    kind='pie',
    title='Distribuição de clientes por segmento',
    figsize=(5, 5),
    autopct='%1.1f%%'
)

# plt.ylabel('')
# plt.show()



# # Verificando a quantidade de registros
# print("Total de registros:", len(df_clientes_cr_tratada))

# # Verificando a quantidade de clientes únicos
# print("Clientes únicos:", df_clientes_cr_tratada['id_cliente'].nunique())

# # Verificando se existem IDs duplicados
# print("IDs duplicados:", df_clientes_cr_tratada['id_cliente'].duplicated().sum())

# # Identificando todos os IDs duplicados
# clientes_duplicados = df_clientes_cr_tratada[
#     df_clientes_cr_tratada['id_cliente'].duplicated(keep=False)
# ]

# # Exibindo os registros duplicados
# print(clientes_duplicados[
#     ['id_cliente', 'nome', 'segmento_cliente']
# ].sort_values('id_cliente'))

# # Verificando quantos segmentos diferentes cada cliente possui
# verificacao_segmentos = (
#     df_clientes_cr_tratada
#     .groupby('id_cliente')['segmento_cliente']
#     .nunique()
# )

# # Exibindo clientes com mais de um segmento
# print(verificacao_segmentos[verificacao_segmentos > 1])





# Na aula, usamos diferentes tipos de gráficos para comunicar os insights da Connecta+. A escolha do gráfico certo é tão importante quanto a análise em si — um gráfico inadequado pode confundir a audiência ou, pior, comunicar uma conclusão errada.

# Guia prático por pergunta que se quer responder:

# Pergunta	Tipo de gráfico	Exemplo no projeto
# "Qual categoria tem maior valor?"	Barras (horizontais para nomes longos)	Valor médio por segmento
# "Como se distribui o total?"	Pizza (até 5-6 categorias) ou barras	Proporção de clientes por segmento
# "Qual a composição de cada grupo?"	Barras empilhadas	Retenção por canal (ativo vs inativo)
# "Como uma métrica evolui no tempo?"	Linha	Cadastros por mês
# "Como os grupos mudam no tempo?"	Barras agrupadas	Canais de atendimento por ano
# "Como os valores se distribuem?"	Histograma	Distribuição de idades
# "Há outliers? Qual a dispersão?"	Boxplot	Duração do atendimento por tipo
# "Há relação entre duas variáveis?"	Dispersão (scatter)	Idade vs valor gasto
# Erros comuns a evitar:

# Pizza com muitas fatias: acima de 5-6 categorias, a pizza fica ilegível. Use barras.
# Barras para tendência temporal: barras sugerem independência entre períodos. Linhas mostram continuidade e tendência.
# Escala que não começa em zero: em gráficos de barras, cortar o eixo Y exagera diferenças pequenas e pode induzir interpretações erradas.
# 3D em qualquer contexto: efeitos 3D distorcem a percepção de tamanho e dificultam a leitura. Sempre preferir 2D.
# Cores sem propósito: usar cores diferentes para cada barra quando não há necessidade de distinção visual adiciona ruído ao gráfico.
# Dica para apresentações executivas:

# Para diretoria, menos é mais. Um gráfico limpo com título claro, rótulos nos eixos e uma frase de insight na parte inferior comunica mais do que um dashboard cheio de visualizações competindo por atenção.

# Para se aprofundar:

# Atlassian: How to Choose the Right Data Visualization — guia visual com recomendação por tipo de dado e objetivo
# Flourish: How to choose the right chart type — guia baseado no vocabulário visual do Financial Times
# Documentação Pandas: Chart visualization — referência oficial sobre todos os tipos de gráficos disponíveis no .plot()