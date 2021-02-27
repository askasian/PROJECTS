# %%
import numpy as np
import pandas as pd

labels = ['a', 'b', 'c']
my_data = [10, 20, 30]
arr = np.array(my_data)
d = {'a': 10, 'b': 20, 'c': 30}

print(pd.Series(my_data))
# %%
pd.Series(my_data, labels)
print(pd.Series(data=my_data, index=labels))
print(pd.Series(my_data, labels))

pd.Series(arr)
print(pd.Series(arr))
print(pd.Series(arr, labels))

pd.Series(d)
print(d)
print(pd.Series(d))

ser1 = pd.Series([1, 2, 3, 4], ['USA', 'China', 'Germany', 'Japan'])
print(ser1)
ser2 = pd.Series([1, 2, 5, 4], ['USA', 'China', 'Italy', 'Japan'])
print(ser2)
print(ser1['USA'], ser2['Japan'])

ser3 = pd.Series(data=labels)
print(ser3, '\n', ser3[0])
