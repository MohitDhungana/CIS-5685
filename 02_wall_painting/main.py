from math import ceil


PAINT_COVERAGE = 350
DOORWAY_COVERAGE = 14
WINDOW_COVERAGE = 8.5


try:
    wall_length = float(input("What is the length of the wall in feet? "))
    wall_height = float(input("What is the height of the wall in feet? "))
    door_count = float(input("How many doors are there in the room? "))
    window_count = float(input("How many windows are there in the room? "))
    cost_per_gallon = float(input("What is the price of paint? "))

    def get_coverage_area(coverage, count):
        return coverage * count

    door_area = get_coverage_area(DOORWAY_COVERAGE, door_count)
    window_area = get_coverage_area(WINDOW_COVERAGE, window_count)

    wall_area = wall_length * wall_height

    actual_paint_area = wall_area - window_area - door_area

    gallons_paint_needed = ceil(actual_paint_area / PAINT_COVERAGE)
    cost = round(cost_per_gallon * gallons_paint_needed, 2)

    print("cost_per_gallon", cost_per_gallon)
    print("gallons_paint_needed", gallons_paint_needed)

    print(f"\nArea of wall to be painted is {actual_paint_area} sqft.")
    print(f"You need {gallons_paint_needed} gallons of paint which will cost ${cost}")


except ValueError:
    print("Input can only be numbers!!!!!")
