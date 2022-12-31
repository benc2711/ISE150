'''
Ben Crotty
ISE 150, Spring 2022
bcrotty@usc.edu
Homework 8
'''
import random

#Function: loadWords
# Purpose: loads in a file and adds each word into a list
# Parameters: filename
# Side effects: none
# Returns: list of words
def loadWords(fileName):
    fileIn = open(fileName, "r")
    wordList =[]
    for line in fileIn:
        word = (line.strip())
        wordList.append(word)

    fileIn.close()
    return wordList
#Function: loadArt
# Purpose: Loads the art file and then changes it to correct for errors
# Parameters: art file name
# Side effects: none
# Returns: list with art
def loadArt(artFileName):
    fileIn = open(artFileName, 'r')
    artlist =[]

    for line in fileIn:
        line = line.strip()
        line = line.replace("\\n", "\n")
        line = line.replace("\\\\","\\")

        artlist.append(line)

    fileIn.close()
    return artlist

#Function: addWord
# Purpose: checks if the word is already in the list. otherwise adds it to the list
# Parameters: a word and the wordlist
# Side effects: none
# Returns: true or false
def addWord(string, stringList):
    if string in stringList:
        return False
    else:
        stringList.append(string.lower())
        stringList.sort()
        return True

#Function: storeWords
# Purpose: Adds the new words to the wordlist
# Parameters: wordlist and a file
# Side effects: adds to a text file
# Returns:none
def storeWords(wordlist, fileName):
    fileIn = open(fileName, 'w')
    for word in wordlist:
        print(word, file = fileIn)
    fileIn.close()

#Function: pickWords
# Purpose: Picks a random word
# Parameters: wordlist
# Side effects: none
# Returns: a random word from the wordlist
def pickWords(wordList):
    randomWordNumber = random.randrange(0,len(wordList))
    randomWord = wordList[randomWordNumber]
    return randomWord

#Function: getEmpties
# Purpose: Takes the target word and makes it all underscores
# Parameters: a target word
# Side effects: none
# Returns: a list of underscores
def genEmpites(word):
    emptiesList =[]
    for x in range(len(word)):
        emptiesList.append("_")
    return emptiesList

#Function: setToString
# Purpose: to convert a list to a string
# Parameters: a list
# Side effects: none
# Returns: a string
def setToString(lettersList):

    letterString =""
    for x in range(len(lettersList)):
        letterString += lettersList[x]
        letterString += " "

    return letterString
#Function: gameOver
# Purpose:  to see if the user has won or lsot
# Parameters: a list of letters
# Side effects: none
# Returns: true or false
def gameOver(letterList):
    for x in letterList:
        if x == "_":
            return False
    return True

#Function: checkGuess
# Purpose: to see if the user made a correct guess
# Parameters: the guess, the target word, and the variable so far, meaning how far they have made it
# Side effects: prints
# Returns: prints to console
def checkGuess(userGuess, targetWord, soFar):
    for x in range(len(targetWord)):
        if userGuess == targetWord[x]:
            index = x
            soFar[index] = userGuess
    if userGuess in targetWord:
        return True
    else:
        return False


#Function: main
# Purpose: User input and UI
# Parameters: none
# Side effects: prints
# Returns: prints to console
def main():

    artFileInput = input("Art file name: ")
    artlist = loadArt(artFileInput)
    wordFileInput = input("Word file name: ")
    wordList = loadWords(wordFileInput)
    userInput = '1'
    #we want to loop the function until an invalid input is given
    while userInput == '2' or userInput == '1':
        print("Pick an option...")
        print("1. Play Spaceman \n2. Add to word list \n?. Quit")
        userInput = input()
        if userInput == '1':
            wrongCounter =0
            guessedLetters =[""]
            print("Lets play Spaceman")
            targetWord = pickWords(wordList)
            print(targetWord)
            userWord = genEmpites(targetWord)
            #This is where I initiate my variables and get the words for the user to guess
            while wrongCounter != len(artlist) and gameOver(userWord) != True:
                #This is my loop for when to run the game
                print(artlist[wrongCounter])
                print("You've already guessed these letters")
                print(setToString(guessedLetters))
                print("Your word is " + setToString(userWord))
                userGuess = input("Letter please: ")
                if userGuess == " ":
                    wrongCounter = len(artlist)-1
                elif userGuess == "":
                    wrongCounter = len(artlist)
                valid = 1
                ifGuessed = 1
                #This is the two variables that allow me to check for both already guessed and one character only
                while valid ==1:
                    if len(userGuess) >1:
                        valid =1
                        print("Please only enter one character")
                        userGuess = input("Letter please: ")
                    else:
                        valid =0
                while ifGuessed == 1:
                    if userGuess in guessedLetters and userGuess != "":
                        ifGuessed =1
                        print("This guess was already guessed")
                        userGuess = input("Letter please: ")
                    else:
                        ifGuessed =0
                # both of these while loops is to check for valid input
                guessedLetters.append(userGuess)
                counter =0
                if checkGuess(userGuess, targetWord, userWord):
                    for x in range(len(targetWord)):
                        if targetWord[x] == userGuess:
                            counter+=1

                    print("Your guess " + userGuess + " was found " + str(counter) + " times")

                else:
                    wrongCounter+=1
                    print("Your guess was wrong")
            if "_" in userWord:
                print("Unfortunatley you have lost. The word was " + targetWord)
            else:
                print("Congratulations you have guessed the word " + targetWord)
                #This is where I determine and print if the user won or lost the game



        if userInput == '2':
            print("Lets add to the word list")
            uWord = input("Enter a word for the wordlist ")
            if addWord(uWord, wordList):
                print("Added the new word " + uWord)
                wordList.append(uWord)
                storeWords(wordList, wordFileInput)
                #Here I store the words in the file
                print("Storing words...")
            else:
                print("The word " + "\"" + uWord + "\"" + " is already in the list.")


    print("Goodbye")




main()