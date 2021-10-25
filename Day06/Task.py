class Students:
    count = 0
    studentlist = []

    def __init__(self, name, id):
        self.name = name
        self.id = id
        Students.countSTd(self)

    @classmethod
    def countSTd(cls, obj):
        cls.count += 1
        cls.studentlist.append(obj)


class ITI:

    # def __init__(self, *students):  # variable len of students 0 or more
    #     self.students = list(students)
    def __init__(self):
        # self.student = studentlist
        self.student = Students  # get all intances form this class as list


s = Students("Ahmed", 10)
s2 = Students("Rana", 4)

iti= ITI()
eng = ITI()


