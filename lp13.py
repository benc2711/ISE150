'''
Ben Crotty
ISE150, Spring 2022
bcrotty@usc.edu
Lab practical 13
'''
#Function: loadFile
# Purpose: gets a dictionary and fills it with the csv file
# Parameters: file name and a dictionary
# Side effects: none
# Returns: if the file read is valid in the boolean form of true which is always in this case
def loadFile(fileName, dict):
    fileIn = open(fileName, "r")
    fileIn.readline()
    for line in fileIn:
        line = line.strip()
        if "," in line:
            row = line.split(",")
            dict[row[0]]=row[1]
        else:
            fileIn.readline()
        #Makes sure there is no index out of bounds by accounting for lines without commas
        #Also splits the line and allows us to add components to dictionary
    fileIn.close()
    return True
#Function: main
# Purpose: guser interface, input and searches dictionary for subreddit and corresponding value
# Parameters: none
# Side effects: prints to console
# Returns: none
def main():
    dict ={}
    #Initiates variables and dictionaries
    tFileName = input("Tallies File: ")
    valid =1
    valid2 =1
    #This variables make sure that the subreddit and file is valid and prompts the user again if they are not
    while valid == 1:
        if loadFile(tFileName, dict):
            #Makes sure the funciton is true
            valid = 0
            print("Loading data...")
            while valid2 == 1:
                subreddit = input("Subreddit: ")

                if subreddit in dict:
                    print(subreddit +" ---> " + str(dict[subreddit]))
                    valid2 =0
                    #this gets the value from the key in the dicitonary
                else:
                    print(subreddit + " is an unknown subreddit.")
                    valid2 =1
        else:
            print("Could not open that file")
            valid =1


main()
