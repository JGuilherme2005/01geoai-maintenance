import pandas as pd

# Simula leitura de dados dos sensores de pontes
df = pd.read_csv("pontes.csv")

# Regras preditivas simples (pode ser substituído por IA real depois)
def prever_risco(row):
    if row['Vibracao'] > 2.0 or row['Transito'] > 20000:
        return "Risco Alto"
    elif row['Vibracao'] > 1.0:
        return "Médio"
    else:
        return "Baixo"

# Aplicar lógica de risco
df["Status"] = df.apply(prever_risco, axis=1)

# Salvar novo CSV com status atualizado
df.to_csv("pontes_com_risco.csv", index=False)

print("Análise concluída! CSV gerado com status de risco.")
