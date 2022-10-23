from random import seed
from random import randint

bal = 500
print("your balance is",bal)
while True:
    try:
        while True:
            bet = float(input("enter bet amount"))
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
    flip = randint(1,2)
    if flip == 1:
        print ("you win!")
        bal = bal + bet * 0.5
        print("your balance is now",bal)
    elif flip == 2:
        print ("you lose.")
        bal = bal - bet
        print("your balance is now",bal)
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