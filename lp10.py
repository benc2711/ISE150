'''
Ben Crotty
ISE 150, Spring 2022
bcrotty@usc.edu
Lab Practical 10
'''
#Function: add
# Purpose: Displays Result = sum
# Parameters: number1, number2
# Side effects: prints to the console
# Returns: Nothing
def add(number1, number2):
    sum = number1 + number2
    print("Result = " + str(sum))

#Function: subtract
# Purpose: Displays Result = sumsubtract
# Parameters: number1, number2
# Side effects: prints to the console
# Returns: Nothing

def subtract(number1, number2):
    sumsubtract = number1 - number2
    print("Result = " + str(sumsubtract))

#Function: multiply
# Purpose: Displays Result = product
# Parameters: number1, number2
# Side effects: prints to the console
# Returns: Nothing


def multiply(number1, number2):
    product = number1 * number2
    print("Result = " + str(product))
#Function: divide
# Purpose: Displays Result = quotient
# Parameters: number1, number2
# Side effects: prints to the console
# Returns: Nothing
def divide(number1, number2):
    if number2 == 0:
        print("Cannot divide by zero!")
    else:
        quotient = number1 // number2
        print("Result = " + str(quotient))
#Here is the division function that also considers if the second number is zero


#Function: exponent
# Purpose: Displays Result = answer
# Parameters: number1, number2
# Side effects: prints to the console
# Returns: Nothing
def exponent(number1, number2):
    answer = number1 ** number2
    print("Result = " + str(answer))
    #Here is the exponent function
#Function: main
# Purpose: Displays the main function
# Parameters: None
# Side effects: prints to the console
# Returns: Nothing
def main():
    print("Welcome to Calc V2.0")
    userNumber1 = float(input("First number please: "))
    userNumber2 = float(input("Second number please: "))
    print("Choose an option \n 1. Add \n 2. Subtract \n 3. Multiply \n 4. Divide \n 5. Exponent")
    userChoice = int(input("Choose an option: "))
    #Here I ask for user numbers and user choice selection for operation

    if userChoice == 1:
        add(userNumber1, userNumber2)
    elif userChoice == 2:
        subtract(userNumber1, userNumber2)
    elif userChoice == 3:
        multiply(userNumber1, userNumber2)
    elif userChoice == 4:
        divide(userNumber1, userNumber2)
    elif userChoice == 5:
        exponent(userNumber1, userNumber2)
    else:
        print("Unknown option selected")
        print("Result = 0")
#Here is my main function where I enact a function given the user choice.
main()

