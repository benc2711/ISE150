'''
Ben Crotty
ISE 150, Spring 2022
bcrotty@usc.edu
Lab 15
'''

import candy

def main():
    print("Let's make some candy")
    c1 = candy.Candy("Reeces's" , 90)
    c2 = candy.Candy("Gummy Bear", 50)

    print("Candy name: {}, calories {}".format(c1.mName, c1.mCal))
    print("Candy name: {}, calories {}".format(c2.mName, c2.mCal))

    candyPile=[]
    candyPile.append(c1)
    candyPile.append(c2)
    candyPile.append(candy.Candy("KitKat", 20))

    for item in candyPile:
        print("{} : {}".format(item.mName, item.mCal))

    print("Bye")
main()