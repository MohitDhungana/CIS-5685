"""
Program: bmi.py
Author: Mohit Dhungana
Last date modified: 3/20/2023
The purpose of this program is to compute an individual's Body Mass Index (BMI)
based on their height in inches and weight in pounds.
"""


def imperial_to_metric(imperial_unit, conversion_rate):
    """converts imperial unit to metric unit"""
    return imperial_unit / conversion_rate


def calculate_bmi(weight, heigh):
    """returns calculated BMI"""
    return weight / heigh**2


def main():
    """The main function for this script"""
    LBS_PER_KG = 2.2046
    INCHES_PER_METER = 39.3701

    weight_lbs = float(input("Please enter weight (pounds): "))
    height_in = float(input("Please enter height (inches): "))

    weight_kg = imperial_to_metric(weight_lbs, LBS_PER_KG)
    height_m = imperial_to_metric(height_in, INCHES_PER_METER)

    bmi = calculate_bmi(weight_kg, height_m)

    print("BMI is", bmi)


if __name__ == "__main__":
    main()
