'''
Ben Crotty
ISE 150, Spring 2022
bcrotty@usc.edu
Homework 2
'''
moreNumbers = "y"
#Here I have the overall while loop run while the answer to run is yes. It will run without user input the first time, but will continue to run given the user input at the end.
while moreNumbers == "y" or moreNumbers == "Y":

    userNumber = 10

    sum = 0
    sumCounter=0
    largestNumber = 0
    #Here I initate some of my variables outside of the next while loop to reset them for each run.

    while userNumber >= 0:
        userNumber = int(input("Input an integer greater than or equal to 0 or -1 to quit "))
        if sumCounter == 0:
            smallestNumber=userNumber
        if userNumber > largestNumber:
            largestNumber=userNumber

        if userNumber < smallestNumber and userNumber != -1:
            smallestNumber = userNumber

#Here I have my while loop collect the numbers and store the largest, smallest, and sum along with number of loops the while loop has gone through
        sum+=userNumber
        sumCounter+=1

    print("The largest number is " + str(largestNumber))
    print("The smallest number is " + str(smallestNumber))
    print("The average is " + str((sum+1)/(sumCounter-1)))
    moreNumbers = input("Would you like to enter more numbers? (y/n) ").lower()
    # Here I work with the numbers to make sure the -1 is not counted and print them.
    if moreNumbers == "n" or moreNumbers =="N":
        print("Goodbye!")
#Here I have the statement where goodbye is printed when there is a N user input