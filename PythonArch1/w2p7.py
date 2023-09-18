def chess_board():
    position = input("Enter the position on the chess board: ")
    column = ord(position[0]) - 96
    row = int(position[1])
    if column % 2 == 0:
        if row % 2 == 0:
            print("Black")
        else:
            print("White")
    else:
        if row % 2 == 0:
            print("White")
        else:
            print("Black")

chess_board()