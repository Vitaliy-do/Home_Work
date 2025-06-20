
class Student:     # Создан класс Student с соответствующими атрибутами.
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    """
    В классе Student реализован метод rate_lecturer(), который
    работает только для лекторов (Lecturer).
    Данный метод проверяет, что лектор прикреплен к курсу студента, а также
    записывает оценки в словарь grades лектора.

    """
    def rate_lecturer(self, lecturer, course, rate):
        if isinstance(lecturer,
                      Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached:
            if course in lecturer.rates:
                lecturer.rates[course] += [rate]
            else:
                lecturer.rates[course] = [rate]
        else:
            return 'Ошибка'

    def average_score(self):  # Создан метод, который определяет среднюю оценку за домашнее задание студента.
        middle_sum = 0
        for course_grades in self.grades.values():
            course_sum = 0
            for grade in course_grades:
                course_sum += grade
            middle_of_course = course_sum / len(course_grades)
            middle_sum += middle_of_course
        if middle_sum == 0:
            return f'Студент еще не получал оценки'
        else:
            return f'{middle_sum / len(self.grades.values()):.2f}'


    def __str__(self): # Применен магический метод который возвращает строковое представление объекта.
        return (f'Имя: {self.name}\n'
                f'Фамилия: {self.surname}\n'
                f'Средняя оценка за домашнее задания: {self.average_score()}\n'
                f'Курсы в процессе изучения: {self.courses_in_progress}\n'
                f'Завершенные курсы: {self.finished_courses}\n')

    def __lt__(self, student): # Применен магический медот сравнения между объектами.
        if not isinstance(student, Student):
            print(f'Такого студента нет')
            return
        return self.average_score() < student.average_score()

class Mentor:  # Создан родительский класс Mentor.
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []
        self.rates = {}

class Lecturer(Mentor): # Создан дочерный класс Lecturer у которого родительский класс Mentor.

    def middle_rate(self):  # Реализован метод позволяющий ставить оценки студентам.
        middle_sum = 0
        for course_grades in self.rates.values():
            course_sum = 0
            for grade in course_grades:
                course_sum += grade
            middle_of_course = course_sum / len(course_grades)
            middle_sum += middle_of_course
        if middle_sum == 0:
            return f'Оценки еще не выставлялись'
        else:
            return f'{middle_sum / len(self.rates.values()):.2f}'

    def __str__(self):  # Применен магический метод который возвращает строковое представление объекта.
        return (f'Имя: {self.name}\n'
                f'Фамилия: {self.surname}\n'
                f'Средняя оценка за лекции: {self.middle_rate()}\n')

    def __lt__(self, lecturer): # Применен магический медот сравнения между объектами.
        if not isinstance(lecturer, Lecturer):
            print(f' Такого лектора нет')
            return
        return self.middle_rate() < lecturer.middle_rate()

class Reviewer(Mentor): # Создан дочерный класс Reviewer у которого родительский класс Mentor.

    def rate_hw(self, student, course, grade): # Реализован метод позволяющий выставлять Reviewer оценки студентам за домашние задания.
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):  # Применен магический метод который возвращает строковое представление объекта.
        return (f'Имя: {self.name}\n'
                f'Фамилия: {self.surname}\n')

"""
Реализована функция подсчета средней оценки за домашние задания по всем студентам в рамках конкретного курса.

"""
def grades_students(students_list, course):
    overall_student_rating = 0
    lectors = 0
    for listener in students_list:
        if course in listener.grades.keys():
            average_student_score = 0
            for grades in listener.grades[course]:
                average_student_score += grades
            overall_student_rating = average_student_score / len(listener.grades[course])
            average_student_score += overall_student_rating
            lectors += 1
    if overall_student_rating == 0:
        return f'Оценок по этому предмету нет'
    else:
        return f'{overall_student_rating / lectors:.2f}'

"""
Реализована функция подсчета средней оценки за лекции всех лекторов в рамках курса.

"""
def grades_lecturers(lecturer_list, course): #
    average_rating = 0
    b = 0
    for lecturer in lecturer_list:
        if course in lecturer.rates.keys():
            lecturer_average_rates = 0
            for rate in lecturer.rates[course]:
                lecturer_average_rates += rate
            overall_lecturer_average_rates = lecturer_average_rates / len(lecturer.rates[course])
            average_rating += overall_lecturer_average_rates
            b += 1
    if average_rating == 0:
        return f'Оценок по этому предмету нет'
    else:
        return f'{average_rating / b:.2f}'

