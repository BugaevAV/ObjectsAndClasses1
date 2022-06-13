class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def lect_grades(self, lecturer, course, grade ):
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached and course in\
                self.courses_in_progress or self.finished_courses:
            if course in lecturer.st_grades:
                lecturer.st_grades[course] += [grade]
            else:
                lecturer.st_grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        res = f'Имя: {self.name}\nФамилия: {self.surname}\n'
        for key in self.grades:
            res += f'Cредняя оценка д/з по курсу {key}: {Lecturer.aver_rating(self, self.grades, key)} балла(-ов)\n'
        if self.courses_in_progress:
              res += f'Курсы в процессе изучения: {", ".join(self.courses_in_progress)}\n'
        else:
            res += f'На данный момент у {self.name} {self.surname} нет изучаемых курсов'
        if self.finished_courses:
            res += f'У {self.name} {self.surname} завершены курсы: {", ".join(self.finished_courses)}'
        else:
            res += f'У {self.name} {self.surname} нет завершенных курсов'
        return res

    def __lt__(self, other):
        res = ''
        for course in self.grades:
            if isinstance(other, Student) and course in other.grades:
                if Lecturer.aver_rating(self, self.grades, course) < Lecturer.aver_rating(other, other.grades, course):
                    res += f'лекции по курсу {course} студент {other.name} {other.surname} выполнил лучше,\nчем ' \
                           f'студент {self.name} {self.surname}\n'
                elif Lecturer.aver_rating(self, self.grades, course) > Lecturer.aver_rating(other, other.grades, course):
                    res += f'лекции по курсу {course} студент {self.name} {self.surname} выполнил лучше,\nчем ' \
                           f'студент {other.name} {other.surname}\n'
                else:
                    res += f'лекции по курсу {course} студент {other.name} {other.surname} и' \
                           f' студент {self.name} {self.surname}\nвыполнили с одинаковой средней оценкой\n'
        return res

class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.st_grades = {}

    def __str__(self):
        res = f'Имя: {self.name}\nФамилия: {self.surname}\n'
        for key in self.st_grades:
            res += f'Cредняя оценка лектора по курсу {key}: {self.aver_rating(self.st_grades, key)} балла(-ов)\n'
        return res

    def aver_rating(self, points_dict, course):
        summa = sum(points_dict[course])
        length = len(points_dict[course])
        res = round((summa/length),1)
        return res

    def __lt__(self, other):
        res = ''
        for course in self.st_grades:
            if isinstance(other, Lecturer) and course in other.st_grades:
                if self.aver_rating(self.st_grades,course) < other.aver_rating(other.st_grades, course):
                    res += f'лекции по курсу {course} от {other.name} {other.surname} нравится студентам' \
                           f' больше,\nчем от {self.name} {self.surname}\n'
                elif self.aver_rating(self.st_grades,course) > other.aver_rating(other.st_grades, course):
                    res += f'лекции по курсу {course} от {self.name} {self.surname} нравится студентам' \
                           f' больше,\nчем от {other.name} {other.surname}\n'
                else:
                    res += f'лекции по курсу {course} от {other.name} {other.surname} и от {self.name} ' \
                           f'{self.surname}\nстуденты оценили одинаково\n'
        return res


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
        res = f'Имя: {self.name}\nФамилия: {self.surname}'
        return res


def average_students(students, course):
    summa = 0
    for student in students:
        summa += Lecturer.aver_rating(student, student.grades, course)
    length = len(students)
    res = f'Средняя оценка выполнения д/з по курсу {course}: {round(summa/length, 1)} балла(-ов)'
    return res

def average_lecturers(lecturers, course):
    summa = 0
    for lecturer in lecturers:
        summa += Lecturer.aver_rating(lecturer, lecturer.st_grades, course)
    length = len(lecturers)
    res = f'Средняя оценка лекций по курсу {course}: {round(summa/length, 1)} балла(-ов)'
    return res


best_student = Student('Ruoy', 'Eman', 'your_gender')
best_student.courses_in_progress += ['Python']
best_student.courses_in_progress += ['Git']
best_student.finished_courses += ['JS']

tipical_student = Student('Petya', 'Motociklov', 'ufo')
tipical_student.courses_in_progress += ['Python']
tipical_student.courses_in_progress += ['Git']

reviewer1 = Reviewer('Some', 'Buddy')
reviewer1.courses_attached += ['Python']
reviewer1.courses_attached += ['Git']

reviewer2 = Reviewer('Genady', 'Yavseviju')
reviewer2.courses_attached += ['Git']
reviewer2.courses_attached += ['Python']

lecturer1 = Lecturer('Fantazer', 'Timenyanazivala')
lecturer1.courses_attached += ['Git']
lecturer1.courses_attached += ['Python']

lecturer2 = Lecturer('Victor', 'Listentomenow')
lecturer2.courses_attached += ['Python']
lecturer2.courses_attached += ['Git']

best_student.lect_grades(lecturer1, 'Python', 10)
best_student.lect_grades(lecturer1, 'Python', 10)
best_student.lect_grades(lecturer2, 'Python', 8)
best_student.lect_grades(lecturer2, 'Python', 8)
best_student.lect_grades(lecturer1, 'Git', 9)
best_student.lect_grades(lecturer1, 'Git', 9)
best_student.lect_grades(lecturer2, 'Git', 9)
best_student.lect_grades(lecturer2, 'Git', 9)

tipical_student.lect_grades(lecturer1, 'Python', 10)
tipical_student.lect_grades(lecturer1, 'Python', 10)
tipical_student.lect_grades(lecturer2, 'Python', 8)
tipical_student.lect_grades(lecturer2, 'Python', 8)
tipical_student.lect_grades(lecturer1, 'Git', 7)
tipical_student.lect_grades(lecturer1, 'Git', 7)
tipical_student.lect_grades(lecturer2, 'Git', 7)
tipical_student.lect_grades(lecturer2, 'Git', 7)

reviewer1.rate_hw(best_student, 'Python', 9)
reviewer1.rate_hw(best_student, 'Git', 9)
reviewer1.rate_hw(best_student, 'Python', 9)
reviewer1.rate_hw(best_student, 'Git', 9)
reviewer1.rate_hw(tipical_student, 'Python', 8)
reviewer1.rate_hw(tipical_student, 'Git', 8)
reviewer1.rate_hw(tipical_student, 'Python', 9)
reviewer1.rate_hw(tipical_student, 'Git', 8)

reviewer2.rate_hw(best_student, 'Python',10)
reviewer2.rate_hw(best_student, 'Git',8)
reviewer2.rate_hw(best_student, 'Python',10)
reviewer2.rate_hw(best_student, 'Git',8)
reviewer2.rate_hw(tipical_student, 'Python',10)
reviewer2.rate_hw(tipical_student, 'Git',10)
reviewer2.rate_hw(tipical_student, 'Python',10)
reviewer2.rate_hw(tipical_student, 'Git',9)



print(best_student.grades)
print(best_student)
print()

print(tipical_student.grades)
print(tipical_student)
print()

print(lecturer1.st_grades)
print(lecturer1)

print(lecturer2.st_grades)
print(lecturer2)

print(reviewer1)
print()
print(reviewer2)
print()

print(lecturer2 < lecturer1)
print(best_student > tipical_student)

st = [best_student, tipical_student]
print(average_students(st, 'Python'))
lec = [lecturer1, lecturer2]
print(average_lecturers(lec, 'Git'))
print()