def calc(a,b,c):
    stepOne=a+b+c
    stepTwo=a-b-c
    stepThree=a*b
    stepFour=a*a
    stepFive=b*b
    stepSix=a*b*c
    stepSix=stepSix*stepSix*stepSix
    sum=(stepOne*stepTwo*stepThree) + stepFour + stepFive + stepSix
    return sum

a=int(input("Enter A "))
b=int(input("Enter B "))
c=int(input("Enter C "))
print("The Solved Equation Result is {}".format(calc(a,b,c)))