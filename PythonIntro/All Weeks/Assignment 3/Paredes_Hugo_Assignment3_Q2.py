#
#2. This program starts off by creating three variables to cover the double summation additions with sum getting the total and i and j covering the start range
sum = 0
i = 2
j = 3

#Then they're plugged into a nested while loop with the i covering a range from 3 to 11, with each addition sequence having every i number getting added by the j range from 3 to 8
while i < 12:
  while j < 9: 
    sum += i + j
    j += 1
  i += 1
  j = 3
  #Once the additions are all added to the sum variable, it checks to see if i is equal to 12 so that the additions won't go over the range, then it breaks the loop and prints the sum
  if i == 12:
    break
print(sum)