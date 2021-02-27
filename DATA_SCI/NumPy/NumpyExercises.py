import numpy as np

arr = np.zeros(10)
print(arr)

print(np.ones(10))
print(np.zeros(10) + 5)
print(np.arange(10, 51))
print(np.arange(10, 51, 2))

print(np.arange(9).reshape(3, 3))
print(np.eye(3))

print(np.random.rand(1))
print(np.random.randn(25))

print(np.linspace(0.01, 1, 100).reshape(10, 10))
print(np.linspace(0, 1, 20))

mat = np.arange(1, 26).reshape(5, 5)
print(mat)

mat = np.arange(12, 27).reshape(3, 5)
print(mat[:, :4])

print(np.arange(12, 27).reshape(3, 5)[:, :4])
print(mat[1, 3])
print(mat[:, 1])
print(mat[:, :4][2, :])

print(mat.sum())
print(mat.std())