"""
Созданы объекты классов "Student", Lecturer и Reviewer с соответсвующей вводной информацией. 

"""
student_1 = Student('Александр', 'Пушкин', 'Male')
student_1.finished_courses = ['Python', 'C++']
student_1.courses_in_progress = ['Git', 'Java']

student_2 = Student('Анна', 'Каренина', 'Female')
student_2.finished_courses = ['С++', 'Git']
student_2.courses_in_progress = ['Python', 'Java']
students_list = [student_1, student_2]

lecturer_1 = Lecturer('Лев', 'Толстой')
lecturer_1.courses_attached = ['Git', 'Java']

lecturer_2 = Lecturer('Сергей', 'Есенин')
lecturer_2.courses_attached = ['Python']
lecturer_list = [lecturer_1, lecturer_2]

reviewer_1 = Reviewer('Максим', 'Горкий')
reviewer_1.courses_attached = ['Python', 'С++', 'Java', 'Git']

reviewer_2 = Reviewer('Владимир', 'Ленин')
reviewer_2.courses_attached = ['Git', 'Python', 'С++']

reviewer_1.rate_hw(student_1, 'Git', 9)
reviewer_1.rate_hw(student_1, 'Git', 7)
reviewer_1.rate_hw(student_1, 'Git', 10)
reviewer_1.rate_hw(student_1, 'Java', 5)
reviewer_1.rate_hw(student_1, 'Java', 8)
reviewer_1.rate_hw(student_1, 'Java', 9)
reviewer_1.rate_hw(student_1, 'Python', 9)
reviewer_1.rate_hw(student_1, 'Python', 3)
reviewer_1.rate_hw(student_1, 'Python', 2)
reviewer_1.rate_hw(student_1, 'С++', 10)
reviewer_1.rate_hw(student_1, 'С++', 9)
reviewer_1.rate_hw(student_1, 'С++', 4)

reviewer_2.rate_hw(student_2, 'С++', 4)
reviewer_2.rate_hw(student_2, 'С++', 2)
reviewer_2.rate_hw(student_2, 'С++', 3)
reviewer_2.rate_hw(student_2, 'Git', 8)
reviewer_2.rate_hw(student_2, 'Git', 1)
reviewer_2.rate_hw(student_2, 'Git', 7)
reviewer_2.rate_hw(student_2, 'Python', 8)
reviewer_2.rate_hw(student_2, 'Python', 10)
reviewer_2.rate_hw(student_2, 'Python', 5)
reviewer_2.rate_hw(student_2, 'Java', 7)
reviewer_2.rate_hw(student_2, 'Java', 4)
reviewer_2.rate_hw(student_2, 'Java', 10)

student_1.rate_lecturer(lecturer_1, 'Git', 10)
student_1.rate_lecturer(lecturer_1, 'Git', 5)
student_1.rate_lecturer(lecturer_1, 'Git', 9)
student_1.rate_lecturer(lecturer_1, 'Java', 6)
student_1.rate_lecturer(lecturer_1, 'Java', 7)
student_1.rate_lecturer(lecturer_1, 'Java', 8)

student_2.rate_lecturer(lecturer_1, 'Java', 10)
student_2.rate_lecturer(lecturer_1, 'Java', 9)
student_2.rate_lecturer(lecturer_1, 'Java', 10)
student_2.rate_lecturer(lecturer_2, 'Python', 10)
student_2.rate_lecturer(lecturer_2, 'Python', 2)
student_2.rate_lecturer(lecturer_2, 'Python', 8)

print(student_1)
print(student_2)

print(reviewer_1)
print(reviewer_2)

print(lecturer_1)
print(lecturer_2)

print(f'Средняя оценка студентов по курсу "Git": {grades_students(students_list, "Git")}')
print(f'Средняя оценка студентов по курсу "Java": {grades_students(students_list, "Java")}')
print(f'Средняя оценка студентов по курсу "Python": {grades_students(students_list, "Python")}')

print(f'Средняя оценка лекторов по курсу "Git": {grades_lecturers(lecturer_list, "Git")}')
print(f'Средняя оценка лекторов по курсу "Java": {grades_lecturers(lecturer_list, "Java")}')
print(f'Средняя оценка лекторов по курсу "Python": {grades_lecturers(lecturer_list, "Python")}')