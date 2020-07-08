import requests
import json

post_codes_req = requests.get("https://api.postcodes.io/postcodes/se120nb")

print(post_codes_req.json())
json_data = post_codes_req.json()


class JSONReader:
    def get_all_values(self, nested_values):      # Here we use recursion to loop through all nested values
        for key, value in nested_values.items():
            if type(value) is dict:
                self.get_all_values
            else:
                print(key, ":", value)

json_reader = JSONReader()
json_reader.get_all_values(type_json)



# Fetch data by key value pairs within dictionaries
# Create a function to return key:value
# Create a class and move the code block inside the class





