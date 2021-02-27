import matplotlib.pyplot as plt
import numpy as np

x = np.arange(1, 10)**2
y = np.arange(1, 20, 2)**2
z = np.arange(1, 40, 4)**2

# plt.plot(x)
# plt.show()

plt.figure(figsize=(10, 4))
plt.plot(x, label='X', lw=2, marker='^', markersize=6)
plt.plot(y, label='Y', lw=2, marker='s', markersize=6)
plt.plot(z, label='Z', lw=2, marker='o', markersize=6)
plt.xlabel('TIME', fontsize=15)
plt.ylabel('PRICE', fontsize=15)
plt.title('GRAPH_1', fontsize=18)
plt.xticks(fontsize=15)
plt.yticks(fontsize=15)
plt.legend(fontsize=15)
plt.tight_layout()
plt.show()
