"""
Author: Hugo Paredes
Date: 8/4/23
Purpose: Last_Number_List
"""
#2. This program makes a list from 1 to the user inputted number as the last number on the list by first recursively calling itself, minusing the number by 1 everytime until it becomes 1, then it prints out the numbers in ascending order
def listing(finalNum):
  if finalNum == 1:
    print(1, end=" ")
  else:
    listing(finalNum - 1)
    print(finalNum, end=" ")
    

#Then the main receives the user's number by telling the numbers from 1 to the final number by calling the function in which the function initiates its recursive program
def main():
  lastNum = int(input("Please enter a positive integer: "))
  print("The numbers from 1 to", lastNum, "is printed as follows:")
  listing(lastNum)



main()  