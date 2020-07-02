# What is a function?
# A function is a re-usuable block of code


# Why should we use a function?
# It saves us from repeating ourselves, re-usuability of code

# How do we create a function?
# Create a function to greet:

# def greeting():
#    return "Hello World!"
# pass is used to skip the function
# return is used to provide an output

# However, in the above code, there is no output because the function has not been called.
# How do we call the function?

# print(greeting())

# Methods with arguments:

def add_values(number1, number2):
    return number1 + number2    # We can return anything - string - integer

print(add_values(4,7))

# Above, we have created a function that will add any two values.
# The function called add_values allows us to specify two integers which it will add together when we asl to print the function.

# Create a function with two arguments to return a subtraction of two values

def subtract_values(number1,number2):
    return number1 - number2
print(subtract_values(10,5))

# Create a function with two arguments to return a multiplication of two values

def multiply_values(number1,number2):
    return number1 * number2
print(multiply_values(5,5))

# Create a function with two arguments to return a division of two values

def divide_values(number1,number2):
    return number1 / number2
print(divide_values(25,5))

# Create a function with two arguments to return a remainder of two values

def remainder_values(number1,number2):
    return number1 % number2
print(remainder_values(36,9))

# Now we shall create a simple add function which asks for user input

def add_values(number1,number2):
    return number1 + number2
print(add_values(int(input("what is your first number?")), int(input("What is your second number?"))))







