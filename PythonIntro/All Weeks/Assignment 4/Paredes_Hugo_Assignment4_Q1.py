#1. This program starts by opening the txt file at read mode, then makes an empty line so the for loop can add all 3 of the lines into the bracket list
filename = input("Enter the input file name: ")
f = open(filename, 'r')
lines = []
for line in f:
  lines.append(line)

#Then they make a variable that holds the len number of the lines list then puts it into a while loop that prints how many lines there are, then asks the user what line they want to see then it prints out that line in that specific number index
num_line = len(lines)
while True:
  print("The file has", num_line, "lines")
  line_num = int(input("Enter a line number (0 to quit): "))
  if line_num == 0:
    break
  else:
    print(str(line_num) + ": " + lines[line_num - 1])