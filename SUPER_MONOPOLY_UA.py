import pandas as pd


class Place:
    def __init__(self):
        # super().__init__()
        # ide,
        # tip,
        # price,
        # price_level,
        # owner,
        # level,
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
        if self.level < 3:
            self.level += 1
            self.price += self.price * 0.15
            self.price_level += self.price_level * 0.15
            self.payment_perhit += self.payment_perhit * 0.15
            print("Level of {} raised to {}".format(self.name, self.level))
            print("Price now is {}".format(self.price))
            print("Price to raise level is {}".format(self.price_level))
            print("Hit payment is {}".format(self.payment_perhit))
        else:
            print("Level of {} is maximal".format(self.name))


class Player:
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
        # pass


Bank1 = Place()
Bank1.pos = 4
Bank1.level = 1
Bank1.price = 150000.00
Bank1.price_level = 15000.00
Bank1.payment_perhit = 4000.00
Bank1.name = "Alfa Bank"

Bank1.upd_level()
Bank1.upd_level()
Bank1.upd_level()


def Players_init():
    players = pd.Series
    # players = []
    player_names = ["Dem", "Sasha", "Nata", "Lena"]
    for i in range(len(player_names)):
        players.append(
            {
                Player.name=player_names[i],
                Player.ide=i,
                Player.position=0,
                Player.education=0,
                Player.capital=500000.00,
            }
        )

    print(
        players
        # players[i].name,
        # "\t",
        # players[i].ide,
        # "\t",
        # players[i].position,
        # "\t",
        # players[i].education,
        # "\t",
        # players[i].capital,
        # "\t",
    )


# Dem.educ_k = 1
# Dem.tax_k = 1
# Dem.ins_k = 1


print(Bank1.price)
Players_init()
