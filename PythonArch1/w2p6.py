years = int(input("Give me amount of human years: "))
if years < 0:
    print("Only positive numbers are allowed")
    exit()
elif years <= 2:
    dogyears = years * 10.5
    print("DogYears: ", dogyears)
else:
    dogyears = 21 + (years - 2) * 4
    print("DogYears: ", dogyears)