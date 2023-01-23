from task1 import students

with open("students.txt", "w") as f:
    for student in students:
        f.write(f"{student.get_info()}\n\n")
