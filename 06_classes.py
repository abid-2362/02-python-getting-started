students = []


class Student:
    def __init__(self, name, student_id=345):
        student = {"name": name, "student_id": student_id}
        students.append(student)

    def __str__(self):
        return "Student Class"


mark = Student("Abid")
print(mark)
