'''
Ben Crotty
ISE 150, Spring 2022
bcrotty@usc.edu
Lab Practical 1
'''

import math
number = float(input("Gimme a number: "))
mathCos =0
mathSin = 0
mathTan = 0
#Define the math variables and import the math library
if number>=0 :
    squareRoot = number ** .5
    squareRootMath = math.sqrt(number)
    print("Using the math library, the square-root of " + str(number) + " is " + str(squareRootMath))
    print("Using the exponent operator, the square-root of " + str(number) + " is " + str(squareRoot))
#Used an if statement to determine if the number is positive and enact the corresponding functions
mathCos=math.cos(math.radians(number))
mathSin=math.sin(math.radians(number))
mathTan=math.tan(math.radians(number))

#make code more readable by editing the variables outside of the print statements
print("Cos of "+ str(number) + " = " +str(mathCos))
print("Sin of "+ str(number) + " = " +str(mathSin))
print("Tan of "+ str(number) + " = " +str(mathTan))
#print the necessary statements combined with the variables