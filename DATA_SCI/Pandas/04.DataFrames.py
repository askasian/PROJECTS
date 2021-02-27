import numpy as np
import pandas as pd

from numpy.random import randn

np.random.seed(101)
df = pd.DataFrame(randn(5, 4),
                  ['A', 'B', 'C', 'D', 'E'], ['W', 'X', 'Y', 'Z'])
print(df)
print(df[['W', 'Z']])

df['V'] = df['W']+df['Y']
print(df['V'])
print(df)

print(df.drop('V', axis=1))
df.drop('V', axis=1, inplace=True)

print(df.drop('E'))
df.drop('E', inplace=True)

# Select ROWS

print(df.loc['A'])
print(df.iloc[0])
print(df.loc['A', 'W'])
print(df.loc[['A', 'B'], ['Y', 'Z']])
