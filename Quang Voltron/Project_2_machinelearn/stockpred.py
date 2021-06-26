import pandas as pd
import numpy as np

df = pd.read_csv("SQ.csv")
df = df.drop(columns=["Date"])
print (df)

