from task1 import students


def get_students_age_gte_20(student_objects):
    result = []

    for student in student_objects:
        if student.age >= 20:
            result.append(f"{student.firstname} {student.lastname}")

    return result


print(get_students_age_gte_20(students))
