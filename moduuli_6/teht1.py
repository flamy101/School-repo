import random

def randDrop():
    num = random.randint(1,6)
    return num

drop = randDrop()
count = 1

while drop != 6:
    print(f"\nRolled: {drop}")
    count += 1
    drop = randDrop()

print(f"\nRolled {drop}! Roll count: {count}")


