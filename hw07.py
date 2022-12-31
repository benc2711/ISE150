'''
Ben Crotty
ISE 150, Spring 2022
bcrotty@usc.edu
Homework 7
'''
import random
#Function: roll
# Purpose: rolls 3 dice through random numbers
# Parameters: none
# Side effects: none
# Returns: a list of the three rolls
def roll():
    rollList = [random.randint(1,6),random.randint(1,6), random.randint(1,6)]
    return rollList
#Function: computereslt
# Purpose: finds the ammount won or lost from a bet
# Parameters: takes the roll list the user bet and the user guess
# Side effects: none
# Returns: profit and number of die matched
def computeReslt(rollList, uBet, guessed):
    match = 0
    profit = 0
    for x in rollList:
        if x == guessed:
            match+=1
    if match  == 0:
        profit = -1* uBet
    elif match == 1:
        profit = uBet * 2
    elif match == 2:
        profit = uBet + (uBet*3)
    elif match ==3:
        profit = uBet + (uBet*10)

    return profit , match

#Function: main
# Purpose: User input and UI
# Parameters: none
# Side effects: prints
# Returns: prints to console
def main():
    playAgain = "y"
    uMoney = 100
    while playAgain == "y" and uMoney > 0:

        valid = False
        valid2 = False
        while valid == False:
            uBet = float(input("Hello player. You have $" + str(uMoney) + " to bet. How much do you want your bet to be? "))
            #This is essentially just making sure that the user is allowed to bet
            if uBet < uMoney and uBet >0:
                valid = True
            else:
                valid = False
        #This checks for valid inputs on bet
        while valid2 == False:
            uBetNumber = int(input("What number do you want to bet on (1-6) "))
            if uBetNumber < 1 or uBetNumber >6:
                valid2 = False
            else:
                valid2 = True
        print("You bet " + str(uBet) + " on " + str(uBetNumber))
        rollList = roll()
        rollListString = ""
        #This is colling functions and iteratting through the roll list to print it as a string
        for x in range(len(rollList)):
            if x != len(rollList)-1:
                rollListString += str(rollList[x])
                rollListString += " , "
            else:
                rollListString += str(rollList[x])
        print("You rolled: \n \t " + rollListString)

        result, match = computeReslt(rollList, uBet, uBetNumber)
        print("You matched " + str(match) + " dice.")
        uMoney += result
        #This shows results and gives user feedback 
        if result <=0:
            print("You lost your bet")
            print("You now have $" + str(uMoney))
            playAgain = input("Would you like to play again (y/n) ")
        elif result >0:
            print("You won your bet")
            print("You now have $" + str(uMoney))
            playAgain = input("Would you like to play again (y/n) ")
    print("You ended up with $" + str(uMoney))

main()