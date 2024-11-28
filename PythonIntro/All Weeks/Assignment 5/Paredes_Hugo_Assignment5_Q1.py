"""
Author: Hugo Paredes
Date: 8/4/23
Purpose: Sorted_List_Identifier
"""
#1. This program starts by creating 4 lists and plugging them into 4 if else statements to identify if they are sorted correctly
def main():


  list1 = [2, -1, 3, 0]
  list2 = []
  list3 = [5]
  list4 = [-2, 1]

  if isSorted(list1):
    print(list1, "is sorted in ascending order")
  else:
    print(list1, "is not sorted in ascending order")
  if isSorted(list2):
    print(list2, "is sorted in ascending order")
  else:
    print(list2, "is not sorted in ascending order")
  if isSorted(list3):
    print(list3, "is sorted in ascending order")
  else:
    print(list3, "is not sorted in ascending order")
  if isSorted(list4):
    print(list4, "is sorted in ascending order")
  else:
    print(list4, "is not sorted in ascending order")

#Then this function checks the list order by using a for loop covering the range from 1 to the length of the list, then identifying if the index is less than the previous index to prove that the list is increasing, then it returns the result
def isSorted(checkList):
  for i in range(1, len(checkList)):
    if checkList[i] < checkList[i - 1]:
      return False
      
  return True

main()