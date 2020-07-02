# What is a control flow?:

# Conditional statements and loops

# If, elif, else, for loop, while loop

# weather = "sunny"
# conditional_weather = "rainy"

# if weather = "sunny": or conditional_weather = "rainy":
 #   print("Let's go to the beach")
#else:
#    print("Sorry better luck next time")

# Excercise:
# Write 12a, PG, U, 18, 15
# Writing a program to check these



age = int(input("How old are you?"))

classifications = ["U", "PG", "12a", "15", "18"]
if age > 17:
    print("Here is what you can watch", classifications)
elif 14<age<18:
    print("Here is what you can watch", classifications[0:4])
elif 11<age<15:
    print("Here is what you can watch", classifications[0:3])
else:
    print("Here is what you can watch", classifications[0:2])

