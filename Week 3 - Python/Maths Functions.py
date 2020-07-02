# How can we use the builtin Python library?

from random import random
import math #import built in modules


# To generate a random number:

# print(random())

# To round float numbers:

# float_num = 24.4 #float
# print(math.ceil(float_num))
# print(math.floor(float_num))
# print(math.pi)


# Let's create a method that would take 1 argument
# Calculate inches into cm

def cm_to_inches (inches):
    return inches * 2.54
print(cm_to_inches(int(input("How many inches would you like to convert?"))))

