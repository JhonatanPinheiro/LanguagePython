# 1 Quantos clientes únicos existem em cada base?
# 2 Faça um merge com inner join. Quantas linhas resultam? O cliente_id 5 (Eva) aparece? E o cliente_id 6?
# 3 Faça um merge com left join. Quantas linhas resultam agora? O que acontece com Eva?
# 4 Usando o resultado do inner join, calcule a satisfação média por segmento. Qual segmento tem a maior satisfação?
import pandas as pd

import pandas as pd

clientes = pd.DataFrame({
    "cliente_id": [1, 2, 3, 4, 5],
    "nome": ["Ana", "Bruno", "Carla", "Diego", "Eva"],
    "segmento": ["vip", "regular", "premium", "regular", "vip"]
})

interacoes = pd.DataFrame({
    "interacao_id": [101, 102, 103, 104, 105, 106, 107],
    "cliente_id": [1, 1, 2, 3, 4, 4, 6],
    "tipo": ["venda", "suporte", "reclamação", "dúvida", "reclamação", "suporte", "venda"],
    "satisfacao": [4.5, 3.8, 2.0, 4.0, 1.5, 3.0, 4.2]
})

# 1. Clientes únicos
print(f"Base clientes: {clientes['cliente_id'].nunique()} únicos")
print(f"Base interações: {interacoes['cliente_id'].nunique()} únicos")
# Resposta: Clientes: 5 únicos, Interações: 5 únicos (1, 2, 3, 4, 6)

# 2. Inner join
df_inner = pd.merge(clientes, interacoes, on="cliente_id", how="inner")
print(f"Inner join: {len(df_inner)} linhas")
print(df_inner["cliente_id"].unique())

# Resposta: 6 linhas
# Eva (id=5) NÃO aparece porque não tem interações
# Cliente 6 NÃO aparece porque não tem cadastro na base de clientes
# Inner join mantém apenas quem existe em AMBAS as bases

# 3. Left join
df_left = pd.merge(clientes, interacoes, on="cliente_id", how="left")
print(f"Left join: {len(df_left)} linhas")
print(df_left[df_left["cliente_id"] == 5])
# Resposta: 7 linhas
# Eva aparece com 1 linha, mas com NaN nas colunas de interação
# porque ela não tem registros na base de interações
# O left join preserva todos da base esquerda (clientes)

# 4. Satisfação por segmento (usando inner join)
df_inner.groupby("segmento")["satisfacao"].mean().round(2).sort_values(ascending=False)
# Resposta:
# vip        4.15  ← maior satisfação (Ana: 4.5 e 3.8)
# premium    4.00  (Carla: 4.0)
# regular    2.17  (Bruno: 2.0, Diego: 1.5 e 3.0)
#
# VIPs têm satisfação quase 2x maior que Regular!