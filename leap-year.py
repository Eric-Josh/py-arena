# leap year within every 4 years
# all leap year from 2000 till when the year the user inputs

getUserYear = 0

getUserYear = int(input("Kindly enter a year from 2000 and above: "))
print("\nList of Leap year between 2000 and "+ str(getUserYear) + " are :")

for year in range(2000, getUserYear):
	#check if the year is a Leap year if yes print
	if (0 == year % 4) and (0 != year % 100) or (0 == year % 400):
		print(year)
        