import re
n=1
try:
    n=int(input("Enter a Natural Number"))
except:
    print("Type Error please enter valid number")

number=bool(re.match('^[1-9]+$', str(n)))
if number == True:
    print("{} is a natural number".format(n))
