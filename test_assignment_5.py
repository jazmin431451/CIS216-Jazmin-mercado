import unittest
from assignment_5 import BMI

class TestBMI(unittest.TestCase):

    def test_valid_calculate_user_bmi_pounds(self):
        user_bmi = BMI(feet=5, inches=8, pounds=150)
        self.assertAlmostEqual(user_bmi.calculate_user_bmi, 22.8, places=1)

    def test_valid_calculate_user_bmi_kilograms(self):
        user_bmi = BMI(meters=1.73, kilograms=68)
        self.assertAlmostEqual(user_bmi.calculate_user_bmi, 22.7, places=1)

    def test_invalid_get_user_height(self):
        user_bmi = BMI(feet=-8, inches=8, pounds=300)
        self.assertEqual(user_bmi.calculate_user_bmi, 27.23398760330579, 
        "BMI calculation failed", )

    def test_invalid_calculate_user_bmi(self):
        user_bmi = BMI(meters=1.73, kilograms=-68)
        self.assertEqual(user_bmi.calculate_user_bmi, -22.720438370810918, 
        "BMI calculation failed", )

if __name__ == '__main__':
    unittest.main()