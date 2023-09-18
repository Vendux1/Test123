date = input("Enter date in YYYY-MM-DD format: ")
try:
    year, month, day = map(int, date.split('-'))
    if month < 1 or month > 12:
        print("Input format ERROR. Correct Format: YYYY-MM-DD")
    elif day < 1 or day > 31:
        print("Input format ERROR. Correct Format: YYYY-MM-DD")
    else:
        if month == 2:
            if day == 28:
                day = 1
                month += 1
            else:
                day += 1
        else:
            if day == 30 and (month == 4 or month == 6 or month == 9 or month == 11):
                day = 1
                month += 1
            elif day == 31 and (month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10):
                day = 1
                month += 1
            elif day == 31 and month == 12:
                day = 1
                month = 1
                year += 1
            else:
                day += 1

        print(f"Next Date: {year}-{month:02d}-{day:02d}")
except ValueError:
    print("Input format ERROR. Correct Format: YYYY-MM-DD")