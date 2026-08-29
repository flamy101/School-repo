import random

inside = 0
tryCount = 0

amount = int(input("Enter amount of iterations: "))

for i in range(amount):

    x = random.uniform(-1, 1)
    y = random.uniform(-1, 1)

    if (x ** 2 + y ** 2) < 1:
        inside += 1
        tryCount += 1

print(4 * inside / amount)