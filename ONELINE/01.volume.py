# sizes = input()
# sizes = sizes.strip()
# sizes = sizes.split()
# x = sizes[0]
# y = sizes[1]
# z = sizes[2]

# unpacking

# x, y, z = input().strip().split()
# print(f"{x=}, {y=}, {z=}")


# upplying func int

# x, y, z = map(int, (x, y, z))
# volume = x * y * z
# print(f"{volume=}")

# simplify

# x, y, z = map(int, input().strip().split())
# volume = x * y * z
# print(f"{volume=}")

# reduce

from functools import reduce

volume = reduce(lambda x, y: x * y, map(int, input().strip().split()))
print(f"{volume=}")
