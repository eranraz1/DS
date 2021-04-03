import pandas as pd
df = pd.read_csv('C:/Users/eranra/Documents/PY/ZMAT_CHAR.csv')
df.head(6)
df.median()
df[0:4] # first 4 lines
df[df['CARBON' == 'NO']]
