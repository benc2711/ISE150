import csv
import json

def loadFile(fileName):
    fileIn = open(fileName, 'r')
    for line in fileIn:
        line.strip()
        newLine = line.split(",")
    fileIn.close()

def loadFileWith(fileName):
    with open(fileName, 'r') as fileIn:
        for line in fileIn:
            line.strip()
            newLine = line.split(",")
            print(newLine[1])
def writeToFile(fileName,promptList):
    with open(fileName, 'w') as fileIn:
        stringy = ""
        for entry in promptList:
            stringy += entry
        print(stringy, file= fileIn)

def splitCSV(fileName):
    fileIn = open(fileName, 'r')
    fileIn.readline() #NEED TO USE THIS TO SKIP HEADER
    for line in fileIn:
        line.strip()
        row = line.split(",") #OTHER TYPES OF DELIMTERS: | " " etc.
def otherTypesFiles(fileName):
    data = json.loads(open(fileName).read())
    for item in data:
        for key in item:
            print(key + "...." + str(item[key]))

    data = csv.reader(open(fileName))
    next(data)
    for line in data:
        print(line)
def takeMultiple(name ="bob", times = 1):
    while times > 0:
        print(name)
        times = times-1
def returnMultiple():
    names = 5
    bro = []
    return names, bro



def starFunctions(*args, **kwargs):
    #*args takes all possible inputs in the function as a tupple and. Ie
    # starFunctions(1,2,3,4)
    #Kwargs just takes the key value pair inputs and makes them a dictionary
    print(args)
    print(kwargs)
def fileError(fileName):
    try:
        fileIn =open(fileName, 'r')
    except FileNotFoundError:
        print("Cannot find the file")
    except ZeroDivisionError:
        print("Cannot divide by zero")

def miss():
    state = "mississippi"
    s1 = state.lower().split("i")
    print([s1])
    print(s1[1:3]) #Doesnt count the last value
    #Prints as an array elements
    print(s1[:-2]) #Start at -2 and goes to the end which is the right
#Just to be clear the colon indicates where the split is goin if there is a 3: the no value after the colon implies going to the end from the start index 3
#If there is a :3 that implies it is going to index 3 not inclusive and starting from the start.
#Using negatives -2: it is starting from -2 and going to the end which is to the right or actual positive end fo the string
#:-2 we are starting from the begginging and going to the -2 index

def join(list):
    delimiter = " "
    x = delimiter.join(list)
    print(x)
def main():
    # names, bro = returnMultiple()
    miss()
    ge = list("Python")
    print(ge)
    ge.sort() #Capitals first then lower case alphabetically
    print(ge)



main()