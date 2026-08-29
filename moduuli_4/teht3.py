print("enter empty space to end the task.")

status = True
nums = []

while status:
    user_input = input("Enter: ")

    if user_input == " ":
        status = False
    else:
        num = float(user_input)
        nums.append(num)

min = min(nums)
max = max(nums)
print(f"The highest number: {max}")
print(f"The lowest number: {min}")