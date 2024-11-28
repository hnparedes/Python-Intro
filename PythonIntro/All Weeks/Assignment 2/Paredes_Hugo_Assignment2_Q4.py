#4. This program takes in 4 variable inputs that are a multiplier number, two numbers that cover the upper and lower range of the multiplicand, and the step_size to determine how much the multiplicand will increase each time until it reaches the upper mulitiplicand range
multiplier = int(input("Please enter the multiplier in the table: ")) #6
lower_multiply = int(input("Enter the lower bound of multiplicand: ")) #3
upper_multiply = int(input("Enter the upper bound of multiplicand: ")) #9
step_size = int(input("Enter the step size for the table: ")) #2

#Then it places the four variables into a for loop which makes a multiplication table for the multiplier times each number in the multiplying range
for number in range(lower_multiply, upper_multiply + 1, step_size):
  multiply = number
  result = multiplier * multiply
  print(multiplier, "x", multiply, "=", result)