#3. This program begins by creating a function called count that is designed to count the total number of appearances of each letter of the string user inputs and sorts them alphebetically
def count(string):

  counts = {}
  for letter in string.lower():
    if letter not in " !":
      counts[letter] = counts.get(letter, 0)
      counts[letter] += 1
  sorted_letters = sorted(counts.items())
  return sorted_letters

#Next it begins the first real line of code by asking the user to input there string choice then creates a variable that plugs in the string in the count function
string = input("Enter a string: ")
total = count(string)

#Then it finally runs the main function that prints out the letter occurences in first alphabet letter appearance
def main():
  for letter, count in total:
    if count > 0:
      print(letter + ":", count, "times")

main()