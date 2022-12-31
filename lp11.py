'''
Ben Crotty
ISE 150, Spring 2022
bcrotty@usc.edu
Lab Practical 11
'''

import random
#global variables are left aligned

COIN_FACES = ("HEADS", "TAILS")
#coin function gives me either heads or tails
#Function: coin
# Purpose: returns a random coin
# Parameters: none
# Side effects: uses random
# Returns: radom coin face
def coin():
    randNum = random.randrange(2)
    return COIN_FACES[randNum]
#Function: experiement
# Purpose:  gets the number of flips to achieve a certain ammount of either heads or tails in a row
# Parameters: inSide and inNum
# Side effects: returns a number
# Returns: number of flips
def experiment(inSide, inNum):
    numSides = 0
    numFlips = 0
    while numSides < inNum:
        result = coin()
        numFlips += 1
        if result == inSide:  #We got the side we want
            numSides+=1
        else:                   #We didnt get the side we want
            numSides =0
    return numFlips
#Function: Main
# Purpose: Gives all of the UI and uses the other functions
# Parameters: none
# Side effects: prints to the console
# Returns: Nothing
def main():

    # for x in range(10):
    #     print(coin())
    # A list to sotre the number of flips each experiment took
    triesList =[]
# Get the desired side from the user
    side = ""  #This sotres the sides the user wants

    while side not in COIN_FACES:
        side = input("Pick a side, heads or tails: ").upper()

#Get the desired number of times from the user
    numInRow = 0  #stores the number of the side in a row
    while numInRow <= 0:
        numInRow = int(input("How many " + side + " in a row do you want? "))
    #Get the number of times to exp

    numToRepeat = 0
    while numToRepeat <= 0:
        numToRepeat = int(input("How many times shall I repeat the experiement? "))
    while len(triesList) < numToRepeat:
        triesList.append(experiment(side, numInRow))

    sum =0
    for num in triesList:
        sum+= num

    print("Out of {} attempts, on average it took {} tries to get {} {} in a row".format(numToRepeat, sum/numToRepeat, numInRow, side))
main()