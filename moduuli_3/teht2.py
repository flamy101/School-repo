input = str(input("Hyttiluokka: "))

if input == "LUX":
    print("LUX on parvekkeellinen hytti yläkannella.")
elif input == "A":
    print("A on ikkunallinen hytti autokannen yläpuolella.")
elif input == "B":
    print("B on ikkunaton hytti autokannen yläpuolella.")
elif input == "C":
    print("C on ikkunaton hytti autokannen alapuolella.")
else:
    print("Virheellinen hyttiluokka")