
letterDict ={}
x=0
while x <26:
    newKey = chr(x+65)
    letterDict[newKey] =0

userInput = input("Give me a word")

for letter in userInput:
    letterDict[letter]+=1

print(letterDict)