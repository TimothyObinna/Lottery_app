import random

def Lucky_Winner():
    while 1:
        Username = input("Enter your Name, ")
        Users_Number = int(input("Enter your Lottery Number, "))
        Number = random.randint(0, 50)
        if Number == 30:
            print("Congratulations", Username,"! You  won")
        else:
            print("Sorry!", Username, "you lost, please try again")
Lucky_Winner()
