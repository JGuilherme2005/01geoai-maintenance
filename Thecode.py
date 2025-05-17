import pandas as pd

# Simula leitura de dados dos sensores de pontes
df = pd.read_csv("pontes.csv")

# Regras preditivas simples (pode ser substituído por IA real depois)
import pandas as pd

# Carregar dados com localização
df = pd.read_csv("dados_pontes.csv")

# Aplicar modelo básico ou inteligente de previsão
def prever_risco(row):
    if row['Vibracao'] > 2.0 or row['Transito'] > 20000:
        return "Alto"
    elif row['Vibracao'] > 1.0:
        return "Médio"
    else:
        return "Baixo"

df["Risco"] = df.apply(prever_risco, axis=1)

# Salvar com coordenadas geográficas
df.to_csv("pontes_com_risco.csv", index=False)

print("Análise concluída! Dados prontos para visualização no ArcGIS.")
