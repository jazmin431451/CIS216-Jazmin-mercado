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
height_inches = 12
height_feet = 1
weight_pounds = 0.453592

# Ask the user for their weight in pounds

weight_pounds = float(input("Please enter your weight in lbs: "))

# Ask the user for their height in feet and inches
# calculate the user's height

height_feet = int(input("Enter your height in feet: "))
hight_inches = int(input("Enter your height in to inches: "))
height = (height_feet * 12) + height_inches

# Calculate the user's BMI

bmi = float(weight_pounds / (height ** 2)) * 703

print("your bmi is: " + str(bmi) + "and you are: " + str(bmi))