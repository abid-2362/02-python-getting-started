# Dictionary
student = {
    "name": "Mark",
    "student_id": 1420,
    "feedback": None
}

# getting data from a dictionary
print("Student name is {0}".format(student["name"]))

# Changing value in a dictionary
student["feedback"] = "Genius Student"

# Now the value for feedback has been changed
print("Student's feedback is \"{0}\"".format(student["feedback"]))

# last_name does not exist, so it will raise a KeyError
# print(student["last_name"])

# Some dictionary methods
# get, keys, values

# Get a key from dictionary
# get method gets the 2nd parameter for default value if key not found in the dictionary.
student_last_name = student.get("last_name", "Unknown")

# keys method returns the keys of the dictionary
student_keys = student.keys()

# values method returns values of the dictionary
student_values = student.values()

# deleting a key value pair in the dictionary
del student["feedback"]

# List of dictionaries
all_student = [
    {"name": "Abid", "student_id": 1400},
    {"name": "Ahmad", "student_id": 1401},
    {"name": "Ashraf", "student_id": 1402}
]

# Getting the values of a dictionary list
first_student = all_student[0]
print("Frist Student is {0} with id {1}".format(first_student["name"], first_student["student_id"]))
