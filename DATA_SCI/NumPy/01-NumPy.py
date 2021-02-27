import numpy as np

my_list = [1, 2, 3]
arr = np.array(my_list)
print(arr)

my_mat = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(np.array(my_mat))

arr2 = np.arange(0, 11, 2)
print(arr2)

arr3 = np.zeros((3, 5))
print(arr3)

arr4 = np.ones((5, 5))
print(arr4)

arr5 = np.linspace(0, 5, 20)
print(arr5)

arr6 = np.random.rand(5)
print(arr6)

arr7 = np.random.randint(1, 100, 10)
print(arr7)
print(arr7.min())
print(arr7.max())
print(arr7.argmax())
print(arr7.argmin())
print(arr7.reshape(5, 2))
