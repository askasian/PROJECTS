import matplotlib.pyplot as plt
import numpy as np

x = np.random.randint(1, 100, 20)
y = np.random.randint(1, 100, 20)
x2 = np.random.randint(1, 100, 20)
y2 = np.random.randint(1, 100, 20)
plt.figure(figsize=(6, 4))
plt.style.use('fivethirtyeight')

plt.scatter(x, y, label='first', s=(x + y) * 2, edgecolors='k', linewidth=2)
plt.scatter(x2, y2, label='second', s=(x2 + y2)
            * 2, edgecolors='k', linewidth=2)

plt.xlabel('X')
plt.ylabel('Y')
plt.legend(loc=(1.05, .4))
plt.title('SCATTER PLOT')

plt.tight_layout()
plt.show()
