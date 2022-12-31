'''
Ben Crotty
ISE 150, Spring 2022
bcrotty@usc.edu
Lab Practical 6
'''
finalString=""
dirty_words =["dren", "frak", "frel", "glob", "grud", "narf", "zark"]
userInput ="a"

while userInput != "":
    userList = []
    userInput = input("What shall I censor: ")
    userList = userInput.split(" ")

#Here I run my while loop so that when entere is pressed it ends. I also define my variables.

    for i in range(0,len(userList),1):
        sWord = userList[i]
        for x in range(0,len(dirty_words),1):
            if sWord.lower() == dirty_words[x].lower():
                userList[i] = "BEEP"

#Here I itterate through my user list and asign each word to a varaible I can work with. I use another for loop to itterate through the dirty words and
#determine if the word variable I made is equal to any dirty word. If it is I change that index in the list

#print(userList)
    delimeter = " "
    newString = delimeter.join(userList)
    print(newString)
'''
    for i in range(0,len(userList),1):
        finalString += userList[i]
        finalString +=" "

    print(finalString)
'''
#for some reason this code was no working and was adding each input ontop of eachother
print("Goodbye!")



#Here I iterate through the new user list and combine everything in one string. I then print that string. I subtract one from length due to the last input being a space