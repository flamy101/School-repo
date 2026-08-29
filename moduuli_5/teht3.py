intNum = int(input("Enter an integer: "))
isPrimeNum = True

for i in range(2, intNum):
    if intNum % i == 0:
        isPrimeNum = False
        break

if isPrimeNum:
    print(f"\nLuku {intNum} ON alkuluku.")
else:
    print(f"\nLuku {intNum} EI ole alkuluku.")
