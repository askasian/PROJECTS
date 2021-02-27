import matplotlib.pyplot as plt
import numpy as np
import random as rd
import pandas as pd

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
plt.bar(x + 0.00, drinks[0], color='b',
        width=0.25, label='Latte')
plt.bar(x - 0.25, drinks[1], color='r',
        width=0.25, label='Cappuchino')
plt.bar(x + 0.25, drinks[2], color='g',
        width=0.25, label='Tea')
plt.xticks(x, days)
plt.legend()
plt.title('HOT DRINKS')
plt.show()


plt.barh(x + 0.00, drinks[0], color='b',
         height=0.25, label='Latte')
plt.barh(x - 0.25, drinks[1], color='r',
         height=0.25, label='Cappuchino')
plt.barh(x + 0.25, drinks[2], color='g',
         height=0.25, label='Tea')
plt.yticks(x, days)
plt.legend()
plt.title('HOT DRINKS')
plt.show()
