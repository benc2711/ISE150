'''
Ben Crotty
ISE 150, Spring 2022
bcrotty@usc.edu
Homework 3
'''


optionSelect = "1"
mode = 0













while optionSelect == "1" or optionSelect == "2":
    optionSelect = input("Select an option: \n 1. Encrypt a message \n 2. Decrypt a message \n ?. Quit \n")
    if optionSelect == "1":
        mode = 1
        message = input("Enter a message to encrypt ")
        encrypted = ""
        for i in range(0, len(message), 1):
            newAlphabet = "EHTGDBWIUQRXLMVFSJCPYZKAON"
            if ord(message[i]) > 96 and ord(message[i]) < 122:
                inAlphabet = ord(message[i]) - 97
                encrypted += newAlphabet[inAlphabet].lower()
            elif ord(message[i]) > 64 and ord(message[i]) < 91:
                inAlphabet = ord(message[i]) - 65
                encrypted += newAlphabet[inAlphabet]
            else:
                encrypted += message[i]
            '''Basically what I am doing here is iteratting through each letter in the message and if it is a capital I take the ASIC code and subtract 97 to make 
            its place in the alphabet standard like A becomes 0 then I can use that number as an Index for the new alphabet and then add that to the encrypted message.
            I do basically the same thing in the elif statement except I account for the lower case. The else accounts for symbols like commas. '''

            # print(fmessage[i] + "  " + str(ord(fmessage[i]))+ "  " + str(inAlphabet) + "  " + newAlphabet[inAlphabet] )

        print("The secret message is: " + encrypted)
    elif optionSelect == "2":
        mode = 2
        message = input("Enter a message to decrypt ")
        unMessage = ""
        newAlphabet = "EHTGDBWIUQRXLMVFSJCPYZKAON"
        for i in range(0, len(message), 1):
            sLetter = message[i]
            for x in range(0, len(newAlphabet), 1):
                if sLetter.upper() == newAlphabet[x]:
                    sIndex = x
            if ord(sLetter) > 64 and ord(sLetter) < 91:
                unMessage += chr(sIndex + 65)
            elif ord(sLetter) > 96 and ord(sLetter) < 123:
                unMessage += chr(sIndex + 97)
            else:
                unMessage += sLetter
        print("The secret message is: " + unMessage)
        '''Here is my decrypt function which uses nested for loops. The first for loop gets a letter from the encrypted message so we can work with it
        the next for loop itterates through the new alphabet and get that index to essentially see where the letter from the encrypted message is in the 
        given alphabet. I can then use this to add to a variable called unMessage with chr to convert that index back into the regular alphabet. I again
        use if and elif statments to distinguish capital and non capital letters and then an else statement to account for symbols'''

print("Goodbye!")

'''Here is my while loop where I give the user options along with deploying my functions written above'''





