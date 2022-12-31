'''
Ben Crotty
ISE 150, Spring 2022
bcrotty@usc.edu
Lab Practical 7
'''

userInput ="a"
#Holds user input from the keyboard
alphabetList =[]
#list of the occurances of a letter
#fill list with 26 0's

for x in range(26):
    alphabetList.append(0)

while userInput:
    userInput = input("Please enter some text: ")

    #loop over the user input
    for character in userInput.upper():
        if ord(character) >= ord("A") and ord(character) <= ord("Z"):
            #calculate the index for the letter
            letterIndex = ord(character)-ord("A")

            alphabetList[letterIndex] +=1
            #print("{} : {}".format(character,letterIndex))

   #outside of the for loop for each character
   #display the results
    for x in range(len(alphabetList)):
        if alphabetList[x]>0:
            asciiValue =x + ord("A")
            #convert ACII number to charcter
            character =chr(asciiValue)
            print(character + " : "+str(alphabetList[x]))


    #reset counters
    for x in range(len(alphabetList)):
        alphabetList[x]=0

print("Goodbye!")