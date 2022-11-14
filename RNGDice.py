from random import seed
from random import randint
import time
import sys

print("7/11 Craps")
print()
print("Rules: Roll a 7 or 11 to win. Roll a 2,3, or 12 to lose.")
print("If none of these numbers are rolled, The point is set")
print("on the number rolled. Roll the point before a 7 to win.")
print()
#Preset user balance of 1000      
bal = 1000
print("your balance is",bal)
print()

while True:
    quit = input("enter any key except q to continue.")
    if quit != "q":
        break
    while quit == "q":
        print()
        sure = input("are you sure? y/n")
        if sure == "y":
            print()
            print("Thank you for playing!")
            print()
            input("enter any key to exit")
            exit()
        elif sure == "n":
            print()
            break
        else:
            print()
            print("invalid input")
print()
while True:
   agn = input("Would you like to roll? y/n")
   if agn == "y":
      break
   if agn == "n":
      print()
      print("Thank you for playing!")
      input("enter any key to exit")
      exit()
   else:
       print ("invalid input")
       continue
while True:
    try:
         while True:
            print()
            bet = float(input("enter bet amount"))
            bet = round(bet,2)
            print()
            if bet > bal:
                print("insufficient balance")
                continue
            elif bet < 0:
                print()
                print("cannot bet below 0")
                continue
            else:
                break
    except:
        ValueError
        print ("invalid input")
        continue
    print("bet is",bet)
    print()
    
    while agn == "y":
        roll = ["Rolling",".",".","."]
#Prints "Rolling..." out slowly to create suspense
        for word in roll:
            sys.stdout.write(word)
            time.sleep(0.35)
        print()
        print()
#Dice roll
        D1 = randint(1,6)
        print("Dice 1 rolled",D1)
        D2 = randint(1,6)
        print("Dice 2 rolled",D2)
        D = (D1 + D2)

        if D == 7:
            print("Rolled a ",D,", you win!",sep="")
            print()
            bal = bal + bet
            bal = round(bal,2)
            print("Your balance is now ",bal)
        elif D == 11: 
            print("Rolled an ",D,", you win!",sep="")
            print()
            bal = bal + bet
            bal = round(bal,2)
            print("Your balance is now ",bal)
        elif (D == 2) or (D == 3) or (D == 12):
            print("Rolled a ",D,", you lose!",sep="")
            print()
            bal = bal - bet
            bal = round(bal,2)
            print("Your balance is now ",bal)
        else:
             if D == 8:
                print("Rolled an ",D,", roll again.",sep="")
             else:
                print("Rolled a ",D,", roll again.",sep="")

             while True:
                print()
                for word in roll:
                    sys.stdout.write(word)
                    time.sleep(0.7)
                print()
                print()
                point = D
                D_1 = randint(1,6)
                print("Dice 1 rolled",D_1)
                D_2 = randint(1,6)
                print("Dice 2 rolled",D_2)
                D_ = (D_1 + D_2)

                if (D_ == point != 8):
                    print("Rolled a ",D_,", you win!",sep="")
                    bal = bal + bet
                    bal = round(bal,2)
                    print()
                    print("Your balance is now ",bal,)
                    break
                elif (D_ == point == 8):
                    print("Rolled an ",D_,", you win!",sep="")
                    bal = bal + bet
                    bal = round(bal,2)
                    print()
                    print("Your balance is now ",bal)
                    break
                elif D_ == 7:
                    print("Rolled a ",D_,", you lose",sep="")
                    bal = bal - bet
                    bal = round(bal,2)
                    print()
                    print("Your balance is now ",bal)
                    break
                else:
                    print()
                    if (D_ == 8) or (D_ == 11):
                        print("Rolled an ",D_,", roll again.",sep="")
                    else:
                        print("Rolled a ",D_,", roll again.",sep="")
                    continue

        while True:
            print()
            agn = input("Roll again? y/n")
            print()
            if agn == "y":
                try:
                    while True:
                        bet = float(input("enter bet amount"))
                        bet = round(bet,2)
                        print()
                        if bet > bal:
                            print()
                            print("insufficient balance")
                            continue
                        elif bet < 0:
                            print()
                            print("cannot bet below 0")
                            continue
                        else:
                            break
                except: 
                    ValueError
                    print ("invalid input")
                    continue
                print("bet is",bet)
                print()
                break
            elif agn == "n":
              print("Thank you for playing!")
              print()
              input("Enter any key to exit")
              exit()
            else:
                print("invalid input")
                continue
    continue