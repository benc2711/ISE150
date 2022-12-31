'''
Ben Crotty
ISE 150, Spring 2022
bcrotty@usc.edu
Homework 5
'''

monthsDicts ={'January': 31, 'Febuary':29, 'March': 30,'April': 30, 'May':31, 'June': 30,'July': 31, 'August':31, 'September': 30,'October': 31, 'November':30, 'December': 31}
userInput2="a"
userInput ="a"
calendarDict = {}
outputDict ={}
valid = 1

#Here I declare some of my variables and my dictionary
for keys, value in monthsDicts.items():
    newList =[]
    for x in range(value):
        newList.append('')

    calendarDict[keys]=newList
#Here I fill the dictionary with an array. So that in my dictionary each month has a value which is an array with the index number being the number of days in the month
while userInput != "":
    userInput = input("Enter a date for a holiday, (for example \"July 1\"): ")
    valid =1
    if userInput !="":
        splice = userInput.split()
        userMonth=splice[0]
        userMonthDays = splice[1]
        if len(splice) > 2:
            userMonthExtra=splice[2]
            valid = 0
            print("I don't see a good input in there.")

##Here I get variables so that I can have indivual spects of user input like the month the day and any extran information
        if userMonth not in monthsDicts.keys():
            valid = 0
            print("I don't know about the month " + "\"" + userMonth + "\"")

#Here I check and execute code that considers if the user enters a wrong month

        if userMonth in monthsDicts.keys():
            for keys in monthsDicts:
                if int(userMonthDays) > monthsDicts[userMonth]:
                    valid = 0
                    print("That month only has " + str(monthsDicts[userMonth]) +" days!")
                    break

#Here I run code that esentially checks if the user entered too many days. Then it resets to the user input
            if valid == 1:
                eventInput = input("What happens on " + userInput + "? ")
                dateIndex = int(userMonthDays)-1
                    # I want to use the date index to and insert the event input at that index
                calendarDict[userMonth].insert(dateIndex,eventInput)
                outputDict[userInput] = eventInput
#Here is my main code that after checking for errors inputs the event into the calendar

print("\n")
for keys in outputDict:
    print(keys + " : " + outputDict[keys])
#Here I print the output as shown in the homework example runs
print("\nGoodbye!")

