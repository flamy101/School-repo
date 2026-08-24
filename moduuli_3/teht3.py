gender = ["N","M"]

while True:
    gender_intput = input("Sukupuoli: ")

    if gender_intput not in gender:
        print("Wrong input")

    else:
        gemoglobin_intput = int(input("gemoglobin: "))
        if gender_intput == "N":
            if gemoglobin_intput in range(117,175):
                print("Gemoglobiino on OK.")
                break
            else:
                print("Gemoglobiini EI ole ok.")
        if gender_intput == "M":
            if gemoglobin_intput in range(134,195):
                print("Gemoglobiino on OK.")
                break
            else:
                print("Gemoglobiini EI ole ok.")
                break
        break