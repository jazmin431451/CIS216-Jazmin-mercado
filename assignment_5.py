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
# The InvalidParameterError custom exception class is defined to handle invalid parameters.
class InvalidParameterError(Exception):
    pass

# Input validation is added to ensure that the entered values are valid numbers and within an acceptable range.
class BMI:
    def __init__(self, feet=0, inches=0, kilograms=0, meters=0, pounds=0):
        self.feet = feet
        self.inches = inches
        self.kilograms = kilograms
        self.meters = meters
        self.pounds = pounds

# Parameter validation is integrated into properties and methods to ensure valid parameters are passed.       
    @property
    def get_user_height(self):
        if not isinstance(self.feet, (int, float)) or not isinstance(self.inches, (int, float)):
            raise InvalidParameterError("Height parameters must be numeric")
        return (self.feet * 12) + self.inches

# Assertions are used to validate assumptions during program execution.   
    @property
    def calculate_user_bmi(self):
        if not (isinstance(self.kilograms, (int, float)) or isinstance(self.pounds, (int, float))):
            raise InvalidParameterError("Weight parameters must be numeric")
        
        if self.kilograms and self.meters:
            return self.kilograms / (self.meters ** 2)
        elif self.pounds and self.get_user_height:
            return (self.pounds / (self.get_user_height ** 2)) * 703
        else:
            return None
# Exception handling is implemented to catch errors and provide appropriate error messages.
def main():
    try:
        weight_pounds = float(input("Please enter your weight in lbs: "))
        height_feet = float(input("Enter your height in feet: "))
        height_inches = float(input("Enter your height in inches: "))
        
        if weight_pounds <= 0 or height_feet <= 0 or height_inches < 0:
            raise InvalidParameterError("Invalid input values")
        
        user_bmi = BMI(feet = height_feet, inches = height_inches, pounds = weight_pounds)
        
        assert user_bmi.calculate_user_bmi is not None, "BMI calculation failed"
        
        print("Your BMI is:", user_bmi.calculate_user_bmi)
        
    except ValueError:
        print("Invalid input. Please enter numeric values.")
    except InvalidParameterError as e:
        print("Error:", e)
    except AssertionError as e:
        print(e)

if __name__ == "__main__":
    main()
