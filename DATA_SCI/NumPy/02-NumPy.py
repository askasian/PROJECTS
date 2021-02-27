import numpy as np

arr = np.arange(0, 11)
print(arr)

print(arr[5])

print(arr[1:5])

print(arr[:6])

print(arr[5:])

arr[1:5] = 100
print(arr)
