import matplotlib.pyplot as plt
import numpy as np

data = [
    np.random.randint(1, 20, 10),
    np.random.randint(1, 20, 10),
    np.random.randint(1, 20, 10)]

print(data)
print(len(data))

[plt.plot(data[i],
          label=['A', 'B', 'C'][i],
          marker=['o', 'h', '^'][i],
          markersize=5,
          color=['lightgreen', 'lightblue', 'g'][i])
 for i in range(len(data))]
plt.show()
