import random

randNum = random.randint(1, 10)

correctAnswer = False
tryCount = 0

while correctAnswer == False:
    answer = int(input("Your guess: "))
    tryCount += 1

    if answer < randNum:
        print(f"\nGuess {answer} is lower than correct number.")
    elif answer > randNum:
        print(f"\nGuess {answer} is greather than correct number.")
    else:
        print(f"\nGuess {answer} is correct!!!\nTry count: {tryCount}")
        correctAnswer = True