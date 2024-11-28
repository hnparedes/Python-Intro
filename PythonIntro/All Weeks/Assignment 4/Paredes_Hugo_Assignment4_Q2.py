#2. This program generates a custom number dictionary by first putting it in an if else statement to see if it's a positive number first
diction_Number = int(input("Please enter a number: "))
if diction_Number <= 0:
  print("Number is not positive, try again")
else:  
  #Then it creates an empty dictionary which the for loop fills it in that covers the range from 1 to the user's number input + 1 and with each iteration as a result of the i's multiplying each other with every value increase of itself
  dictionary = {}
  for i in range(1, diction_Number + 1):
    dictionary[i] = i * i

  print("The dictionary generated is", dictionary)
