'''
Ben Crotty
ISE 150, Spring 2022
bcrotty@usc.edu
Homework 1
'''
vehiclePrice = ""
totalDownPayment = ""
salesTax = ""
tradeinAnswer = ""
currentVehiclePrice = ""
currentVehicleOwed = ""
loanAmmount = 0
loanOption = 0
loanLength = 0
monthlyPaymentNumber =0
percentDown =0
monthlyInterest= 0
monthlyExponent = 0
monthlyPayment = 0
#initiating all variables


print("Bank of Ben Crotty - Auto Loan Payment Calculator")
vehiclePrice = float(input("Enter the Vehicles Purchase Price: "))
totalDownPayment= float(input("Enter the down payment for this vehicle: "))
salesTax= float(input("Enter the sales tax for the vehicle (for 8.25% enter 8.25): "))
tradeinAnswer= input("Do you have a car to trade in? Answer with y or n: ")
#gathering user input
if tradeinAnswer.lower() == "y":
    currentVehiclePrice= float(input("What is the current price of your vehicle? "))
    currentVehicleOwed = float(input("How much is owed on the vehicle "))
    totalDownPayment = totalDownPayment + (currentVehiclePrice-currentVehicleOwed)
    loanAmmount = (vehiclePrice-totalDownPayment)*(1+(salesTax/100))
    print("Your overall downpayment is: $" + str(totalDownPayment))
    print("Your overall Loan payment is: $" + str(loanAmmount))
else:
    loanAmmount = (vehiclePrice-totalDownPayment)*(1+(salesTax/100))
    print("Your overall downpayment is: $" + str(totalDownPayment))
    print("Your overall Loan payment is: $" + str(loanAmmount))

#determining if there is a trade in and preforming the corresponding necessary functions

print("Enter the length of your loan \n 1: 3 years \n 2: 4 years \n 3: 5 years \n 4: 6 years")
loanOption = int(input("Select an option: "))
if loanOption == 1:
    loanLength = 3
    monthlyPaymentNumber = loanLength * 12
    print("You selected a " + str(loanLength) + " year loan with a total of " + str(monthlyPaymentNumber) + " monthly payments.")

elif loanOption == 2:
    loanLength = 4
    monthlyPaymentNumber = loanLength * 12
    print("You selected a " + str(loanLength) + " year loan with a total of " + str(monthlyPaymentNumber) + " monthly payments.")

elif loanOption == 3:
    loanLength = 5
    monthlyPaymentNumber = loanLength * 12
    print("You selected a " + str(loanLength) + " year loan with a total of " + str(monthlyPaymentNumber) + " monthly payments.")
elif loanOption == 4:
    loanLength = 6
    monthlyPaymentNumber = loanLength * 12
    print("You selected a " + str(loanLength) + " year loan with a total of " + str(monthlyPaymentNumber) + " monthly payments.")
else :
    loanLength = 5
    monthlyPaymentNumber = loanLength * 12
    print("You are given a " + str(loanLength) + " year loan with a total of " + str(monthlyPaymentNumber) + " monthly payments.")
#if statements for possible loan options and storing new information in variables
print("*****************************")
percentDown = totalDownPayment/vehiclePrice *100

if loanLength == 3 and percentDown < 20:
    print("With "+ str(percentDown) +"% down and a " + str(loanLength) +" year loan, we can offer you an interest rate of 4.0%")
    interest = 4.0
elif loanLength == 4 and percentDown < 20:
    interest = 4.33
    print("With "+ str(percentDown) +"% down and a " + str(loanLength) +" year loan, we can offer you an interest rate of 4.33%")
elif loanLength == 5 and percentDown < 20:
    interest = 4.66
    print("With "+ str(percentDown) +"% down and a " + str(loanLength) +" year loan, we can offer you an interest rate of 4.66%")
elif loanLength == 6 and percentDown < 20:
    interest = 5
    print("With "+ str(percentDown) +"% down and a " + str(loanLength) +" year loan, we can offer you an interest rate of 5.0%")
elif loanLength == 3 and percentDown >= 20:
    interest = 3.7
    print("With "+ str(percentDown) +"% down and a " + str(loanLength) +" year loan, we can offer you an interest rate of 3.7%")
elif loanLength == 4 and percentDown >= 20:
    interest = 3.8
    print("With "+ str(percentDown) +"% down and a " + str(loanLength) +" year loan, we can offer you an interest rate of 3.8%")
elif loanLength == 5 and percentDown >= 20:
    interest = 3.9
    print("With "+ str(percentDown) +"% down and a " + str(loanLength) +" year loan, we can offer you an interest rate of 3.9%")
elif loanLength == 6 and percentDown >= 20:
    interest = 4.0
    print("With "+ str(percentDown) +"% down and a " + str(loanLength) +" year loan, we can offer you an interest rate of 4.0%")
#determining interest rate

print("*****************************")
monthlyInterest= interest/1200
monthlyExponent = (1+monthlyInterest)**(-monthlyPaymentNumber)
monthlyPayment = loanAmmount * (monthlyInterest/(1-monthlyExponent))
print("Your estimated monthly payment is " + str(monthlyPayment) + " a month")

#final prints