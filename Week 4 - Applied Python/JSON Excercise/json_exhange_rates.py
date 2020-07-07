import json

with open("exchange_rates.json") as exchange_rates: # Decoding
    data = json.load(exchange_rates) # Storing data from file to car variable
    x_data = data["rates"]
    print(x_data["CAD"])

# Create Exchange_rates class


def exchange():
    c = input("Please enter the currency you wish to convert to:")
    a = input("Please enter value of currency in EUR:")
    print((x_data[c]) * int(a))

print(exchange())



# Fetch data from exchange_rates.json

# Display the data
# Display the type of data
# Method to return the exchange rate
# Display exchange rate with specific currencies
