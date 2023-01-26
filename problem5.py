import math

class equation:
    def __init__(self, x1, x2, y1, y2):
        self.x1 = x1
        self.x2 = x2
        self.y1 = y1
        self.y2 = y2

    def cacl(self):
        try:
            sumOfEquation = math.sqrt((self.x1 - self.x2) ** 2 + (self.y1 - self.y2) ** 2)
            return sumOfEquation
        except TypeError:
            print("Please use Valid data")
        except ValueError:
            print("Give a Good Values")


sum = equation(3,3,1,2)
print(sum.cacl())
