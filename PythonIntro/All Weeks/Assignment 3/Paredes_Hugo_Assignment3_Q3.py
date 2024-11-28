"""
XXXXX
OXXXX
OOXXX
OOOXX
OOOOX
"""

#3. This program starts by creating 2 variables with i controlling the number of X's printed and j controlling the number of O's printed
i = 5
j = 0
#Then thy're plugged into a nested while loop to print X then O's 5 times. With X starting at 5 going down until 1 and O starting at 0 going up unitl 4
while i > 0:
  while j <= 4:
    print("O" * j, end="")
    print("X" * i, end="\n")
    j += 1
    i -= 1
  #Finally it checks to see if the i covering the X's is equal to 0 so that way the number of X's don't equal 0  
  if i == 0:
    break