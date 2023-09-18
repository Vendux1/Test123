lengths = input("Give me the lengths of the sides: ")
a, b, c = map(int, [s.split('=')[1] for s in lengths.split(',')])
if(a==b==c):
    print("equilateral")
else:
    print("scalene")