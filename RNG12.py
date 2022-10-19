from random import seed
from random import randint
import math
bal = int(input("enter deposit amount"))
while True:
	agn = input("Want to roll? y/n")
	if agn == "y":
		break
	elif agn == "n":
		input ("enter any key to close program")
		sys.exit
	else:
		print ("invalid input")
		continue
while agn == "y":
	num = randint(2,12)
	print (num)
	if num != 7 or 11:
		bal = bal - 2
		print(bal)
	elif num == 7 or 11:
		bal = bal + 1
		print(bal)

	while True: 
		agn = input("Roll again? y/n")
		if agn == "y":
			break
		elif agn == "n":
			input ("enter any key to close program")
			sys.exit
		else:
			print ("invalid input")
			continue
	continue	

