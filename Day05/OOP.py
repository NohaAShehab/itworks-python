#struct

# emp1 = {
#     "name":"Ahmed",
#     "age" : 28,
#     "gender": "male",
#     "mail": "Ahmed@itworks.com"
# }
#
# emp2 = {
#     "name":"Mohamed",
#     "age" : 22,
#     "gender": "male",
#     "mail": "mohamed@itworks.com"
# }
#
#
# emp3 = {
#     "name":"Mohamed",
#     "age" : 22,
#     "gender": "male",
#     "mail": "mohamed@itworks.com"
# }

class Employee:
    #blueprint 0=--> create varibale number of object -- with same basic structure
    # empty class
    # define instance variable , define it inside constructor ,
    #this function is called during creation of the object
    def __init__(self, ename):
        # print(f"self: {self}")  # self refere to this instance of this class
        # this
        # print("Object or intance created")
        self.name = ename



# take isntance from the class
# m = Employee
# print(m)
e = Employee("Zenia ")# reference from employee
print(f"instance {e}")
print(e.name)
e.name = "Zeina Ahmed"

e2 = Employee("Rana")
print("test")
# e = new Employee(), new instance from Employee class
# inside each constructor --> function --> is called during creating object
# by default ---> classes cannot have constructor
