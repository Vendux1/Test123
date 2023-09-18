number = input("Enter a four-digit integer: ")
sum = 0
for digit in number:
    sum += int(digit)
print(number[0], "+", number[1], "+", number[2], "+", number[3], "=",sum)