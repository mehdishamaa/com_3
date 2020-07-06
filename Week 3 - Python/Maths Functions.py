# How can we use the builtin Python HW library?

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

# def cm_to_inches (inches):
#    return inches * 2.54
# print(cm_to_inches(int(input("How many inches would you like to convert?"))))


# Let us now create a class with key word called class
# The naming convention for creating a class is to capitalise the first letter

# class Python_Calculator:

#   def add_values(self, num1, num2): # Self key word refers to the class


# Let us now create the calculator inside the class:

print("Press 1 for Addition")
print("Press 2 for Subtraction")
print("Press 3 for Multiplication")
print("Press 4 for division")

class Python_Calculator:
    def add_values(self, num1, num2):
        return num1 + num2

    def subtract_values(self, num1, num2):
        return num1 - num2

    def multiply_values(self, num1, num2):
        return num1 * num2

    def divide_values(self, num1, num2):
        return num1 / num2



    print(int(input("Please choose your operation:")))
    if input == 1:
        object.add_values(num1, num2)
    elif input == 2:
        object.subtract_values(num1, num2)
    elif input == 3:
        object.multiply_values(num1, num2)
    elif input == 4:
        object.divide_values(num1, num2)


num1 = print(int(input("Please input your first number")))
num2 = print(int(input("Please input your second number")))


















