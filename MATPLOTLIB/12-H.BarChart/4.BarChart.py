import matplotlib.pyplot as plt
import numpy as np

plt.style.use('fivethirtyeight')
women = np.array([7, 20, 45, 30])
men = np.array([1, 35, 25, 60])
x = np.arange(4)
hobb = 'gaming', 'gym', 'pets', 'udemy'
plt.barh(x, women, label='Female')
plt.barh(x, -men, label='Male')
plt.legend()
plt.yticks(x, hobb)
plt.tight_layout()

plt.show()
