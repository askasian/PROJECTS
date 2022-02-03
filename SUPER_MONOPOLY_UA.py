class Player:
    def __init__(self):
        # super().__init__()
        # self.ide = ide
        # self.position = position
        # self.education = education
        # self.capital = capital
        # self.bank_acc = bank_acc
        # self.ensurance = ensurance
        # self.credit = credit
        pass


class Place(Player):
    def __init__(self):
        super().__init__()
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
            self.price += self.price * 0.1
            self.price_level += self.price_level * 0.1
            self.payment_perhit += self.payment_perhit * 0.1
            print("Level of {} raised to {}".format(self.name, self.level))
            print("Price now is {}".format(self.price))
            print("Price to raise level is {}".format(self.price_level))
            print("Hit payment is {}".format(self.payment_perhit))
        else:
            print("Level of {} is maximal".format(self.name))


Bank1 = Place()
Bank1.pos = 4
Bank1.level = 1
Bank1.price = 150000.00
Bank1.price_level = 15000.00
Bank1.payment_perhit = 4000.00
Bank1.name = "Alfa Bank"

Bank1.upd_level()

Dem = Player()
Sasha = Player()
Nata = Player()

Dem.ide = 1
Sasha.ide = 2
Nata.ide = 3

Dem.account = 0.00

Dem.educ_k = 1
Dem.tax_k = 1
Dem.ins_k = 1


print(Bank1.price)
print(Dem.ide)
