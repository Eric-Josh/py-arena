#author: Joshua
#write a code that determines whether you are underweight, fit or overweight.
#weight in kg
#height in meters ex 1.65m.
#BMI: weight divided by height square, where weight is in kg and height is in meters.

#Rules
#if BMI <= 18.5 you are underweight
#if BMI > 18.5 and BMI <= 25 you are fit
#if BMI > 25 you are overweight
   

#declear variables
getHeight = 0.0;
getWeight = 0.0;
bodyMassIndex = 0.0;

#From this point I will ask the user for his/her information.
getHeight = float(input("Please enter your height in meter: "))
getWeight = float(input("Please enter your weight in kg: "))
#user will enter there information above and we will then calcualte.
bodyMassIndex = (getWeight * 703) / (getHeight ** 2)



if bodyMassIndex <= 18.5:
    print("Your BMI is " + str( bodyMassIndex ) + " and you are underwieght ")
elif bodyMassIndex > 18.5 & bodyMassIndex <= 25.0:
    print("Your BMI is " + str(bodyMassIndex ) + " and you are fit ")
else:
    print("Your BMI is " + str(bodyMassIndex ) + " and you are overweight ")
