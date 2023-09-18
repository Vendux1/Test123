import re
import datetime


def validName(name):
    r = r"^[A-Z]{1}[a-z]{1,9}$"
    if re.match(r, name):
        return True
    else:
        print("Input Error")
        return False


def validJob(job):
    r = r"[a-zA-Z]"
    if re.match(r, job) and len(job) >= 10:
        return True
    else:
        print("Input Error")
        return False


def validSalary(num):
    if num >= 20000 and num <= 80000:
        return True
    else:
        print("Input Error")
        return False


def validDate(date):
    try:
        x = datetime.datetime.strptime(date, "%Y-%m-%d").year
        if (x == 2021 or x == 2022):
            return True
        else:
            print("Input Error")
            return False
    except ValueError:
        print("Input Error")
        return False


fn = None
ln = None
jt = None
ans = None
sd = None
fb = None
feedback = None
i = input()
while i.lower() != "no":
    jor = input()
    if jor.lower() == "job offer":
        fn = input()
        while validName(fn) is False:
            fn = input()
        ln = input()
        while validName(ln) is False:
            ln = input()
        jt = input()
        while validJob(jt) is False:
            jt = input()
        ans = float(input().replace('.', '').replace(',', '.'))
        while validSalary(ans) is False:
            ans = float(input().replace('.', '').replace(',', '.'))
        sd = input()
        while validDate(sd) is False:
            sd = input()
    elif jor.lower() == "rejection":
        fn = input()
        while validName(fn) is False:
            fn = input()
        ln = input()
        while validName(ln) is False:
            ln = input()
        jt = input()
        while validJob(jt) is False:
            jt = input()
        fb = input()
        if fb.lower() == "yes":
            feedback = input()
        elif fb.lower() != "no":
            print("Input Error")
    if jor.lower() == "job offer":
        print("Here is the final letter to send:")
        print(f"Dear {fn} {ln},")
        print(f"After careful evaluation of your application for the position of {jt},")
        f = f'{ans:,.2f}'
        f = f.replace(',', "!")
        f = f.replace('.', ',')
        f = f.replace('!', '.')
        print(f"we are glad to offer you the job. Your salary will be {f} euro annually.")
        print(f"Your start date will be on {sd}. Please do not hesitate to contact us with any questions.")
        print("Sincerely,")
        print("HR Department of XYZ")
    elif jor.lower() == "rejection":
        print("Here is the final letter to send:")
        print(f"Dear {fn} {ln},")
        print(f"After careful evaluation of your application for the position of {jt},")
        print("at this moment we have decided to proceed with another candidate.")
        if feedback is not None:
            print(f"Here we would like to provide you our feedback about the interview. {feedback}")
        print("We wish you the best in finding your future desired career.")
        print("Please do not hesitate to contact us with any questions.")
        print("Sincerely,")
        print("HR Department of XYZ")
    i = input()