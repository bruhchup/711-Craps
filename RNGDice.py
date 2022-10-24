from random import seed
from random import randint
import time
import sys

while True:
   agn = input("Would you like to roll? y/n")
   if agn == "y":
      break
   if agn == "n":
      input("enter any key to exit")
      exit()
   else:
       print ("invalid input")
       continue
        
while agn == "y":
    roll = ["Rolling",".",".","."]
#Prints "Rolling..." out slowly to create suspense
    for word in roll:
        sys.stdout.write(word)
        time.sleep(0.35)
    print()
#Dice roll
    D1 = randint(1,6)
    print("Dice 1 rolled",D1)
    D2 = randint(1,6)
    print("Dice 2 rolled",D2)
    print("Roll is",D1 + D2)
    while True:
        agn = input("Roll again? y/n")
        if agn == "y":
            break
        elif agn == "n":
            input("Enter any key to exit")
            exit()
        else:
            print("invalid input")
            continue
    continue