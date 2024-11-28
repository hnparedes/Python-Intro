fr = open("sentence.txt", 'r')

strSentence = fr.read()

sum = 0
counter = 0

for word in strSentence.split():
    counter += 1
    sum += len(word)

print("The average word length is", sum/counter)

fr.close()
