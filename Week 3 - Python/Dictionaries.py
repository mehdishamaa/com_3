# What is a dictionary?:
# A bit more dynamic than tuples and lists
# Very useful tool within any coding language
# Simple concept of KEY VALUE PAIRS

# Syntax: We use {} to create a dictionary

# Let us now create an example:

student_record = { "name" : "mehdi",
                   "stream" : "DevOps",
                 "completed lesson": 5,
                 "completed_lesson_names": ["strings", "tuples", "variables"] }


# Add 2 topics that we have covered number Lists and number 2 Builtin methods

student_record["completed_lesson_names"].append("Lists")
student_record["completed_lesson_names"].append("Builtin methods")
print(student_record)


# Let us now print 2 specifics from our dictionary

print(student_record["completed_lesson_names"][0], student_record["name"])


