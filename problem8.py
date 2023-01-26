with open("myfile.txt", "w") as file1:
    file1.write("Hello World")

with open("myfile.txt", "r+") as file1:

    print(file1.read())