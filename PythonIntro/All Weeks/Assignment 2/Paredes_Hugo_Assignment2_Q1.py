#1. This program first takes in the input of the user as an integer
number = int(input("Please enter an integer number: "))

#Then plugs it into an if else statement to first see if it's a negative
if number < 0:

  #if it is then it stops the program
  print("The program does not accept negative numbers")
else:

  #If the input int is positive, then it identifies to see if it's divisible by 3
  if number % 3 == 0:

    #If it is then it prints it's approval
    print(number, "is divisible by 3")
  else:

    #If not then it disproves it
    print(number, "is not divisible by 3")