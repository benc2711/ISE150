'''
Ben Crotty
ISE 150, Spring 2022
bcrotty@usc.edu
Lab Practical 1
'''
#Declare variables
#variable for user name
userName=""
#variable for favorite animal
userFavoriteAnimal=""
#variable for favorite number
userFavoriteNumber=""
#declares the variable footsteps as an int
footstep= 0
#weclomes the player
print("Welcome to MadLibs 1.0")
#asigns the variable userName to the given input by the user
userName= input("What is your name? ")
#asigns userFavoriteAnimal to the user input
userFavoriteAnimal= input("What's your favorite four legged animal (in plural form)? ")
#Asigns userFavoriteNumber to the user input and castes as an int so that it can be used in multiplication for footstep
userFavoriteNumber = int(input("Enter your favorite number? "))

footstep = userFavoriteNumber * 4 + 2

print("Here's your Madlib:")
print(userName.title().strip() + " lead " + str(userFavoriteNumber).strip() + " \"" + userFavoriteAnimal.strip() + "\"" + ".")
print("They all left " + str(footstep) +" footprints each step of the way!")