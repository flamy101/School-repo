
names = []

print("Enter an empty space to exit.")

while True:
    name_input = input("Enter name: ")

    if name_input == " ":
        print("Exiting...")
        break

    if name_input in names:
        print(f"Name: '{name_input}' is already in stored.")
    else:
        names.append(name_input)
        print(f"Name: '{name_input}' added.")

print(f"\nAll added names:")

for name in names:
    print(f"{name}")
