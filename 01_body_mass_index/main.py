INCH_TO_METERS_RATE = 0.0254
POUND_TO_KG_RATE = 0.45359237


try:
    height_inches = float(input("Enter your height in inches: "))
    weight_inches = float(input("Enter your weight in pounds: "))

    height_meters = INCH_TO_METERS_RATE * height_inches
    weight_kg = POUND_TO_KG_RATE * weight_inches

    body_mass_index = round(weight_kg / (height_meters**2), 2)

    print("Your BMI is:", body_mass_index)

    if body_mass_index < 18.5:
        print("Your BMI is in underweight range")

    elif body_mass_index >= 18.5 and body_mass_index <= 24.9:
        print("Your BMI is in healthy range")

    elif body_mass_index >= 25.0 and body_mass_index <= 29.9:
        print("Your BMI is in overweight range")

    else:
        print("Your BMI is in obese range")


except ValueError:
    print("Input can only be numbers!!!!!")
