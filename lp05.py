'''
Ben Crotty
ISE 150, Spring 2022
bcrotty@usc.edu
Homework 1
'''

name = "o"
while name != "":
    name = input("What is your name (enter to quit)? ").lower()
    end = len(name) -1
    vowels = ["a", "e", "i", "o", "u"]
    vowelsCount = 0
    #here I initiate my lest and vowel counter along with determining the last index of the name
    for i in range(0, end, 1):
        for x in range(0, 5, 1):
            if name[i] == vowels[x]:
                vowelsCount += 1
                #here I used nested for statements to iterate through each letter and then when I get to a letter iterate through each vowel and see if that character of a name is a vowel
    if name != "":
        print("That name has " + str(vowelsCount) + " vowel(s)!")
print("Goodbye")

#could also do a multistep if statement inside a for loop that iterates through the name. Might actually be simpler
# I know how to code which is why I used lists