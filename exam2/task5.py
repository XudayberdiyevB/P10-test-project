from task1 import Student


class Internship(Student):
    def __init__(self, firstname, lastname, age, region, university, subjects, **kwargs):
        super().__init__(firstname, lastname, age, region, university, subjects)
        self.extra_data = kwargs

    def get_info(self):
        student_info = super().get_info()
        return f"{student_info}\n\nExtra info: {self.extra_data}"
