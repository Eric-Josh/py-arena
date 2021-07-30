# Determine Interim Grade Letter.
# The program allows the Subject Coordinator to type in a student’s 3 assessment marks separated by a comma.
# This was based on some business rules.

marksInput = input('Enter a student\'s assessment marks (separated by comma): ')

# seperate each mark using split
marksList = marksInput.split(",")

# convert each mark from string to a number using float
mark1 = float(marksList[0])
mark2 = float(marksList[1])
mark3 = float(marksList[2])

finalMark = round(mark1 * 20/100 + mark2 * 40/100 + mark3 * 40/100)

# Add mark1-3 to a list
list = [mark1, mark2, mark3]
lowMarkCheck = 0

for i in list:
    if i < 50:
        lowMarkCheck += 1

# Interim grade use case conditions
if list.count(0) >= 2 and finalMark <= 44:
    print('Interim Grade is AF')
elif list.count(0) == 1 and finalMark <= 44:
    print('Interim Grade is F')
elif list.count(0) == 1 and 45 < finalMark < 49:
    print('Interim Grade is F')
elif lowMarkCheck == 2 and 45 < finalMark < 49:
    print('Interim Grade is F')
elif mark3 < 50 and 45 < finalMark < 49:
    print('Interim Grade is SE')
elif mark1 < 50 or mark2 < 50 and 45 < finalMark < 49:
    print('Interim Grade is SA')
elif 50 < finalMark < 64:
    print('Interim Grade is P')
elif 65 < finalMark < 74:
    print('Interim Grade is C')
elif 75 < finalMark < 84:
    print('Interim Grade is D')
elif 85 < finalMark < 100:
    print('Interim Grade is HD')
    
