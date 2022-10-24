from random import seed
from random import randint

print("50/50 gamble")
print("Rules: Roll a 1 to win. Roll a 2 to lose.")

#Preset user balance of 1000      
bal = 1000
print("your balance is",bal)

while True:
    quit = input("enter any key except q to continue.")
    if quit != "q":
        break
    while quit == "q":
        sure = input("are you sure? y/n")
        if sure == "y":
            input("enter any key to exit")
            exit()
        elif sure == "n":
            break
        else:
            print("invalid input")

while True:
    try:
        while True:
            bet = float(input("enter bet amount"))
            bet = round(bet,2)
            if bet > bal:
                print("insufficient balance")
                continue
            elif bet < 0:
                print("cannot bet below 0")
                continue
            else:
                break
    except:
            ValueError
            print ("invalid input")
            continue
    print("bet is",bet)
    flip = randint(1,2)
    if flip == 1:
        print ("Rolled a 1. You win!")
        bal = bal + bet * 0.5
#Rounds bet to two decimals if the number is longer
        bal = round(bal,2)
        print("your balance is now",bal)
    elif flip == 2:
        print ("Rolled a 2. You lose.")
        bal = bal - bet
        bal = round(bal,2)
        print("Your balance is now",bal,".")
    while True:
        agn = input("play again? y/n")
        if agn == "y":
            break
        elif agn == "n":
            input("enter any key to exit")
            exit()
        else:
            print("invalid input")
            continue
    continue