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
    * https://www.youtube.com/watch?v=AEOuYv699K4
    * https://www.youtube.com/watch?v=jCzT9XFZ5bw
    * https://www.youtube.com/watch?v=AsafkCAJpJ0
    
"""
# what I did in this code, the BMI class encapsulates the properties related to BMI calculation and conversion between different units. 
# The @property decorators are used to define class properties (height and bmi) that can be accessed like attributes. 
# The constructor (__init__) takes optional named parameters for feet, inches, kilograms, meters, and pounds.
# The bmi property calculates the BMI based on either kilograms/meters or pounds/height.
class BMI:
    def __init__(self, feet=0, inches=0, kilograms=0, meters=0, pounds=0):
        self.feet = feet
        self.inches = inches
        self.kilograms = kilograms
        self.meters = meters
        self.pounds = pounds
        
    @property
    def height(self):
        return (self.feet * 12) + self.inches
    
    @property
    def bmi(self):
        if self.kilograms and self.meters:
            return self.kilograms / (self.meters ** 2)
        elif self.pounds and self.height:
            return (self.pounds / (self.height ** 2)) * 703
        else:
            return None
#The main function now creates an instance of the BMI class using the provided input values and 
# accesses the bmi property to get the calculated BMI. 
# This approach helps encapsulate the functionality within the class and avoids the use of global variables and functions.
def main():
    weight_pounds = float(input("Please enter your weight in lbs: "))
    height_feet = float(input("Enter your height in feet: "))
    height_inches = float(input("Enter your height in inches: "))
    
    user_bmi = BMI(feet=height_feet, inches=height_inches, pounds=weight_pounds)
    
    print("Your BMI is:", user_bmi.bmi)
    
if __name__ == "__main__":
    main()