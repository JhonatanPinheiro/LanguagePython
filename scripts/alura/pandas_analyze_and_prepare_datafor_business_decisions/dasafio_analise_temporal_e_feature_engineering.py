
# Prático - Análise temporal e feature engineering
# Discutir no fórum
# Contexto: O time de growth da Connecta+ quer entender padrões temporais: em que meses entram mais clientes? Quem é cliente "novo" vs "antigo"? O WhatsApp está crescendo?

# Base de dados:

# 1 - Extraia o ano e o mês do cadastro em novas colunas usando .dt.year e .dt.month.
# 2 - Calcule dias_desde_cadastro subtraindo data_cadastro de hoje (pd.Timestamp("today")).
# 3 - Crie a coluna perfil: "Novo" se até 365 dias, "Antigo" caso contrário. Quantos são "Novo" e quantos "Antigo"?
# 4 - Crie uma tabela cruzada de ano_interacao por canal_atendimento com normalize="index". O WhatsApp está crescendo?

import pandas as pd

df = pd.DataFrame({
    "cliente_id": [1, 2, 3, 4, 5, 6, 7, 8],
    "data_cadastro": pd.to_datetime([
        "2022-03-15", "2022-07-20", "2023-01-10", "2023-06-05",
        "2024-02-28", "2024-04-12", "2024-09-01", "2024-11-20"
    ]),
    "canal_atendimento": ["telefone", "email", "whatsapp", "telefone",
                          "whatsapp", "whatsapp", "whatsapp", "chat"],
    "ano_interacao": [2022, 2022, 2023, 2023, 2024, 2024, 2024, 2024]
})


# 1. Extrair ano e mês
df["ano_cadastro"] = df["data_cadastro"].dt.year
df["mes_cadastro"] = df["data_cadastro"].dt.month

print(df[["cliente_id", "data_cadastro", "ano_cadastro", "mes_cadastro"]])
# Os meses que mais aparecem: março, julho, janeiro, junho, fevereiro, abril, setembro, novembro

# # 2. Dias desde o cadastro
# df["dias_desde_cadastro"] = (pd.Timestamp("today") - df["data_cadastro"]).dt.days
# 2. Dias desde o cadastro
df["dias_desde_cadastro"] = (pd.Timestamp("2025-04-01") - df["data_cadastro"]).dt.days

# 3. Perfil Novo vs Antigo
df["perfil"] = df["dias_desde_cadastro"].apply(
    lambda x: "Novo" if x <= 365 else "Antigo"
)

print(df["perfil"].value_counts())

print(df[["cliente_id", "data_cadastro", "dias_desde_cadastro"]].head())

# Exemplo (se hoje fosse abril de 2025):
# cliente 1 (2022-03-15): ~1125 dias
# cliente 8 (2024-11-20): ~145 dias


# 3. Perfil Novo vs Antigo
df["perfil"] = df["dias_desde_cadastro"].apply(
    lambda x: "Novo" if x <= 365 else "Antigo"
)
print(df["perfil"].value_counts())


# Resposta (considerando ~abril 2025):
# Antigo    5 (clientes 1-5, cadastrados antes de abril 2024)
# Novo      3 (clientes 6-8, cadastrados após abril 2024)


# 4. Evolução do WhatsApp
tab = pd.crosstab(df["ano_interacao"],df["canal_atendimento"], normalize="index") * 100

print(tab.round(1))

# Resposta:
# canal_atendimento  chat  email  telefone  whatsapp
# ano_interacao
# 2022                0.0   50.0     50.0       0.0
# 2023                0.0    0.0     50.0      50.0
# 2024               25.0    0.0      0.0      75.0
#
# WhatsApp: 0% em 2022 → 50% em 2023 → 75% em 2024
# Sim, está crescendo significativamente!
