str="Guvi python"
listOfString=str.split(" ")
findStr="python"
if findStr in listOfString:
    indexOfString=listOfString.index(findStr)
    print("Find The String is")
    print(listOfString[indexOfString])
else:
    print("Word Not Found")