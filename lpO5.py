'''
Ben Crotty
ISE 150, Spring 2022
bcrotty@usc.edu
Homework 1
'''

name = "o"
while name != "":
    name = input("What is your name (enter to quit)? ").lower()
    end = len(name)
    vowelsCount = 0
    #here I initiate my variables and ask for user input
    for i in range(0, end, 1):
        if ord(name[i]) == 97 or ord(name[i]) == 101 or ord(name[i]) == 105 or ord(name[i]) == 111 or ord(name[i]) == 117:
            vowelsCount+=1
            #here I use a multi condition if statement to find vowels and then add counter. I don't have to deal with lower and upper because I already fixed that earlier.

    if name != "":
        print("That name has " + str(vowelsCount) + " vowel(s)!")
print("Goodbye")

#could also do a multistep if statement inside a for loop that iterates through the name. Might actually be simpler
# I know how to code which is why I used lists