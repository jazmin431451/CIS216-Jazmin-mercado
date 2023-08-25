import pytest
import assignment_2

def test_get_user_height():
    assert assignment_2.get_user_height(5, 3) == 63
    assert assignment_2.get_user_height(5, 2) == 62
    assert assignment_2.get_user_height(6, 3) == 75
    assert round(assignment_2.get_user_height(6, 4), 1) == 76

def test_calculate_user_bmi():
    assert round(assignment_2.calculate_user_bmi(140, 63), 1) == 24.8
    assert round(assignment_2.calculate_user_bmi(200, 62), 1) == 36.6
    assert round(assignment_2.calculate_user_bmi(120, 75), 1) == 15.0
    assert round(assignment_2.calculate_user_bmi(130, 76), 1) == 15.8

# Additional test cases

