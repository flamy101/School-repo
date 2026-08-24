year = int(input("Vuosi luku: "))

if year % 4 == 0:
    print("\nVuosi on karkovuosi.")

elif year % 100 == 0:
    if year % 400 == 0:
        print("\nVuosi on karkovuosi.")
else:
    print("\nVuosi ei ole karkovuosi.")