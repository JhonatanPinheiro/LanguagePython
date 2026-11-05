import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler


url="https://storage.googleapis.com/download.tensorflow.org/data/creditcard.csv"

df = pd.read_csv(url)

df["Class"].value_counts(normalize=True)
scaler = StandardScaler()

df["Amount_log"] = np.logip(df["Amount"])

