student = {
    "name": "Abid",
    "student_id": 1400,
    "feedback": None
}

# Exception handling
try:
    last_name = student["last_name"]
except KeyError as error:
    print("Error finding the last_name ");
    print(error)
except TypeError as error:
    print("Type error occurred ")
    print(error)
except Exception as error:
    print("Unknown error occurred ")
    print(error)

print("code executes to this point")
