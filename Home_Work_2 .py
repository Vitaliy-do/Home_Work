class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
        self.courses_attached = []

    def rate_lecturer(self, lecturer, course, grade):
        if isinstance(lecturer,
                      Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'
"""
В классе Student реализован метод rate_lecturer(), который
работает только для лекторов (Lecturer).
Проверяет, что лектор прикреплен к курсу студента, а также
записывает оценки в словарь grades лектора.

"""
class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
              student.grades[course] += [grade]
            else:
              student.grades[course] = [grade]
        else:
            return 'Ошибка'
"""
Класс Reviewer преобразован в дочерный, в котором
реализован метод позволяющий ставить оценки студентам.

"""

lecture = Lecturer('Иван', 'Иванов')
reviewer = Reviewer('Пётр', 'Петров')
student = Student('Алёхина', 'Ольга', 'Ж')

student.courses_in_progress += ['Python', 'Java']
lecture.courses_attached += ['Python', 'C++']
reviewer.courses_attached += ['Python', 'C++']

print(student.rate_lecturer(lecture, 'Python', 7))  # None
print(student.rate_lecturer(lecture, 'Java', 8))  # Ошибка
print(student.rate_lecturer(lecture, 'С++', 8))  # Ошибка
print(student.rate_lecturer(reviewer, 'Python', 6))  # Ошибка

print(lecture.grades)  # {'Python': [7]}