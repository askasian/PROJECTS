class MyClass:
    def __init__(self, name):
        self.name = name
        self.checkme = "awesome {}".format(self.name)


instanceNames = ["red", "green", "blue"]

# Here you use the dictionary

holder = {name: MyClass(name=name) for name in instanceNames}

print(holder["red"].checkme)
print(holder["blue"].checkme)
