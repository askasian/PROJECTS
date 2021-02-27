import matplotlib.pyplot as plt
import numpy as np
import random as rd
import pandas as pd

plt.style.use('seaborn')

# r = rd.seed(12)
# print(r)
drinks = [
    rd.sample((range(1, 20)), 5),
    rd.sample((range(1, 20)), 5),
    rd.sample((range(1, 20)), 5)
]
print(drinks)

x = np.arange(5)
print(x)

days = 'Mon', 'Tue', 'Wed', 'Thu', 'Fri'
plt.bar(x, drinks[0], bottom=np.sum(drinks[:0], axis=0), color='b',
        label='Latte')
plt.bar(x, drinks[1], bottom=np.sum(drinks[:1], axis=0), color='r',
        label='Cappuchino')
plt.bar(x, drinks[2], bottom=np.sum(drinks[:2], axis=0), color='g',
        label='Tea')
plt.xticks(x, days)
plt.legend()
plt.title('HOT DRINKS')
# plt.show()

plt.barh(x, drinks[0], left=np.sum(drinks[:0], axis=0),
         color='b', label='Latte')
plt.barh(x, drinks[1], left=np.sum(drinks[:1], axis=0),
         color='r', label='Cappuchino')
plt.barh(x, drinks[2], left=np.sum(drinks[:2], axis=0),
         color='g', label='Tea')
plt.yticks(x, days)
plt.legend()
plt.title('HOT DRINKS')
plt.tight_layout()
plt.show()

[plt.barh(x, drinks[i], left=np.sum(drinks[:i], axis=0)) for i in range(3)]
plt.show()
