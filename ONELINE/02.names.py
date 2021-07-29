from faker import Faker

faker = Faker()
names = []

for _ in range(25):
    names.append(faker.first_name())

print(names)

name_starts_a = [name for name in names if name.startswith("A")]
print(name_starts_a)

name_starts_a = filter(lambda name: name.startswith("A"), names)
print(list(name_starts_a))
print(tuple(name_starts_a))
