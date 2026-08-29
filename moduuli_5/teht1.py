import random

cube = int(input("Enter amount of cubes: "))
drop_sum = 0

for i in range(cube):
    drop  = random.randint(1, 6)
    drop_sum += drop

print(drop_sum)