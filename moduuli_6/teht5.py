def even_list(list):
    even_list = []

    for value in list:
        if value % 2 == 0:
            even_list.append(value)

    return even_list

print("To exit -> enter empty space.")
list = []

while True:
    value = input("\nEnter an integer: ")

    if value == " ":
        print("Exiting...")
        break

    list.append(int(value))

res = even_list(list)

print(f"\nBefore: {list} -> After: {res}")