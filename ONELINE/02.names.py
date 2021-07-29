from faker import Faker

faker = Faker()
names = []

for _ in range(25):
    names.append(faker.first_name())

print(names)
