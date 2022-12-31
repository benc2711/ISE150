
'''
Ben Crotty
ISE 150, Spring 2022
bcrotty@usc.edu
Lab Practical 2
'''

# I didn't initate all variables because of my past experience with python
print("Welcome to Calc V1.0")
firstNumber= float(input("First number please: "))
secondNumber= float(input("Second number please: "))
print("Choose an option: \n 1.Add \n 2.Subtract \n 3.Multiply \n 4.Divide \n 5.Exponent")
chosenOption = float(input("Choose an option:"))
#Defines all my main variables with the inputs required
if chosenOption == 1:
    result = firstNumber+ secondNumber
    print("Result " + str(result))
elif chosenOption == 2:
    result = firstNumber - secondNumber
    print("Result " + str(result))
elif chosenOption == 3:
    result = firstNumber * secondNumber
    print("Result " + str(result))
elif chosenOption == 4:
    result = firstNumber / secondNumber
    print("Result " + str(result))
elif chosenOption == 5:
    result = firstNumber ** secondNumber
    print("Result " + str(result))

'''
Here I use if statements and else if statements to find what the user input really means in regards
to what operation I will be doing with the inputs they have given me. I then cast the result  into a string 
and print it. 
'''