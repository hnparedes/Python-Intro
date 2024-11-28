#1. This program is a nested for loop that covers a mutiplier range from 2 to 4 and each of those three numbers are multiplied by 1, 2, and 3 and printed out in a table row
for i in range(2, 5):
  for j in range(1, 4):
    k = i * j
    print(i, " * ", j, " = ", k)