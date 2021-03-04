from random import randrange as rnd
from faker import Faker

fake = Faker()
stat = []
unit = []
year = 2000

experience_to_show = 15
initial_population = 7000
sexs = ['male', 'female']
cords = [100, 100]
area = (cords[0] * cords[1])

namef = [fake.first_name_male() for _ in range(40)]
namem = [fake.first_name_female() for _ in range(40)]
professions = [fake.job() for _ in range(40)]
phrase = ['I like you in these panties',
          'It is so sexy!',
          'You make me happy!',
          'I feel wet!',
          'I feel drizzle!',
          'I need this turn back!',
          'We are alone at all!',
          'Look i can do this with you!',
          'I will do what you like now!',
          'I like the way you do this!',
          'Take me now!',
          'Take me tighter!',
          'It so amazing!',
          'Use me as you want!',
          'I feel the fire!']


class Person():

    def __init__(self, ide, sex, name, age, profession, state, family, exp, cord):
        self.ide = ide
        self.sex = sex
        self.name = name
        self.age = age
        self.profession = profession
        self.state = state
        self.family = family
        self.exp = exp
        self.cord = cord

# def upd(): Live список номеров Unit.state = 'alive'

    def upd():
        Person.Live = [i for i, unit[i] in enumerate(
            unit) if unit[i].state == 'alive']

    def statistics():
        stat.append([year, len(Person.Live), Person.born,
                     Person.kills, Person.dead])
        # Person.Dead = [i for i, unit[i] in enumerate(unit) if unit[i].state == 'dead']

    def create(*args):
        sex = sexs[rnd(len(sexs))]
        if sex == 'male':
            name = namem[rnd(len(namem))]
        else:
            name = namef[rnd(len(namef))]
        if len(args) == 0:
            age = rnd(20, 55)
        else:
            age = 0
        profession = professions[rnd(len(professions))]
        state = 'alive'
        family = []
        if args:
            for i in args:
                family.append(i)
        exp = []
        cord = [rnd(cords[0]), rnd(cords[1])]
        ide = len(unit) + 1
        unit.append(Person(ide, sex, name, age,
                           profession, state, family, exp, cord))
        print('\nNew born: ', end='')
        Person.show(unit[-1])
        print()

        Person.upd()
        return unit[-1]

    def show(self, *args):
        print('\nid' + str(self.ide), self.name,
              self.age, self.profession, ' ', end='')
        for i in args:
            if type(i) == str or type(i) == int:
                print(i)
            else:
                for j in range(len(i)):
                    print(i[j])

    def shor(self):
        return ['id' + str(self.ide), self.name,
                self.age, self.profession]

# def move():
# for i in range(len(Person.Live)): для всего количества живых
# obj = Person.Live[i] номер живого из Live[]

    def move():
        Person.kills = 0
        Person.born = 0
        Person.dead = 0
        for i in range(len(Person.Live)):
            dx, dy = rnd(-1, 2), rnd(-1, 2)
            obj = Person.Live[i]
            if unit[obj].cord[0] == 0:
                dx = rnd(0, 2)
            if unit[obj].cord[0] == cords[0]:
                dx = rnd(-1, 1)
            if unit[obj].cord[1] == 0:
                dy = rnd(0, 2)
            if unit[obj].cord[1] == cords[1]:
                dy = rnd(-1, 1)
            unit[obj].cord[0] += dx
            unit[obj].cord[1] += dy

            unit[obj].age += 1

            if (unit[obj].age > 40 and rnd(30) == 1):
                unit[obj].state = 'dead'
                Person.dead += 1
                Person.show(unit[obj], str(year) + ' dead!',
                            'family:', unit[obj].family,
                            'experience:', unit[obj].exp)
                print()
            elif (unit[obj].age > 70 and rnd(8) == 1):
                unit[obj].state = 'dead'
                Person.dead += 1
                Person.show(unit[obj], str(year) + ' dead!',
                            'family:', unit[obj].family,
                            'experience:', unit[obj].exp)
                print()

        if len(Person.Live) == 0:
            print('No one alived at ' + str(year))
        print('\nYear: ' + str(year) + ' People count: ' +
              str(len(Person.Live)), end='')

    def findmatch():
        cc = []
        for i in Person.Live:
            for j in Person.Live:
                if unit[i].cord == unit[j].cord and unit[i].ide != unit[j].ide:
                    cc.append([unit[i], unit[j]])
                    if cc[-1][::-1] in cc:  # check if duplicate
                        cc.pop()  # remove duplicate

        for i in range(len(cc)):
            print('\nContact: ', end='')
            Person.show(cc[i][0])
            print('         ', end='')
            Person.show(cc[i][1])
            Person.contact(cc[i][0], cc[i][1])

    def contact(pers1, pers2):
        Person.iscouple(pers1, pers2)
        Person.iskill(pers1, pers2)

    def iscouple(pers1, pers2):
        # pers1, pers2
        if pers1.sex != pers2.sex:
            if 15 <= pers1.age <= 60 and 15 <= pers2.age <= 60:
                print('\nCouple! ')
                Person.show(pers1, '\nfcks ' + phrase[rnd(len(phrase))])
                Person.show(pers2, '\nscks ' + phrase[rnd(len(phrase))])
                pers1.exp.append([year, Person.shor(pers2)])
                pers2.exp.append([year, Person.shor(pers1)])

                Person.birth(pers1, pers2)

    def iskill(pers1, pers2):
        if rnd(6) == 1:  # chance of kill, 15 < age <  90
            if 15 <= pers1.age <= 90 or 15 <= pers2.age <= 90:
                if len(pers1.exp) > len(pers2.exp):
                    Person.kill(pers1, pers2)
                if len(pers2.exp) > len(pers1.exp):
                    Person.kill(pers2, pers1)

    def kill(pers1, pers2):
        pers2.state = 'dead'
        print('\n' + str(Person.shor(pers1)) +
              '\nkills ' + str(Person.shor(pers2)))
        pers2.exp.append([year, 'killed by', Person.shor(pers1)])
        pers1.exp.append([year, 'kills', Person.shor(pers2)])
        Person.show(pers2, str(year) + ' dead!',
                    'family:', pers2.family,
                    'experience:', pers2.exp)
        Person.kills += 1

    def birth(pers1, pers2):
        if rnd(3) == 1:
            if rnd(10) == 1:
                for _ in range(2):
                    newpers = Person.create(
                        Person.shor(pers1), Person.shor(pers2))
                    pers1.family.append([year, Person.shor(newpers)])
                    pers2.family.append([year, Person.shor(newpers)])
                    Person.born += 2
            else:
                newpers = Person.create(Person.shor(pers1), Person.shor(pers2))
                pers1.family.append([year, Person.shor(newpers)])
                pers2.family.append([year, Person.shor(newpers)])
                Person.born += 1


for _ in range(initial_population):
    Person.create()

while len(Person.Live) != 0 and len(Person.Live) < area:
    Person.move()
    Person.findmatch()
    Person.upd()
    Person.statistics()
    year += 1

print('\nPopulation raised ' + str(len(unit)) + ' people')


for i in range(len(unit)):
    if len(unit[i].exp) > experience_to_show:
        Person.show(unit[i], '\nfamily:', unit[i].family,
                    'experience:', unit[i].exp)

print('\n')

for i in range(len(stat)):
    print(stat[i])
