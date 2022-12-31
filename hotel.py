# CS 102 Placement Exam
# University of Southern California
#
# Given a hotel with 30 floors numbered 1-30 and up to 100 rooms per floor
# so that the lower 2 digits are the room number and upper digits are the
# floor number, take reservations that consist of pairs of inputs that
# represent the number of nights and a room number (each on a separate line)
# and terminated by "0 0", and output
#   a.) the average duration (number of nights) of a reservation,
#   b.) the floor number (1-30) that had the most reservations. If there is
#       a tie for the floor with the most reservations, you may output ANY
#       one of the floors that tied.
# For error checking of input values, you should ignore any input that
# has an illegal room number (i.e. above 3099 or below 100) or an input
# that has a negative number of nights for the reservation. Instead, count
# how many of these errors occur and output those values. So, in addition,
# to the outputting a. and b. described above, also output
#   c.) the number of invalid room numbers entered
#   d.) the number of negative reservation durations
#
# We guarantee inputs from the user will contain at least one valid entry
# so that there will always be a floor with the most reservations and a
# non-zero average duration.
#
# No other error conditions need be checked for and we guarantee the input
# will match our described format (two integers per line and terminated
# by a line with "0 0").
#
# Your program should compute the desired values a. through d. described
# above. Then, We have provided a function, `printResults()` below that you
# MUST call to output those answers in a format that will our automated
# tests will recognized.
#
# An example input and output sequence is shown below.
#
# Sample input:
# -------------
# | 101 2
# | 3099 3
# | 2054 -1
# | 3100 -1
# | 99 2
# | -546 3
# | 3064 2
# | 0 0
# -------------
#
# In the above there are only 3 valid input lines (the first 2 and the last).
# There are 3 lines with invalid room numbers (3100, 99, -546) and
# 2 lines with negative night durations.  Notice that one input line can
# contain both and invalid room number AND a negative night duration.
# 2.3333 is the average number of nights per reservation for the valid inputs.
# And floor 30 is the floor with the most reservations.
#
# The correct output of your program for this input is shown below:
# -------------
# | Average nights per reservation: 2.33333
# | Floor with most reservations: 30
# | Invalid room numbers: 3
# | Number of negative nights: 2
# -------------
#
# If you are unable to produce all 4 answers, you may pass dummy values
# (e.g. 0) to printResults(), but still produce and pass the answers you
# can correctly compute.

# You may not import other modules but must use built-ins

# Helper function to print out your computed results in
# the desired format to match our automated tests.
#------------------------- DO NOT ALTER THIS CODE ---------------------
def printResults(avgNights,
                 mostUsedFloor,
                 numInvalidRoomNumbers,
                 numNegativeNights):
    print("Average nights per reservation: " + str(avgNights));
    print("Floor with most reservations: " + str(mostUsedFloor));
    print("Invalid room numbers: " + str(numInvalidRoomNumbers));
    print("Number of negative nights: " + str(numNegativeNights));


def main():
    # Add your code here to declare data values, read the input,
    # and compute the desired answers.
    # userDict = {}
    numberFloorDict = {}
    # uInput = "k"
    sumDuration = 0
    counter =0
    negNights = 0
    invalidRoom =0
    max =0
    maxFloor = 0
    # while uInput != "?":
    #
    #     uInput = input("Enter a room number followed by the duration of stay make sure there is a space. If you want to quit enter a ? ")
    #     uInputList = uInput.split(" ")
    #     print(uInputList[0])
    #     print(uInputList[1])
    #     userDict[uInputList[0]] = uInputList[1]

    # userDict = {101:2, 3099: 3, 2054: -1, 3100: -1, 99:2, -546: 3, 3064: 2, 2134: 3, 2122:4, 2144: 5, -20:3}
    userDict = {}
    uInput = "0"
    while uInput != "0 0":

        uInput = input(
            "Enter a room number followed by the duration of stay make sure there is a space. If you want to quit enter a ? ")
        uInputList = uInput.split(" ")
        if uInput != "0 0":
            userDict[int(uInputList[0])] = int(uInputList[1])
    #I created this as a test case. I added the additional 21 floor rooms to ensure that my floor with most reservations was correct
    #I also wasn't sure where to pull my file from. I know how to pull a file and I originally thought of doing user input, but that wasn't specified.
    #Here is how I would open the file
    # fileIn = open(filename, 'r')
    # for line in fileIn:
    #     line = line.strip()
    #     listLine = line.split(" ")
    #     userDict[listLine[0]] = listLine[1]
    newDict = {}
    for key in userDict:
        #Here I was having the problem where when I had both the negative night and invalid room number I would only add to negative nights so I fixed that with this inital if statement
        if int(userDict[key])<0 and (int(key) < 100 or int(key) > 3099):
            negNights+=1
            invalidRoom+=1
        elif int(userDict[key])<0:
            negNights +=1
        elif int(key) < 100 or int(key) > 3099:
            invalidRoom +=1
        else:
            #This just creates a new dictionary with only valid numbers so that I can more easily work with it to find averages and floor with most reservation
            newDict[key] = userDict[key]
    for key in newDict:
        sumDuration += userDict[key]
        counter +=1
    average = sumDuration/counter
#This is simply going through the valid dictionary and getting the total number of nights and dividing that by a counter
    for x in range(1, 31, 1):
        numberFloorDict[x] = 0
    for key in newDict:
        if len(str(key)) >3:
            #This essentially just gets us the floor number from the room number
            floor = key//100
        else:
            floor = key//10
        numberFloorDict[floor] += 1
    # print(numberFloorDict)

    for key in numberFloorDict:
        if numberFloorDict[key] > max:
            max = numberFloorDict[key]
            maxFloor = key
        else:
            continue
    # print(str(maxFloor))

    
    

    # call printResults before exiting and pass it your answers
    printResults(average, maxFloor, invalidRoom, negNights)



if __name__ == "__main__":
    main()
