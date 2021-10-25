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


s = Students("Ahmed", 10)
s = Students("Rana", 4)
print(Students.count)
print(Students.studentlist)

for item in Students.studentlist:
    # print(f"id={item.key} and value: {item.v}")
    # print(f"item {item.name}, id= {item.id}")
    if item.id == 10:
        print(f"{item.name}")


