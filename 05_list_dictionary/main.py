from pprint import pprint
import re

FOLDER_PATH = "05_list_dictionary/"
SOURCE_FILE_NAME = "TheTortoiseAndTheHare.txt"

term_frequency_vector = {}


file = open(FOLDER_PATH + SOURCE_FILE_NAME, "r")
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


pprint(term_frequency_vector)
file.close()
