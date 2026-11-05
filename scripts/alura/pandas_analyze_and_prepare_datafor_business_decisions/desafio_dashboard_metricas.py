# Contexto: A diretoria pediu que você prepare 4 gráficos para a reunião trimestral, cada um comunicando um insight diferente. Você deve escolher o tipo de gráfico adequado e criá-lo usando apenas .plot() do Pandas.

# Base de dados:
# Tarefa: Crie os 4 gráficos e justifique a escolha de cada tipo:

# Gráfico 1: Comparar o valor médio gasto por segmento.
# Gráfico 2: Mostrar a proporção de clientes por segmento.
# Gráfico 3: Mostrar a evolução mensal de cadastros ao longo do ano.
# Gráfico 4: Comparar a taxa de reclamação por segmento, facilitando a leitura de categorias com nomes.


import pandas as pd

df = pd.DataFrame({
    "segmento": ["VIP", "Premium", "Regular"],
    "qtd_clientes": [400, 700, 900],
    "valor_medio": [12000, 7500, 3500],
    "satisfacao": [3.5, 3.2, 3.0],
    "pct_reclamacao": [24, 28, 35]
})

evolucao = pd.DataFrame({
    "mes": range(1, 13),
    "cadastros": [180, 165, 190, 140, 120, 110, 95, 105, 115, 130, 125, 145]
})


# Gráfico 1: Valor médio por segmento → BARRAS HORIZONTAIS
# Justificativa: barras são ideais para comparar magnitudes entre categorias
df.set_index("segmento")["valor_medio"].sort_values().plot(
    kind="barh",
    title="Valor Médio Gasto por Segmento (R$)",
    figsize=(8, 4),
    color=["#85C1E9", "#5DADE2", "#2E86C1"],
    xlabel="Valor médio (R$)",
    ylabel=""
)
# Insight: VIP gasta 3,4x mais que Regular

# Gráfico 2: Proporção por segmento → PIZZA
# Justificativa: pizza é boa para mostrar composição com poucas categorias (3)
df.set_index("segmento")["qtd_clientes"].plot(
    kind="pie",
    title="Distribuição de Clientes por Segmento",
    figsize=(6, 6),
    autopct="%1.1f%%",
    ylabel=""
)
# Insight: Regular é 45% da base, mas gasta 3,4x menos que VIP

# Gráfico 3: Cadastros ao longo do ano → LINHA
# Justificativa: linha mostra tendência e continuidade ao longo do tempo
evolucao.set_index("mes")["cadastros"].plot(
    kind="line",
    title="Cadastros por Mês",
    figsize=(9, 4),
    marker="o",
    color="#2E86C1",
    xlabel="Mês",
    ylabel="Cadastros",
    grid=True
)
# Insight: primeiro trimestre concentra mais cadastros; Q3 é o mais fraco

# Gráfico 4: Taxa de reclamação → BARRAS HORIZONTAIS
# Justificativa: barh facilita leitura quando queremos comparar taxas
df.set_index("segmento")["pct_reclamacao"].sort_values().plot(
    kind="barh",
    title="% de Interações que São Reclamações por Segmento",
    figsize=(8, 4),
    color=["#2ECC71", "#F39C12", "#E74C3C"],
    xlabel="% reclamações",
    ylabel=""
)
# Insight: Regular reclama mais (35%) que VIP (24%)



# Resumo das escolhas:

# Pergunta	Tipo escolhido	Por quê
# Comparar valores entre categorias	barh	Facilita comparação de magnitudes
# Mostrar proporção de um todo	pie	Bom para 3 categorias; mostra parte-todo
# Tendência ao longo do tempo	line	Mostra continuidade e sazonalidade
# Comparar taxas entre categorias	barh	Mesmo caso de comparação; barh é mais legível com nomes
