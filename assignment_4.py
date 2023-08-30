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

# Calculate the user's height 
def get_user_height(height_feet, height_inches):
    while True:
        try:
            return (height_feet * 12) + height_inches
        except ValueError:
            print("Invalid input, enter a valid number.")

# Calculate the user's BMI
def calculate_user_bmi(weight_pounds, height):
    while True:
        try:
            return (weight_pounds / (height ** 2)) * 703
        except ValueError:
            print("Invalid input, enter a valid number.")

# Classify the user's BMI
def get_user_bmi_classification(bmi):
    if bmi < 16:
        return ("is severely underweight.  Received '" + str(bmi) + "'")
    elif bmi >= 16 and bmi < 18.5:
        return ("is underweight.  Received '" + str(bmi) + "'")
    elif bmi >= 18.5 and bmi < 25:
        return (" is healthy. Received '" + str(bmi) + "'")
    elif bmi >= 25 and bmi < 30:
        return (" is overweight. Received '" + str(bmi) + "'")
    else:
        return (" is obese. Received '" + str(bmi) + "'")

def main():
    weight_pounds = float(input("Please enter your weight in lbs: "))
    height_feet = float(input("Enter your height in feet: "))
    height_inches = float(input("Enter your height in inches: "))
    
    height = get_user_height(height_feet, height_inches)
    bmi = calculate_user_bmi(weight_pounds, height)
    
    print("Your BMI is:", bmi)
    get_user_bmi_classification(bmi)

if __name__ == "__main__":
    main()