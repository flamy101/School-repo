tuuma = float(input("Tuuma: "))
cm = 2.54

if tuuma < 0:
    print("Anna positiivisen numeron.")

while tuuma >= 0:
    res = tuuma * cm
    print(res)
    break