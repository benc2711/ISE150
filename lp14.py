'''
Ben Crotty
ISE 150, Spring 2022
bcrotty@usc.edu
Lab 14
'''

import calculator as calc
#Function: main
# Purpose: Displays the main function
# Parameters: None
# Side effects: prints to the console
# Returns: Nothing
def main():
    print("Welcome to Calc V3.0")
    userChoice = 3
    while userChoice > 0 and userChoice < 6:
        print("Choose an option \n 1. Add \n 2. Subtract \n 3. Multiply \n 4. Divide \n 5. Exponent")
        userChoice = int(input("Choose an option: "))
        if userChoice > 0 and userChoice < 6:
            userNumber1 = float(input("First number please: "))
            userNumber2 = float(input("Second number please: "))


        #Here I ask for user numbers and user choice selection for operation

        if userChoice == 1:
           answer = calc.add(userNumber1, userNumber2)
           print("Result = " + str(answer))
        elif userChoice == 2:
            answer = calc.subtract(userNumber1, userNumber2)
            print("Result = " + str(answer))

        elif userChoice == 3:
            answer = calc.multiply(userNumber1, userNumber2)
            print("Result = " + str(answer))

        elif userChoice == 4:
            answer = calc.divide(userNumber1, userNumber2)
            print("Result = " + str(answer))

        elif userChoice == 5:
            answer = calc.exponent(userNumber1, userNumber2)
            print("Result = " + str(answer))

        else:
            print("Unknown option selected")

    print("Goodbye")
#Here is my main function where I enact a function given the user choice.
main()