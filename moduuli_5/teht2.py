nums = []

while True:
    num = input("Enter a number or empty space to exit: ")

    if num == " ":
        break
    else:
        nums.append(float(num))

nums.sort(reverse=True)
print(nums[:5])