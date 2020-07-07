# What is JSON?
# Javascript Object Notation

# Syntax: JSON is a syntax for exchanging data
# Where and how?: Between a browser and server
# What type of data?: The data can only be text
# How is data stored?: Data is stored using key value pairs

import json

# encoding from dictionary and writing to jsonfile
car_data = {"name": "tesla", "engine":"electric"} #dictionary
print(car_data)

# checking type of dictionary

print(type(car_data))

# Let us now change Python dictionary to JSON string

car_data_json_string = json.dumps(car_data)

print(type(car_data_json_string))

# Let's create a JSON file with writing permission



with open("new_json_file.json", "w") as jsonfile:
    json.dump(car_data, jsonfile)  # json.dump takes two arguments
    # "name of file", "permission type"
    # The first is the dictionary, the second is file_type on this occasion jsonfile

    # Reading from the file we just created

with open("new_json_file.json") as jsonfile: # Decoding
    car = json.load(jsonfile) # Storing data from file to car variable
    print(type(car))





