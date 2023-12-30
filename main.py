class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_hw(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def average_homework(self):
        rating_all = []
        for i in self.grades.values():
            for x in i:
                rating_all.append(x)
        return sum(rating_all) / len(rating_all)
    def __lt__(self, other):
        if self.average_homework() < other.average_homework():
            return f'Средняя оценка {self.name} ниже чем у {other.name}'
        else:
            return f'Средняя оценка {other.name} ниже чем у {self.name}'
    def __eq__(self, other):
        if self.average_homework() == other.average_homework():
            return f'Средние оценки студентов {self.name} и {other.name} ровны'
        else:
            return f'Средние оценки студентов {self.name} и {other.name} не ровны'

    def __str__(self):
        return f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за домашние задания: {self.average_homework():.2f}\nКурсы в процессе изучения: {', '.join(self.courses_in_progress)}\nЗавершенные курсы: {', '.join(self.finished_courses)}'
class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []
        self.name = name
        self.surname = surname
        self.courses_attached = []
class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.courses_attached = []
        self.grades = {}
    def average_rating(self):
        rating_all = []
        for i in self.grades.values():
            for x in i:
                rating_all.append(x)
        return sum(rating_all)/len(rating_all)
    def __lt__(self, other):
        if self.average_rating() < other.average_rating():
            return f'Средняя оценка у лектора {self.name} ниже чем у лектора {other.name}'
        else:
            return f'Средняя оценка у лектора {other.name} ниже чем у лектора  {self.name}'
    def __eq__(self, other):
        if self.average_rating() == other.average_rating():
            return f'Оценки {self.name} и {other.name} ровны'
        else:
            return f'{self.name} и {other.name} не ровны'
    def __str__(self):
        return f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {self.average_rating():.2f}'

class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.courses_attached = []
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'
    def __str__(self):
        return f'Имя: {self.name} \nФамилия: {self.surname}'

student_1 = Student('Александр','Пупкин', 'М')
student_1.courses_in_progress += ['Python']
student_1.courses_in_progress += ['GIT']
student_1.finished_courses += ['Введение в программирование']
student_2 = Student('Валерий','Фиксиков','М')
student_2.courses_in_progress += ['Python']
student_2.courses_in_progress += ['GIT']
student_2.finished_courses += ['Введение в программирование']
mentor_1 = Mentor('Сергей','Петров')
mentor_2 = Mentor('Олег','Зелебобин')
lecturer_1 = Lecturer('Юрий','Ким')
lecturer_2 = Lecturer('Сергей','Бобиков')
lecturer_1.courses_attached += ['Python']
lecturer_1.courses_attached += ['GIT']
lecturer_2.courses_attached += ['Python']
lecturer_2.courses_attached += ['GIT']
student_1.rate_hw(lecturer=lecturer_1,course='Python',grade=8)
student_1.rate_hw(lecturer=lecturer_1,course='GIT',grade=3)
student_1.rate_hw(lecturer=lecturer_1,course='Python',grade=8)
student_2.rate_hw(lecturer=lecturer_2,course='Python',grade=3)
student_2.rate_hw(lecturer=lecturer_2,course='GIT',grade=5)
student_2.rate_hw(lecturer=lecturer_2,course='Python',grade=8)
reviewer_1 = Reviewer('Игнат','Жульберов')
reviewer_2 = Reviewer('Валерий','Бурунов')
reviewer_1.courses_attached +=['Python']
reviewer_1.courses_attached +=['GIT']
reviewer_2.courses_attached +=['Python']
reviewer_2.courses_attached +=['GIT']
reviewer_1.rate_hw(student=student_1,course='Python',grade=7)
reviewer_1.rate_hw(student=student_1,course='Python',grade=5)
reviewer_1.rate_hw(student=student_1,course='GIT',grade=7)
reviewer_2.rate_hw(student=student_2,course='Python',grade=6)
reviewer_2.rate_hw(student=student_2,course='Python',grade=8)
reviewer_2.rate_hw(student=student_2,course='GIT',grade=9)
print(student_1)
print()
print(lecturer_2)
print()
print(reviewer_1)
print()
print(lecturer_1>lecturer_2)
print()
print(student_1==student_2)
print()
print(student_1>student_2)
student_list = []
student_list.append(student_1)
student_list.append(student_2)
def average_course_rating(students_list,course):
    data = []
    for i in students_list:
        for x in i.grades[course]:
            data.append(x)
    return print(f'Средний балл студентов по курсу {course} {sum(data)/len(data):.2f}')
average_course_rating(students_list=student_list,course='Python')

lecturer_list = []
lecturer_list.append(lecturer_1)
lecturer_list.append(lecturer_2)
def average_lecturer_rating(lecturers_list,course):
    data = []
    for i in lecturers_list:
        for x in i.grades[course]:
            data.append(x)
    return print(f'Средний балл лекторов по курсу {course} {sum(data)/len(data):.2f}')
average_lecturer_rating(lecturers_list=lecturer_list,course='GIT')