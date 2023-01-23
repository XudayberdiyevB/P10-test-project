import random


class Student:
    def __init__(self, firstname, lastname, age, region, university, subjects: dict) -> None:
        self.firstname = firstname
        self.lastname = lastname
        self.age = age
        self.region = region
        self.university = university
        self.subjects = subjects
        self.gpa = self.get_gpa()

    def get_gpa(self) -> float:
        return round(sum(self.subjects.values()) / len(self.subjects.values()), 2)

    def get_info(self) -> str:
        data = f"Ф.И.О: {self.to_upper(self.firstname)} {self.lastname}\nВозраст: {self.age}\n" \
               f"Регион: {self.region}\nУниверситет: {self.university}\n" \
               f"Предметы: {', '.join(self.subjects.keys())}\nСредная оценка: {self.gpa}"
        return data

    @staticmethod
    def to_upper(name):
        return name.upper()

    @staticmethod
    def obj_generator(firstnames, lastnames, regions, universities, subjects) -> list:
        return [
            random.choice(firstnames),
            random.choice(lastnames),
            random.randint(18, 30),
            random.choice(regions),
            random.choice(universities),
            subjects
        ]


# 10 ta student yaratish
first_names = ['Хуршид', 'Умид', 'Даврон', 'Рано', 'Нумонбек']
last_names = ['Хайитбоев', 'Хайитбоев', 'Хайдаров', 'Шодиев', 'Вулиев']
university_names = ['Тату', 'Вест', 'Инха', 'Туит', 'Авиация']
region_names = ['Ташкент', 'Андижан', 'Шимкент', 'Фергана', 'Бухара']
subjects_data = {
    'Английский Язык': random.randint(2, 5),
    'Математика': random.randint(2, 5),
    'Физика': random.randint(2, 5),
}

students = [
    Student(*Student.obj_generator(
        first_names, last_names, region_names, university_names, subjects_data
    ))
    for _ in range(10)
]
