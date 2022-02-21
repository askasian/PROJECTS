#!/usr/bin/env python
# -*- coding: utf-8 -*-

from collections import namedtuple
import random

Car = namedtuple("Car", ["color", "brand"])


class Garage:

    def __init__(self):
        self._cars = [
            Car(color="brown", brand="Porsche"),
            Car(color="black", brand="BMW"),
            Car(color="silver", brand="Mercedes"),
        ]

    def __len__(self):
        return len(self._cars)

    def __getitem__(self, position):
        return self._cars[position]


garage = Garage()
print(len(garage))
print(garage[0])
print(garage[-1])
print(garage[0:3])

print(random.choice(garage))

for cars in garage:
    print(cars.brand)
