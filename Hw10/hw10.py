import hero




def main():
    superman = hero.hero("Superman|strength,flight,laser|5")
    print(superman.getName() +" has the following powers...")
    print(superman.__str__())

main()