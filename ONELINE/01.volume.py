# sizes = input()
# sizes = sizes.strip()
# sizes = sizes.split()
# x = sizes[0]
# y = sizes[1]
# z = sizes[2]

# unpacking

x, y, z = input().strip().split()
# print(f"{x=}, {y=}, {z=}")


# upplying func int

x, y, z = map(int, (x, y, z))
volume = x * y * z
print(f"{volume=}")
