import random
x='Y'
while x=='y':
	num=random.randint(1,6)
	if num==1:
		print("-------------")
		print("|           |")
		print("|     o     |")
		print("|           |")
	if(num==2):
		print("-------------")
		print("|           |")
		print("| o       o |")
		print("|           |")
	if(num==3):
		print("-------------")
		print("|     o    |")
		print("|     o    |")
		print("|     o    |")
	if(num==4):
		print("-------------")
		print("| o       o |")
		print("|           |")
		print("| o       o |")
	if(num==5):
		print("-------------")
		print("| o       o |")
		print("|     o     |")
		print("| o       o |")
	if(num==6):
		print("-------------")
		print("| o       o |")
		print("| o       o |")
		print("| o       o |")
	x=input('\npress y to roll again \n')
