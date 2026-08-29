user_name = "some"
password = "123"


while True:
    user_nameINP = input("Enter user name: ")
    passwordINP = input("Enter password: ")

    if user_nameINP != user_name or passwordINP != password:
        print("\nUser name OR password is wrond.")
    else:
        print("\nLog in successfull!")
        break
    
