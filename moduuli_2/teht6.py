import random


koodi1 = ""
koodi2 = ""

i = 1
j = 1


while i <= 3:
    num = str(random.randint(0,9))
    koodi1 += num
    i += 1

while j <= 4:
    num = str(random.randint(1,6))
    koodi2 += num
    j += 1

print(koodi1)
print(koodi2)