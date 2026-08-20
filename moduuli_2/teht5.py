luoti = 13.3
naula = luoti * 32
leiviskä = naula * 20

leiviskät = int(input("anna leiviskät: "))
naulat = int(input("anna naulat: "))
luodit = int(input("anna luodit: "))

result = leiviskä * leiviskät + naula * naulat + luoti * luodit

kg = int(result // 1000)
g = result % 1000

print(f"Massa nykymittojen mukaan:\n{kg} kilogrammaa ja {g} grammaa.")


