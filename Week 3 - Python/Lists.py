# Data Collection

# Syntax of list: [list] square brackets (tuple) {dictionary - key:value}
# Tuples are immutable

# Let's create a list

cities = ["Tokyo", "Paris", "Prague", "Luxembourg"]

# Let's print Luxembourg:

print(cities[3])

# Let's switch Luxembourg for Amsterdam:

cities[3] = "Amsterdam"

print(cities)

# Let's add a city to the list:

cities.append("Vilnius")

# Let's remove a city from our list:

cities.remove("Paris")
print(cities)
