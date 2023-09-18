name = input()
reverse = name[::-1]
if name.replace(" ", "") == reverse.replace(" ", ""):
    print("is a palindrome")
else:
    print("is not a palindrome")