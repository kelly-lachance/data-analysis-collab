import sys
print(sys.executable)

import pandas as pd
print("pandas", pd.__version__)

ventes = pd.read_csv("data/ventes.csv")

ventes.info()
