from random import seed
from random import randint

while True:
   agn = input("Would you like to roll? y/n")
   if agn == "y":
      break
   if agn == "n":
      input("enter an key to exit")
      exit()
   else:
       print ("invalid input")
       continue
        
while agn == "y":
    print ("RNG Dice")
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