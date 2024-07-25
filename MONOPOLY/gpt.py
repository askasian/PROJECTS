import random

class Property:
    def __init__(self, name, price, rent):
        self.name = name
        self.price = price
        self.rent = rent
        self.owner = None

class Board:
    def __init__(self):
        self.properties = [
            Property("Go", 0, 0),
            Property("Mediterranean Avenue", 60, 2),
            Property("Baltic Avenue", 60, 4),
            Property("Income Tax", 0, 0),
            Property("Reading Railroad", 200, 25),
            # Add more properties as needed
        ]

    def display(self):
        for prop in self.properties:
            owner = prop.owner.name if prop.owner else "None"
            print(f"{prop.name}: Price=${prop.price}, Rent=${prop.rent}, Owner={owner}")

class Player:
    def __init__(self, name):
        self.name = name
        self.position = 0
        self.money = 1500
        self.properties = []

    def move(self, steps, board):
        self.position = (self.position + steps) % len(board.properties)
        print(f"{self.name} moved to {board.properties[self.position].name}")

    def buy_property(self, property):
        if property.price <= self.money and property.owner is None:
            self.money -= property.price
            property.owner = self
            self.properties.append(property)
            print(f"{self.name} bought {property.name} for ${property.price}")

    def pay_rent(self, property):
        rent = property.rent
        self.money -= rent
        property.owner.money += rent
        print(f"{self.name} paid ${rent} rent to {property.owner.name}")

class Game:
    def __init__(self, players):
        self.board = Board()
        self.players = players
        self.current_player_index = 0

    def play_turn(self):
        player = self.players[self.current_player_index]
        steps = random.randint(1, 6)
        player.move(steps, self.board)
        current_property = self.board.properties[player.position]

        if current_property.owner is None:
            if player.money >= current_property.price and current_property.price > 0:
                player.buy_property(current_property)
        elif current_property.owner != player:
            player.pay_rent(current_property)

        self.current_player_index = (self.current_player_index + 1) % len(self.players)

    def display_status(self):
        self.board.display()
        for player in self.players:
            print(f"{player.name}: Money=${player.money}, Properties={[p.name for p in player.properties]}")

# Example Usage
players = [Player("Alice"), Player("Bob")]
game = Game(players)

# Play 10 turns
for _ in range(10):
    game.play_turn()
    game.display_status()
    print("-" * 40)
