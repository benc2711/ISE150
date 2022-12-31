'''
Name
ISE150, Spring 2022
USC email
Homework 6
'''

import soundLib as sl

morseDict ={"A": ".-","B": "-...","C": "-.-.","D": "-..","E": ".","F": "..-.","G": "--.","H": "....","I": "..","J": ".---",
            "K": "-.-","L": ".-..","M": "--","N": "-.","O": "---","P": ".--.","Q": "--.-","R": ".-.","S": "...","T": "-","U": "..-",
            "V": "...-","W": ".--","X": "-..-","Y": "-.--","Z": "--..",}

morseOutput =""
userInput ="a"
#Here is my variable and dictionary declarations
while userInput != "":
    morseOutput =""
    userInput = input("Input a message to translate into morse code: ")
    for x in range(len(userInput)):
            if userInput[x].upper() in morseDict:
                morseOutput += morseDict[userInput[x].upper()]
                morseOutput += " "
            elif userInput[x] == " ":
                morseOutput += "  "
                #This also makes sure that I only consider letters and spaces and not punctioation

            #I only add two spaces because the third space will be given after the letter prior
    print(morseOutput)
    #Here I get and print the morse code by converting, using my dictionary, I convert letters to code.
    if userInput != "":
        userInputHear = input("Would you like to hear your morse code (y/n)? ")
#Here is where I aks if they want to hear the code and store it as a variable
    if userInputHear.lower() == "y":
        sl.initSound()
        for x in range(len(morseOutput)):
            if morseOutput[x] == ".":
                sl.addMorseDot()
            if morseOutput[x] == "-":
                sl.addMorseDash()
            if morseOutput[x] ==" ":
                sl.addMorsePause()

        sl.playSound()
        #Here is where I convert morse code to sound.

print("Goodbye!")


