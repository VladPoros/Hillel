class Student():

    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade

    def info (self):
        print('Студент',self.name,',',self.age, 'лет, ', self.grade, ' группа')


class Group():

    def __init__(self, *args):
        self.list = []
        for _ in args:
            self.list.append(_)

    def printInfo(self):
        for student in self.list:
            student.info()

first_data = Student('Влад', 25, 3)
second_data = Student('Саша', 24, 2)

general_data = Group(first_data, second_data)

general_data.printInfo()
