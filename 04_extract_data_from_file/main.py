"""

Author: Mohit Dhungana
Assignment: Construct a program to copy all records with a user entered integer value 
            found in field X4 to a new file. 
            
"""

FOLDER_PATH = "04_extract_data_from_file/"
SOURCE_FILE_NAME = "moxy.csv"
DESTINATION_FILE_NAME = "output.csv"
CSV_HEADER = "X4"


result_list = []


file = open(FOLDER_PATH + SOURCE_FILE_NAME, "r")
lines = file.readlines()


user_input = input(
    f"Enter the integer value for {CSV_HEADER} field to be used to copy data: "
)


# get header of CSV file
csv_header = lines.pop(0).split(",")
index_of_header = csv_header.index(CSV_HEADER)


for line in lines:
    line = line.split(",")

    # compare user input to our field
    if line[index_of_header] == user_input:
        # convert list back to string then append to the result list
        result_list.append(",".join(line))


output_file = open(FOLDER_PATH + DESTINATION_FILE_NAME, "w")

# write header of the output csv file
output_file.write(",".join(csv_header))

if len(result_list) > 0:
    # write results to csv body
    output_file.writelines(result_list)
    print(f"Success!!!! \nWrote {len(result_list)} records to file")
else:
    print(f"No data found!!! \nPlease select a valid data for {CSV_HEADER} field")


# close all open files
output_file.close()
file.close()
