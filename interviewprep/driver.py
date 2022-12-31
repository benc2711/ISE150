import student

studentList = [student.Student("Beg", 1, {"python": 1, "java": 2, "c++": 3}),student.Student("Beg", 2, {"python": 3, "java": 2, "c++": 1}),student.Student("Beg", 3, {"python": 4, "java": 3, "c++": 2})]
#creating a list of students with their given values


def sort(chosenSkill):
    studList = studentList
    #We want to take a skill and return a new list ordering the students in that skill.
    n = len(studList)
    for i in range(len(studList)):
        #Itterating through every student


        for j in range(0,n-i-1):
            skills = studList[j].getLevel()
            skill = skills[chosenSkill]

            nextSkills = studList[j+1].getLevel()
            nextSkill = nextSkills[chosenSkill]
            if skill > nextSkill:
                studList[j], studList[j+1] = studList[j+1], studList[j]
            elif skill == nextSkill:
                id = studList[j].getId()
                nId = studList[j+1].getId()
                if id > nId:
                    studList[j], studList[j + 1] = studList[j + 1], studList[j]

    for stud in studList:
        print (stud.getLevel())
        print(stud.getId())
# sort("c++")

def mergeSortStudent(chosenSkill, arr):


    if len(arr) >1:
        middle = len(arr)//2
        L = arr[:middle]
        R = arr[middle:]

        mergeSortStudent(chosenSkill, L)
        mergeSortStudent(chosenSkill, R)

        i =j =k =0

        while i < len(L) and j < len(R):
            if L[i].getChosenSkill(chosenSkill) < R[j].getChosenSkill(chosenSkill):
                arr[k] = L[i]
                i+=1
            elif L[i].getChosenSkill(chosenSkill) > R[j].getChosenSkill(chosenSkill):
                arr[k] = R[j]
                j+=1
            elif  L[i].getChosenSkill(chosenSkill) == R[j].getChosenSkill(chosenSkill) and i>j:
                arr[k] = R[j]
                j += 1
            else:
                arr[k] = L[i]
                i += 1
            k+=1
        while i < len(L):
            arr[k] = L[i]
            i+=1
            k+=1
        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1


def mergeSortStudent2(chosenSkill, arr):
    if len(arr) > 1:
        middle = len(arr) //2
        L = arr[:middle]
        R = arr[middle:]

        mergeSortStudent2(chosenSkill, L)
        mergeSortStudent2(chosenSkill, R)

        i=j=k=0

        while i < len(L) and j < len(R):
            if L[i].getChosenSkill(chosenSkill) > R[j].getChosenSkill(chosenSkill):
                arr[k] = R[j]
                j+=1
            elif L[i].getChosenSkill(chosenSkill) < R[j].getChosenSkill(chosenSkill):
                arr[k] = L[i]
                i+=1
            elif L[i].getChosenSkill(chosenSkill) == R[j].getChosenSkill(chosenSkill) and i > j:
                arr[k] = R[j]
                j+=1
            else:
                arr[k] = L[i]
                i+=1
            k+=1
        while i < len(L):
            arr[k] = L[i]
            i+=1
            k+=1
        while j < len(R):
            arr[k] = R[j]
            j+=1
            k+=1






def printArr(arr):
    for stud in arr:
        print(stud.getLevel())
        print(stud.getId())


mergeSortStudent2('python', studentList)
printArr(studentList)




    # I want to search through the list of students. Acesss their skills. If their skill value is higher than the last entries skill value

# def mentorMatching:
