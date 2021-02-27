import matplotlib.pyplot as plt

data = [10, 5, 100, 40]
register = 0, 1, 2, 3
pets = 'CAT', 'DOG', 'HEDGEHOG', 'BUNNY'

plt.figure(figsize=(8, 4))
b = plt.bar(register, data, width=.8,
            color=('m', 'r', 'b', 'g'))
plt.title('FAVOURITE PETS')
plt.xticks(register, pets)
plt.legend(b, pets)
plt.show()


plt.figure(figsize=(8, 4))
b = plt.barh(register, data, height=.8,
             color=('m', 'r', 'b', 'g'))
plt.title('FAVOURITE PETS')
plt.yticks(register, pets)
plt.legend(b, pets)
plt.show()
