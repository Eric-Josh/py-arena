#ask user how many items did they put in their cart?
#input the price for each item independenly
#print the total price for each item

#declear variables
getCountOfItem = 0.0
getAmountPerItem = 0.0
getTotal=[]

getCountOfItem = float(input("Please enter count of item added to cart: "))

while getCountOfItem > 0:

	getAmountPerItem = float(input("Please enter price for item %d: " % getCountOfItem))

	getTotal.append(getAmountPerItem)

	getCountOfItem = getCountOfItem - 1
		
	if(getCountOfItem == 0):

		sumUp = sum(getTotal)
		print("Your total price for items purchased is: " + str(sumUp))