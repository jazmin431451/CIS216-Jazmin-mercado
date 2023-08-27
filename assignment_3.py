height_inches = 12
height_feet = 1
weight_pounds = 0.453592

# Calculate the user's height 
def get_user_height(height_feet, height_inches):
    return (height_feet * 12) + height_inches

# Calculate the user's BMI
def calculate_user_bmi(weight_pounds, height):
    return (weight_pounds / (height ** 2)) * 703

# Classify the user's BMI
def get_user_bmi_classification(bmi):
    if bmi < 16:
        print("severely underweight")
    elif bmi < 18.5:
        print("underweight")
    elif bmi < 25:
        print("healthy")
    elif bmi < 30:
        print("overweight")
    else:
        print("obese")

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