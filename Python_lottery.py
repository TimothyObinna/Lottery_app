import random

Winning_number = 30
username = input("Enter your name to play: ")
print("Hello", username, "welcome to cohort 1 lucky lottery.")

def Lottery_app():
    while 1:
        usernumber = int(input("Enter any number from 0 to 50: "))
        random_number = random.randint(0, 50)
        if usernumber > 50:
            print("Your input number is more than 50, sorry you are disqualified, try agin later.")
            exit()
        elif usernumber == Winning_number == random_number:
            print("Congratulations", username,"! You  won")
        else:
            print("Sorry!", username, "you lost, please try again")

Lottery_app()
