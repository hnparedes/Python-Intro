#2. This program starts by making a variable called sum equal to 0
sum = 0

#The for loop runs repeatedly for a total of 3 times and get the user to input a random number 3 times in which the numbers are added to the sum variable
for number in range(3):
  print("Iteration", number + 1)
  int(input("Please enter integer number: "))
  sum += number

#Then it plugs in the sum variable to the if else statement to see if the total sum of the 3 inputs are either less, equal or greater than 100 
if sum < 0:
  print("Sum is less than 100")
elif sum == 0:
  print("Sum is equal to 100")
else:
  print("Sum is greater than 100")