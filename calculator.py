'''
Ben Crotty
ISE 150, Spring 2022
bcrotty@usc.edu
Lab Calculator
'''
#Function: add
# Purpose: gets the sum
# Parameters: number1, number2
# Side effects: none
# Returns: sum
def add(number1, number2):
    sum = number1 + number2
    return sum
#Function: subtract
# Purpose: gets the subtraction result of two numbers
# Parameters: number1, number2
# Side effects: prints to the console
# Returns: sumsubtract

def subtract(number1, number2):
    sumsubtract = number1 - number2
    return sumsubtract
#Function: multiply
# Purpose: get the product
# Parameters: number1, number2
# Side effects: none
# Returns: product
def multiply(number1, number2):
    product = number1 * number2
    return product
#Function: divide
# Purpose: quotient is gotten
# Parameters: number1, number2
# Side effects: none
# Returns: quotient
def divide(number1, number2):

    if number2 == 0:
        print("Cannot divide by zero!")
        return 0
    else:
        quotient = number1 // number2
        return quotient
#Function: exponent
# Purpose: Displays Result = answer
# Parameters: number1, number2
# Side effects: none
# Returns: answer
def exponent(number1, number2):
    answer = number1 ** number2
    return answer