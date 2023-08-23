"""This program converts weight and it calculate BMI what level your weight is.

Input:
    BMI what level of weight you are

Output:
    the user's need to give whati is you feet and inches 
    the user's need to put in what wieght the are in lb

example:
    enter your weight and height:
    130 and 5'3 ft
    resulting from mass in kilograms and 
height in meters is healthy (bmi= 23.025951121189216)

Todo:
    * ask there weight in lbs and their height in feet and inches 
    * calculate and display their BMI and also include the display of the value
range for underweight,normal and overweight.
    * also make sure the source in BMI is in range recommendations.
    
References:
    * https://en.wikipedia.org/wiki/Body_mass_index
    * https://www.mathsisfun.com/metric-imperial-conversion-charts.html
    * https://www.w3schools.com/python/python_syntax.asp

"""
# Ask the user for their weight in pounds
weight_pounds = float(input("Please enter your weight in lbs: "))

# Ask the user for their height in feet and inches
height = int(input("Enter your height in feet: "))

# Calculate the user's BMI
bmi = float(weight_pounds) / (height * 12) * 703

# Classify the user's BMI
if bmi < 16:
    print("severely underweight")
else:
    if bmi >= 16 and bmi < 18.5:
        print("underweight")
    else:
        if bmi >= 18.5 and bmi < 25:
            print("healthy")
        else:
            if bmi >= 25 and bmi < 30:
                print("overweight")
            else:
                if bmi >= 30:
                    print("obese")

print("your bmi is: " + str(bmi) + "and you are: " + str(bmi))