
def calculate_sum(list):
    total = 0
    for value in list:
        total += value
    return total

print("To exit -> enter empty space.")
list = []

while True:
    num = input("Enter an integer: ")

    if num == " ":
        print("Exiting...")
        break

    list.append(int(num))

res = calculate_sum(list)
print(f"sum: {res}")