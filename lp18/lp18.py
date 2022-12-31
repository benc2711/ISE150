'''
Ben Crotty
ISE 150, Spring 2022
bcrotty@usc.edu
Lab 18
'''
import candy

def main():
    candyPile = []
    # c1 = candy.Chocolate("Kit-Kat", 10, 40)
    # c2 = candy.FilledChocolate("Reces", 5, 20 , "Peanut Butter")
    # c3 = candy.SoftCandy("Twix", 5, "Cherry")
    #
    # print("c1 ---" + str(c1))
    # print("c2 ----" + str(c2))
    # print(str(c3))
    while True:
        print("1) Candy")
        print("2) Chocolate")
        print("3) Filled Chocolate")
        print("4) Soft Candy")
        uOption = input("> ")

        if uOption == "1":
            inName  = input("Name: ")
            inCal = input("Calories: ")
            candyPile.append(candy.Candy(inName,inCal))
        elif uOption == "2":
            inName = input("Name: ")
            inCal = input("Calories: ")
            inPerCoco = input("Percentage of Coco: ")
            candyPile.append(candy.Chocolate(inName,inCal,inPerCoco))
        elif uOption == "3":
            inName = input("Name: ")
            inCal = input("Calories: ")
            inPerCoco = input("Percentage of Coco: ")
            inFilling = input("Filling: ")
            candyPile.append(candy.FilledChocolate(inName,inCal,inPerCoco,inFilling))
        elif uOption =="4":
            inName = input("Name: ")
            inCal = input("Calories: ")
            inFlavor = input("Flavor: ")
            candyPile.append(candy.SoftCandy(inName,inCal,inFlavor))
        else:
            break

    for item in candyPile:
        print(item)




main()