'''
Ben Crotty
ISE 150, Spring 2022
bcrotty@usc.edu
HW 09
'''

import student as stud
#Function: genRoster
# Purpose: Takes the file and makes sure that it is openable and then sets a dictionary up using the student function of generating a student
# Parameters: class roster and file
# Side effects: none
# Returns: True or false based on if the file is valid
def genRoster(fileName, dict):
    try:
        fileIn = open(fileName, 'r')
    except:
        print("There is a problem with the file " + fileName)
        return False
    recordNumber = fileIn.readline()
    recordNumber.strip()

    for x in range(int(recordNumber)):
        sName = ""
        sLscores =""
        hwScores = ""
        mtScore = ""
        fScore =""
        for x in range(5):
            line = fileIn.readline()
            line = line.strip()
            if x == 0:
                sName = line
            if x == 1:
                sLscores = line
            if x == 2:
                hwScores = line
            if x ==3:
                mtScore = line
            if x == 4:
                fScore = line
        # This is pretty self explanatory but I am setting each line to the corresponding parameter values so that I can generate a student

        x = stud.genStud(sName,sLscores,hwScores,mtScore,fScore)
        dict[x[0]] = x[1]

    return True

#Function: getOvAvg
# Purpose: Get the overall average of the entire class hw grades
# Parameters: class roster and total points
# Side effects: none
# Returns: Returns the average of hw grades
def getHwAvg(rosterDict, totalPoints):
    x=0
    counter = 0
    for key in rosterDict:
        x += stud.getHwGrade(rosterDict[key], totalPoints)
        counter+=1
    return (x/counter).__round__(1)
#These functions all follow the same general formula by taking the entire roster and iteratting throuhg the keys to get each student then summing the students averages and dividing it by a counter

#Function: getOvAvg
# Purpose: Get the overall average of the entire class lab grades
# Parameters: class roster
# Side effects: none
# Returns: Returns the average lab grades
def getLpAvg(rosterDict):
    x = 0
    counter = 0
    for key in rosterDict:
        x += stud.getLpGrade(rosterDict[key])
        counter += 1
    return (x / counter).__round__(1)

#Function: getOvAvg
# Purpose: Get the overall average of the entire class midterms
# Parameters: class roster
# Side effects: none
# Returns: Returns the average of the Midterms
def getMtAvg(rosterDict):
    x = 0
    counter = 0
    for key in rosterDict:
        x += stud.getMTGrade(rosterDict[key])
        counter += 1
    return (x / counter).__round__(1)

#Function: getFeAvg
# Purpose: Get the overall average of the entire class for the final
# Parameters: class roster
# Side effects: none
# Returns: Returns the average
def getFeAvg(rosterDict):
    x = 0
    counter = 0
    for key in rosterDict:
        x += stud.getFinalGrade(rosterDict[key])
        counter += 1
    return (x / counter).__round__(1)

#Function: getOvAvg
# Purpose: Get the overall average of the entire class
# Parameters: class roster
# Side effects: none
# Returns: Returns the average
def getOvAvg(rosterDict):
    x = 0
    counter = 0
    for key in rosterDict:
        x += stud.getOverallGrade(rosterDict[key], 430)
        counter += 1
    return (x / counter).__round__(1)
# I used the round function because it is built in and I have used it before.

#Function: main
# Purpose: Displays the main function
# Parameters: None
# Side effects: prints to the console
# Returns: Nothing
def main():
    hwTotal = 430
    roster = {}
    userInput = input("What are the grades ")

    while genRoster(userInput, roster) == False:
            userInput = input("What are the grades ")
            if userInput == "":
                print("Quitting")
                return
#This just checks for if the file is not loading properly

    print("Loaded the grades")
    uInput = "5"
#This loop ensures that the user input is valid and if not it quits
    while uInput == "1" or uInput == "2" or uInput == "3" or uInput=="4" or uInput =="5":
        print("Select an option: \n\t1. Get lab Scores \n\t2. Get Homework Scores \n\t3. Get midterm exam scores \n\t4. Get final Exam Scores \n\t5. Get overall Grades \n\t?. Quit")
        uInput = input("")
        if uInput == "1":
            print("Name         %")
            # all of the following code in the if statements remains the relativly the same. The for key in roster essentially allows me to get the average of each student. With each key being a student
            for key in roster:
                x = stud.getLpGrade(roster[key])
                print(key + " " + str(x) + "%")
            print("Class " + str(getLpAvg(roster)) + "%")
            #This is more simple because we can just call the function above and use the entire roster because the entire class is being referenced
        elif uInput == "2":
            print("Name         %")
            for key in roster:
                x=stud.getHwGrade(roster[key], hwTotal)
                print(key + " " + str(x) + "%")
            print("Class " + str(getHwAvg(roster, hwTotal)) + "%")
        elif uInput == "3":
            print("Name         %")
            for key in roster:
                x = stud.getMTGrade(roster[key])
                print(key + " " + str(x) + "%")

            print("Class " + str(getMtAvg(roster)) + "%")
        elif uInput == "4":
            print("Name         %")
            for key in roster:
                x = stud.getFinalGrade(roster[key])
                print(key + " " + str(x) + "%")
            print("Class " + str(getFeAvg(roster)) + "%")
        elif uInput == "5":
            print("Name         %")
            for key in roster:
                x = stud.getOverallGrade(roster[key], hwTotal)
                print(key + " " + str(x) + "%")
            print("Class " + str(getOvAvg(roster)) + "%")
    print("Goodbye!")


main()