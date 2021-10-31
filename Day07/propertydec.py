class Employee:

    def __init__(self, firstname, lastname, salary):
        self.firstname = firstname
        self.lastname = lastname
        self.salary = salary

    # setting an email
    # get information in special format from existing information
    @property  # define when create object
    def email(self):
        return f"{self.firstname[0].lower()}.{self.lastname.lower()}@itworks.com"

    @property
    def salary(self):
        return self.__salary

    @salary.setter
    def salary(self, sal):
        self.__salary = abs(sal)

    # delete the property
    @salary.deleter
    def salary(self):
        print("Delete salary")
        self.__salary = None

    # generate setter and getter for a new property

    @property
    def fullname(self):
        return f"{self.firstname} {self.lastname}"

    @fullname.setter
    def fullname(self, name):
        # if name:
        #     if name.isdigit:
        #         raise ValueError("plz you should enter valid name")
        name = name.strip()
        first, last = name.split(" ")
        self.firstname = first
        self.lastname = last

    @fullname.deleter
    def fullname(self):
        # self.fullname = None
        self.firstname = None
        self.lastname = None
        print("fullname deleted")

    # implement __str__ magic method ---> you call it when print object
    # make object printable, with users
    def __str__(self):
        return f"this is an Employee with name ={self.firstname} {self.lastname}"

    # developer, quick debugging
    def __repr__(self):
        return f"Employee({self.firstname},{self.lastname},{self.email},{self.salary})"

    # operator overlaoding
    def __add__(self, other):
        return f"{self.firstname} {other.firstname}"

    def __call__(self, *args, **kwargs): # call object with zero or more parmar,
        print(f"this object is constructed {args} {kwargs}")

    def __len__(self):
        # must retrun with number
        # count the properties within object
        return 5


print(len("noha"))
# print(str.__len__("itworks"))
# print("hiii")
e = Employee("Mohamed", "Elsayed", -1000)
print(len(e))
# e.salary = -9000
# print(e.fullname)
# del e.fullname
# print(e.fullname)
# print("hi")
# try:
#     e.fullname = "100000"  # must affect the object structure
# except Exception as e:
#     fname = input("plz enter valid name herrrrrrrr   ")
#     e.fullname = fname
# # print(e.salary)
# # # print(e.email)
# print("hello")

# #####
# del(e.salary)
# print("hii")
# print(e.salary)
### special methods
e = Employee("Mohamed", "Elsayed", -1000)
b = Employee("Test", "Emp", 3000)
print(e)
e("ahmed", "ali", name="iti", email="test")

# print(e)

# print("noha")  # string is an object
# print("noha".__str__())
# print(e.__str__())
# print(Employee.__str__(e))

# print(e.__repr__())
# print(Employee.__repr__(e))

# print(2+3)  #interpreter --->   int =2 + int = 3 ---> output
# print(int.__add__(3,4))
# print("Ahmed"+" Ali")
# print(str.__add__("Ahmed", "Ali"))
# print(e+b)
