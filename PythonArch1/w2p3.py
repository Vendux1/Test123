sides = input("Give me amount of sides your shape has: ")
if (int(sides) == 3):
    print("Triangle")
else:
    if(int(sides) == 6):
        print("Hexagon")
    else:
        if(int(sides) == 8):
            print("Octagon")
        else:
            if(int(sides) == 10):
                print("Decagon")
            else:
                print("Amount of sides is out of range")
