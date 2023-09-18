import datetime
holidays = {
    datetime.date(datetime.date.today().year, 12, 25): "Christmas"}
date = input("Give me a date in the following format in numbers: Month: , Day: ")
try:
    month, day = map(int, [s.split(':')[1] for s in date.split(',')])
    if month < 1 or month > 12:
        print("No holiday found on given input")
    elif day < 1 or day > 31:
        print("No holiday found on given input")
    else:
        if month == 12 and day == 25:
            print("Christmas")
        else:
            print("No holiday found on given input")
except ValueError:
    print("No holiday found on given input")