# Tuples:
# Tuples are the same as lists but IMMUTABLE
# Tuples are used for data that DO NOT need changing (e.g DOB, Passport Number)

# Syntax of Tuple: we use () to create a Tuple:

dob = ("name", "dob", "passport number")
print(dob)

# Converting the tuple into a list:

user_details = list(dob)
print(user_details)

# Add your name into the list at 0 index

user_details.insert(0, "Mehdi")
print(user_details)
