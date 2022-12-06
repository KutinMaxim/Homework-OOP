class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_hw(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached and course in self.courses_in_progress:
            if course in lecturer.grades:
                    lecturer.grades[course] += [grade]
            else:
                    lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __rate_average(self):
        average = round(sum(sum(self.grades.values(), [])) / len(sum(self.grades.values(), [])), 1)
        return average

    def __str__(self):
        res = f'Имя: {self.name}\n'\
        f'Фамилия: {self.surname}\n'\
        f'Средняя оценка за домашние задания: {self.__rate_average()}\n'\
        f'Курсы в процессе изучения: {", ".join(self.courses_in_progress)}\n'\
        f'Завершенные курсы: {", ".join(self.finished_courses)}'
        return res

    def __lt__(self, other):
        if not isinstance(other, Student):
            print('Такое сравнение некорректно')
            return
        return self.__rate_average() < other.__rate_average()

class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def __rate_average(self):
        average = round(sum(sum(self.grades.values(), [])) / len(sum(self.grades.values(), [])), 1)
        return average

    def __str__(self):
        res = f'Имя: {self.name}\n'\
        f'Фамилия: {self.surname}\n'\
        f'Средняя оценка за лекции: {self.__rate_average()}'
        return res

    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            print('Такое сравнение некорректно')
            return
        return self.__rate_average() < other.__rate_average()

class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        res = f'Имя: {self.name}\n'\
        f'Фамилия: {self.surname}'
        return res

student_1 = Student('Максим', 'Кутьин', 'M')
student_1.courses_in_progress += ['Python']
student_1.courses_in_progress += ['Excel']
student_1.courses_in_progress += ['Java']
student_1.finished_courses += ['Git']

student_2 = Student('Алёна', 'Коротенко', 'Ж')
student_2.courses_in_progress += ['Python']
student_2.courses_in_progress += ['Excel']
student_2.courses_in_progress += ['Java']
student_2.finished_courses += ['Git']

reviewer_1 = Reviewer('Алексей', 'Никитин')
reviewer_1.courses_attached += ['Python']
reviewer_1.courses_attached += ['Java']
reviewer_1.courses_attached += ['Excel']

reviewer_2 = Reviewer('Андрей', 'Пермяков')
reviewer_2.courses_attached += ['Python']
reviewer_2.courses_attached += ['Java']
reviewer_2.courses_attached += ['Excel']

reviewer_1.rate_hw(student_1, 'Python', 9)
reviewer_1.rate_hw(student_1, 'Java', 6)
reviewer_1.rate_hw(student_1, 'Excel', 7)

reviewer_2.rate_hw(student_2, 'Python', 10)
reviewer_2.rate_hw(student_2, 'Java', 8)
reviewer_2.rate_hw(student_2, 'Excel', 5)

lecturer_1 = Lecturer('Сергей', 'Петрик')
lecturer_1.courses_attached += ['Python']
lecturer_1.courses_attached += ['Java']
lecturer_1.courses_attached += ['Excel']

lecturer_2 = Lecturer('Виктор', 'Павлов')
lecturer_2.courses_attached += ['Python']
lecturer_2.courses_attached += ['Java']
lecturer_2.courses_attached += ['Excel']

student_1.rate_hw(lecturer_1, 'Python', 10)
student_1.rate_hw(lecturer_1, 'Java', 8)
student_1.rate_hw(lecturer_1, 'Excel', 9)

student_2.rate_hw(lecturer_2, 'Python', 9)
student_2.rate_hw(lecturer_2, 'Java', 6)
student_2.rate_hw(lecturer_2, 'Excel', 10)

students_list = [student_1, student_2]
lecturers_list = [lecturer_1, lecturer_2]

def comparison_students(students_list, course):
    sum_grades = []
    for stud in students_list:
        if course in stud.grades.keys():
            sum_grades += stud.grades[course]
        else:
            return 'Курсы не совпадают'
    return round(sum(sum_grades) / len(sum_grades), 1)

def comparison_lecturers(lecturers_list, course):
    sum_grades = []
    for lect in lecturers_list:
        if course in lect.grades.keys():
            sum_grades += lect.grades[course]
        else:
            return 'Курсы не совпадают'
    return round(sum(sum_grades) / len(sum_grades), 1)

print(student_1)
print()
print(student_2)
print()
print(reviewer_1)
print()
print(reviewer_2)
print()
print(lecturer_1)
print()
print(lecturer_2)
print()
print(f'Результат сравнения студентов (по средним оценкам за ДЗ): '
      f'{student_1.name} {student_1.surname} < {student_2.name} {student_2.surname} = {student_1 > student_2}')
print()
print(f'Результат сравнения лекторов (по средним оценкам за лекции): '
      f'{lecturer_1.name} {lecturer_1.surname} < {lecturer_2.name} {lecturer_2.surname} = {lecturer_1 > lecturer_2}')
print()
print(f'Средняя оценка студентов за курс: {comparison_students(students_list, "Java")}')
print()
print(f'Средняя оценка лекторов за курс: {comparison_lecturers(lecturers_list, "Python")}')