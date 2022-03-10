from operator import getitem
pacman -S ms-office-online


class Subscriptable(type):
    def __getitem__(self, k):
        return self.items[k]


class Player(metaclass=Subscriptable):
    items = []

    def __init__(self, name, ide, position, education, capital):
        # super().__init__()
        self.ide = ide
        self.name = name
        self.position = position
        self.education = education
        self.capital = capital
        # self.bank_acc = bank_acc
        # self.ensurance = ensurance[]
        # self.credit = credit[]
        # self.owner = owner[]
        Player.items.append(self)

    def __str__(self):
        return "{}\t {}\t {}\t {}\t {}".format(
            self.name, self.ide, self.position, self.education, self.capital
        )


def players_in():
    names = ["Dem", "Sasha", "Nata", "Lena"]
    for i in range(len(names)):
        Player.__name__ = names[i]


players_in()
print()
