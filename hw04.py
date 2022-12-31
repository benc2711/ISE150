'''
Ben Crotty
ISE 150, Spring 2022
bcrotty@usc.edu
Homework 4
'''
userInput = "a"
hConsonants="p k h l m n "
hConsonantsList = hConsonants.split(" ")
vowels=['a','e','i','o','u']
hPunctuation =['\'','`']
vowelsSound=['ah','eh','ee', 'oh', 'oo']
doubleVowels=['ai','ae', 'ao', 'au', 'ei', 'iu', 'oi', 'ou', 'ui']
doubleVowelsSound=['eye', 'eye','ow', 'ow','ay','eh-oo','ew','oy','ow','ooey']
wrongCount =0
totalLettersList =['a','i','e','o','u','e','p','k','h','l','m','n','w']

#Here is where I create all of my lists and initate some variables
while userInput != "":
    userInput = input("Please give me a hawaiian word ").lower()
    letterCount =0
    wordOutput = []
    currentSyllable = ""
    while letterCount < len(userInput):
#Here is where I run the central while loop that prompts multiple user inputs. I also initate my syllables and output list

        if (userInput[letterCount] not in totalLettersList) and (userInput[letterCount] not in hPunctuation):
            print("This is an invalid word")
            break
    #Here I check if the word is in my valid letters and puncuation lists.

        if userInput[letterCount] in hConsonantsList:
            currentSyllable+= userInput[letterCount]
    #Here if the letter is a consonant I add it to the list

        if userInput[letterCount] in vowels:
            if letterCount != len(userInput)-1:
                doubleLetter = userInput[letterCount] + userInput[letterCount + 1]
                if (userInput[letterCount + 1] in vowels) and (doubleLetter in doubleVowels):

                    index = doubleVowels.index(doubleLetter)
                    currentSyllable += doubleVowelsSound[index]
                    wordOutput.append(currentSyllable)
                    wordOutput.append('-')
                    currentSyllable=""
                    letterCount+=2
                    continue
        if userInput[letterCount] in vowels:
            index = vowels.index(userInput[letterCount])
            currentSyllable+= vowelsSound[index]
            wordOutput.append(currentSyllable)
            wordOutput.append('-')
            currentSyllable=""

#Here I check for vowels and double vowels along with adding my dashes to the words and changing letter counts

        if userInput[letterCount] == 'w':
            if letterCount == 0:
                currentSyllable +="w"
            elif (userInput[letterCount-1] == 'i') or (userInput[letterCount-1]=='e'):
                currentSyllable +="v"
            elif (userInput[letterCount-1]== 'u') or (userInput[letterCount-1]=='o'):
                currentSyllable += "w"
            else:
                currentSyllable+="w"
#Here I check for w and following the rules as given
        if (userInput[letterCount] == '\''):
            wordOutput.pop()
            wordOutput.append("\'")
        elif (userInput[letterCount] == '`'):
            wordOutput.pop()
            wordOutput.append('`')
#Here I check for punctioation and remove the last dash and insert the punctioation as to follow the rules. This originaly did not work but that was because of errors in my punctuation list.







        letterCount += 1
    if userInput != "":
        wordOutput.pop()
    #Here I remove the last dash along with increase letter count for constants
    delimiter=''
    newString = delimiter.join(wordOutput)
    print(newString)

#Here I print the string
print("Goodbye!")


#Tested will all test cases. Works.