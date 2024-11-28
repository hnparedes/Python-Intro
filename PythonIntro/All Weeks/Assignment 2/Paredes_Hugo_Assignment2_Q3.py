#3. This program takes in four variable inputs from the user that are a two string names and two float numbers
first_student = input("Please enter the first student's name: ")
first_grade = float(input("Please enter the first student's score: "))

second_student = input("Please enter the second student's name: ")
second_grade = float(input("Please enter the second student's score: "))

#Then it prints out the variables in a table with two columns, one for name and one for score
print("%-15s%8s" % ("NAME", "SCORE"))

#Finally it prints out the two names in the name column 15 spaces left justified, and the two scores in the score column 8 spaces right justified
print("%-15s%8s" % (first_student, first_grade))
print("%-15s%8s" % (second_student, second_grade))