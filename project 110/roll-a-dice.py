import random


response = str("y")

while response == "y":
	no = random.randint(1,6)
	
	if no == 1:
		print("1")
	if no == 2:
		print("2")
	if no == 3:
		print("3")
	if no == 4:
		print("4")
	if no == 5:
		print("5")
	if no == 6:
		print("6")
	
		
	response=str(input("press y to roll again and n to exit:"))

    
	


    