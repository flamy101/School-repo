import random

sideNum = int(input("Enter side amount: "))

def rollDie(sideNum):
    num = random.randint(1, sideNum)
    return num

drop = rollDie(sideNum)
tryCount = 0

while drop != sideNum:
    drop = rollDie(sideNum)
    tryCount += 1

print(f"Rolled {sideNum}! It took {tryCount} tries to roll.")