def gal_to_l(gallons):
    liters = gallons * 3.785
    return liters

litersArray = []
print("\nTo exit -> enter negative value.")

while True:
    gallons = int(input("\nEnter gasoline in gallons: "))

    if gallons < 0:
        print("Exiting...")
        break
    else:
        liters = gal_to_l(gallons)
        litersArray.append(liters)

print(f"\nAll values was converted! {litersArray}")
