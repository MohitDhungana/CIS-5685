"""
Author: Mohit Dhungana
Assignment: Create a program to find the term frequency vector of a document
            stored in a text file TheTortoiseAndTheHare.txt
"""
import re


term_frequency_vector = {}


file_name = input("Enter filename: ")
file = open(file_name, "r")
lines = file.readlines()


for each_line in lines:
    each_line = each_line.lower()
    words = each_line.split(" ")

    for each_word in words:
        # remove all characters except alphanumeric characters
        clean_word = re.sub("[^A-Za-z0-9]+", "", each_word)

        # dont count empty strings
        if clean_word == "":
            continue

        # if key exists, increment it, else initialize it to 1
        if clean_word in term_frequency_vector:
            term_frequency_vector[clean_word] += 1
        else:
            term_frequency_vector[clean_word] = 1


sorted_keys = sorted(list(term_frequency_vector.keys()))


print(f"There are {len(sorted_keys)} unique terms")


for key in sorted_keys:
    print(f"{term_frequency_vector[key]} {key}")


file.close()
