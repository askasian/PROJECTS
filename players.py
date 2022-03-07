#!/usr/bin/env python
# -*- coding: utf-8 -*-
from dataclasses import astuple, dataclass
from typing import NamedTuple
import random


class Player(NamedTuple):
    name: str
    ide: int
    pos: int = 0
    edu_level: int = 0
    bank_acc: float = 0.00
    capital: float = 0.00
    credit: float = 0.00
    owner: list = []
    ens_level: int = 0

    players = []

    def __init_subclass__(self):
        Player.players.append(self)
        return NamedTuple.__init_subclass__()

        Player.players.append(Player)

    def __len__(self):
        return len(self.players)

    def __getitem__(self, position):
        return self.players[position]

    def __str__(self):
        return str(self)

    def __iter__(self):
        return iter(astuple(self))


Dem = Player("Dem", 1)
Lena = Player("Lena", 2)
Sasha = Player("Sasha", 3)
Nata = Player("Nata", 4)

for i in range(len(Player.players)):
    print(Player.players[i].ide)
