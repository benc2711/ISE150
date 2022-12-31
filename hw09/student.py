'''
Ben Crotty
ISE 150, Spring 2022
bcrotty@usc.edu
Student Python file
'''
#Function: genStud
# Purpose: Generates a student kind of like an object but instead in the form of a dictionary
# Parameters: name, lab scores, hw scores, midterm score, final score
# Side effects: none
# Returns: both the name and the dictionary
def genStud(sName, lScores, hwScores, mtScore, fScore):
    newDict ={}
    lscoreList =[]
    hwScoresList =[]
    newDict["NAME"] = sName
    for score in lScores:
        if score != ",":
            lscoreList.append(score)

    hwScoresList = hwScores.split(",")
    # for score in hwScores:
    #     if score != ",":
    #         hwScoresList.append(score)
    newDict["LP"] = lscoreList
    newDict["HW"] = hwScoresList
    newDict["MT"] = int(mtScore)
    newDict["FE"] = int(fScore)

    return sName,newDict
#Function: getHwGrade
# Purpose: Get the overall grade of a student
# Parameters: dictionary of the student and grades
# Side effects: none
# Returns: Returns the overall
def getHwGrade(sDict, totalPoints):
    hwList = sDict["HW"]
    sum = 0
    for x in hwList:
        sum += int(x)
    avg = float((sum / totalPoints) * 100)
    avg = avg.__round__(1)
    return  avg

#Function: getLpGrade
# Purpose: Get the overall grade of a student for their labs
# Parameters: dictionary of the student and grades
# Side effects: none
# Returns: Returns the overall grade of the labs
def getLpGrade(sDict):
    lpList = sDict["LP"]
    sum = 0
    totalpoints =0
    for x in lpList:
        sum += int(x)
        totalpoints+=1

    avg = sum / totalpoints
    avg = avg * 100
    avg = avg.__round__(1)
    return avg

#Function: getMTGrade
# Purpose: Get the overall grade of a student for their midterm
# Parameters: dictionary of the student and grades
# Side effects: none
# Returns: Returns the midterm grade as a float
def getMTGrade(sDict):
    mtGrade = sDict["MT"]
    return float(mtGrade)
#Function: getFinalGrade
# Purpose: Get the overall grade of a student for the final exam
# Parameters: dictionary of the student and grades
# Side effects: none
# Returns: Returns the overall final grade converted to a float
def getFinalGrade(sDict):
    feGrade = sDict["FE"]
    return float(feGrade)
#Function: getOverallGrade
# Purpose: Get the overall grade of a student
# Parameters: dictionary of the student and grades
# Side effects: none
# Returns: Returns the overall
def getOverallGrade(dict, hwPoints):
    overall = .1*getLpGrade(dict) + .5*getHwGrade(dict,hwPoints) + .2*getMTGrade(dict) + .2*getFinalGrade(dict)
    overall = overall.__round__(1)
    return overall
