import sys
print(sys.executable)

import pandas as pd


ventes = pd.read_csv("data/ventes.csv")

df_ventes = pd.DataFrame(ventes)
print(df_ventes.head())

df_ventes = df_ventes.dropna().reset_index(drop =True)
df_ventes.shape

df_ventes["produit"] = df_ventes["produit"].str.strip().str.title()

df_ventes["date_vente"] = pd.to_datetime(df_ventes["date_vente"])
df_ventes[df_ventes.duplicated()]