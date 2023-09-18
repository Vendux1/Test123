import re

def license_plate():
    license = input("Enter the license plate: ")
    pattern = re.compile(r'^([A-Z]{2}-\d{2}-\d{2}|\d{2}-\d{2}-[A-Z]{2}|\d{2}-[A-Z]{2}-\d{2}|[A-Z]{2}-\d{2}-[A-Z]{2}|[A-Z]{2}-[A-Z]{2}-\d{2}|\d{2}-[A-Z]{2}-[A-Z]{2}|\d{2}-[A-Z]{3}-\d|\d-[A-Z]{3}-\d{2}|[A-Z]{2}-\d{3}-[A-Z]|\d-[0-9]{3}-[A-Z]{2}|[A-Z]{3}-\d{2}-[A-Z]|[0-9]-[A-Z]{2}-\d{3})$')
    if pattern.match(license):
        print("Valid")
    else:
        print("Invalid")

license_plate()