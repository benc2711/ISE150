'''
Ben Crotty
ISE 150, Spring 2022
bcrotty@usc.edu
Lab 17
'''

import teacher
# Function opens a file returns a list of jokes
def loadJokes(inFileName):
    retval = []
    #open the file
    try:
        fileIn = open(inFileName, 'r')
        numJokes = int(fileIn.readline().strip())
        for i in range(numJokes):
            setup = fileIn.readline().strip()
            punchline = fileIn.readline().strip()
            seperator = fileIn.readline().strip()
            retval.append(setup + "\n" + punchline)
    except IOError:
        print("Could not open the file \"" + inFileName + "\"")
    except ValueError:
        print("Not able to get number of jokes")
    except IndexError:
        print("Problem with the list")
    except Exception as e:
        print("Error: " + str(e))
    return retval


def main():
    fName = input("Where are the jokes? ")
    ISE150Teacher = teacher.Teacher("Nathan", loadJokes(fName)) # For some reason this line is not working properly. I copied the same code as Nathan. I am not getting any errors either. Everything else works though. 
    Math225Teacher = teacher.Teacher("Professor")

    print("Time for a poll in ISE 150!")
    print(ISE150Teacher.getJoke())

    print("Time for MATH225")
    print(Math225Teacher.getJoke())


main()