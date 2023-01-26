
class plaindrom:
    def __init__(self, enterStr):
        self.enterStr = enterStr
        

    def isPalindrome(self):
        x=list(self.enterStr)
        y=[]
        y.extend(x)
        x.reverse()
        if(x==y):
            return True
        return False


sum = plaindrom("MADAM")

if sum:
    print("Given Value is palindrom")
else :
    print("Given String is not Palindrom")

