'''
Ben Crotty
ISE 150, Spring 2022
bcrotty@usc.edu
Homework 1
'''


import random
print("Let's play a guessing game!")
play = input("Wanna play (y/n)? ")
guess = -1
rando =-2
#initiate some variables and import random along with define the play variable for the outer loop

while play == "y":
    print("I'm thinking of a number of a number between 1 and 10!")
    rando = random.randrange(10)+1
    #get a random number that is unique for each iteration of the game
    while guess != rando:
        guess = int(input("Try to guess it! "))
        if guess < rando and guess != rando :
            print("Too low!")
        elif guess > rando and guess != rando:
            print("Too high!")
#use if and elif statements to get the too high or too low and only run while guess does not equal random

    print("You got it!")

    play = input("Wanna play again (y/n)? ")
#ask if user wants to play again
print("Oh well, you're no fun!")

