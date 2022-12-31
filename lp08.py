'''
Ben Crotty
ISE 150, Spring 2022
bcrotty@usc.edu
Lab Practical 8
'''

letterDict ={}
userInput = "a"

for i in range(0,26,1):
    newKey = chr(i+65)
    letterDict[newKey] = 0

while userInput != "":
    userInput = input("Gimmie some text ")
    for x in range(0,len(userInput),1):
        if (ord(userInput[x]) >64 and ord(userInput[x]) < 90) or (ord(userInput[x]) >96 and ord(userInput[x])<123):
            letter = userInput[x]
            letterDict[letter.upper()]+=1

print("Here is the letter frequency:")
z=0

letterDictList = list(letterDict.keys())
letterDictList.sort()

for key in letterDictList:
    print(key, ":", letterDict[key])