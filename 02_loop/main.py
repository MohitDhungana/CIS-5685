initial_organism_count = int(input("What is the initial number of organisms?: "))
growth_rate = float(input("Enter the rate of growth (a real number > 1): "))
growth_period = int(input("Enter the number of hours to achieve the rate of growth: "))
total_growing_time_hrs = int(input("Enter the total hours of growth: "))


total_growth_period = total_growing_time_hrs / growth_period


while total_growth_period > 0:
    initial_organism_count *= growth_rate
    total_growth_period -= 1

print(f"Total population is: {initial_organism_count}")
