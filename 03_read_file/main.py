from math import inf

# change file path based on your file structure
FILE_PATH = "03_read_file/data.txt"

file = open(FILE_PATH, "r")

minimum = inf
maximum = -inf
total_lines = 0
missing = 0
sum_total = 0
count = 0

for line in file:
    line = line.strip()
    line_data = float(line)

    # calculate the total number of missing values (-1)
    if line_data == -1:
        missing += 1

    else:
        # get sum and count to calculate mean of non-missing values only
        sum_total += line_data
        count += 1

        # get minimum and maximum values from the file
        if line_data < minimum:
            minimum = line_data
        elif line_data > maximum:
            maximum = line_data

    total_lines += 1

file.close()


print(f"\nTotal lines in the file = {total_lines}")
print(f"Total missing values (-1) = {missing}")
print(f"Maximum value = {maximum}")
print(f"Minimum value = {minimum}")
print(f"Mean = {sum_total/count:.2f}")
