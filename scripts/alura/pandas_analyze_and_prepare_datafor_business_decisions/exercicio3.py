import pandas as pd
from pathlib import Path  # Permite manipular caminhos de arquivos

'''
Contexto: Você recebeu a mesma base do exercício anterior e agora precisa limpá-la: remover duplicatas, padronizar textos, tratar nulos. A diretoria quer saber o valor médio por cidade, mas isso só será possível com a base limpa.

Base de dados: Use o mesmo DataFrame do exercício 3

Tarefa: Execute, na ordem:

Crie uma cópia da base com .copy()
Remova duplicatas por cliente_id, mantendo a primeira ocorrência
Padronize a coluna cidade com .str.strip().str.lower()
Preencha os nulos de nome com "nao informado"
Após a limpeza, quantos registros restaram? Quantas cidades únicas existem agora
'''

def caminho_principal():  # Define a função que retorna o caminho do arquivo CSV
    pasta_atual = Path(__file__).resolve().parent  # Define a pasta onde está o arquivo Python
    caminho_relatorio = pasta_atual / "clientes_crm.csv"  # Define o caminho do arquivo CSV
    return caminho_relatorio  # Retorna o caminho completo do arquivo

# Importar a base de dados
df = pd.read_csv(caminho_principal())  # Lê o CSV e cria o DataFrame df

# 1. Cópia
df_limpo = df.copy()  # Cria uma cópia da base original

# 2. Remover duplicatas
df_limpo = df_limpo.drop_duplicates(subset="cliente id")  # Mantém a primeira ocorrência de cada cliente
print(f"Registros após remover duplicatas: {len(df_limpo)}")
# Resposta: 2000 registros (removeu 40 duplicatas)

# 3. Padronizar texto
df_limpo["canal aquisicao"] = ( df_limpo["canal aquisicao"].str.strip().str.lower())  # Remove espaços extras e converte para minúsculas
df_limpo["status cliente"] = ( df_limpo["status cliente"].str.strip().str.lower())  # Remove espaços extras e converte para minúsculas

#print(df_limpo["canal aquisicao"].value_counts())
#print(df_limpo['status cliente'].value_counts())


# 4. Preencher nulos de nome
df_limpo["nome"] = df_limpo["nome"].fillna("nao informado")


# 5. Verificação final
print(f"Registros: {len(df_limpo)}")
print(f"Canais únicos: {df_limpo['canal aquisicao'].nunique()}")


#df_cliente_limpo.head()
