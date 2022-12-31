'''
Ben Crotty
ISE 150, Spring 2022
bcrotty@usc.edu
Lab 19
'''

import lady
import animal

def displayMenu():
    #Have the different animals displayed
    retval = 0
    print("Pick an animal...")
    print("1) Fly")
    print("2) Spider")
    print("3) Bird")
    print("4) Cat")
    print("5) Dog")
    print("6) Goat")
    print("7) Cow")
    print("8) Horse")
    print("?) Sing the Song")
    retval = input(">")
    return retval


def main():

    grandma = lady.Lady("Helene")

    while True:
        uOption = displayMenu()
        if uOption == "1":
            grandma.swallow(animal.Fly)
        elif uOption == "2":
            grandma.swallow(animal.Spider)
        elif uOption == "3":
            grandma.swallow(animal.Bird)
        elif uOption == "4":
            grandma.swallow(animal.Cat)
        elif uOption == "5":
            grandma.swallow(animal.Dog)
        elif uOption == "6":
            grandma.swallow(animal.Goat)
        elif uOption == "7":
            grandma.swallow(animal.Cow)
        elif uOption == "8":
            grandma.swallow(animal.Horse)
        else:
            break
#This should all work, but I genuinly have no idea why it isn't I copied directly from Nathan
    grandma.singSong()

main()




