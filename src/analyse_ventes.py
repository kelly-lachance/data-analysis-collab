import pandas as pd

analyse_vente = pd.read_csv("data/ventes.csv")

df_analyse_vente = pd.DataFrame(analyse_vente)

df_analyse_vente['CA total'] = df_analyse_vente['prix_unitaire'] * df_analyse_vente['quantite']


