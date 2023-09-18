meal= float(input("Cost of the meal: "))
tax = 0.21
tax = meal * tax
tip = 0.15
tip = meal * tip
total = round(meal + tax + tip, 3)
print("Tax: ",'{:.3f}'.format(round(tax,3)),',' "Tip: ", '{:.3f}'.format(round(tip,3)),',' "Total: ", total)
