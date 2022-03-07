import random
import pandas as pd


class Subscriptable(type):
    def __getitem__(self, k):
        return self.items[k]


class Place(metaclass=Subscriptable):
    items = []

    def __init__(self):
        # super().__init__()
        # ide,
        # tip,
        # price,
        # price_level,
        # owner,
        # level,
        # events[]
        # tax_permove,
        # payment_perhit,
        # tax_influence,
        # payment_influence,
        # self.ide = ide
        # self.tip = tip
        # self.price = price
        # self.price_level = price_level
        # self.owner = owner
        # self.level = level
        # self.tax_permove = tax_permove
        # self.payment_perhit = payment_perhit
        # self.tax_influence = tax_influence
        # self.payment_influence = payment_influence
        pass

    def upd_level(self):
        up_perc = 0.15
        if self.level < 3:
            self.level += 1
            self.price += self.price * up_perc
            self.price_level += self.price_level * up_perc
            self.payment_perhit += self.payment_perhit * up_perc
            print("Level of {} raised to {}".format(self.name, self.level))
            print("Price now is {}".format(self.price))
            print("Price to raise level is {}".format(self.price_level))
            print("Hit payment is {}".format(self.payment_perhit))
        else:
            print("Level of {} is maximal".format(self.name))


class Player(metaclass=Subscriptable):
    items = []

    def __init__(self, *args, **kwargs):
        # super().__init__()
        # self.ide =ide
        # self.name = name
        # self.position = position
        # self.education = education
        # self.capital = capital
        # self.bank_acc = bank_acc
        # self.ensurance = ensurance
        # self.credit = credit
        # self.owner = owner
        Player.items.append(self)

    def __str__(self):
        return "{ }\n{ }".format(*args, **kwargs)


# Bank1 = Place()
# Bank1.pos = 4
# Bank1.level = 1
# Bank1.price = 150000.00
# Bank1.price_level = 15000.00
# Bank1.payment_perhit = 4000.00
# Bank1.name = "Alfa Bank"

# Bank1.upd_level()
# Bank1.upd_level()
# Bank1.upd_level()

# print(Bank1.price)

Sasha = Player(ide=1, name="Sasha")
Demi = Player(ide=2, name="Demi")
Lena = Player(ide=3, name="Lena")
Nata = Player(ide=4, name="Nata")


def players_in():

    for i in range(len(Player.items)):
        print(str(Player.items[i]))


players_in()
print(Lena.ide, Lena.capital)

NUM_CELLS = 100
banks = 3
# food_shops =
# food_corts=
# malls=
# repair_shops =
# gas_stations=
# airports=
# train_stations=
# factories=
# developers=
# residentals=
# villas=
# terminals=

# tax_offices=
# police_stations=
# gails=
# exchanges=
# pharmacies=
# hospitals=
# agrocomplexes=
# freecells=
# scools=
# colleges=1
# universities=1
# insurances=


# cells_in()


# Dem.educ_k = 1
# Dem.tax_k = 1
# Dem.ins_k = 1


# print("\n", Dem.capital)
# print("\n", Players.items[1])
