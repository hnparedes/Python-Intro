from os.path import exists

fileName = input("Please enter the file name: ")
if exists(fileName):
    fr = open(fileName, 'r')
    numbers = []
    for line in fr:
        eachList = line.split()
        for element in eachList:
            numbers.append(element)

    print(numbers)

else:
    print("This file does not exist")
