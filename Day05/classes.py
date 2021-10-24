class Employees:
    # protected
    # _age = "10" # pyhon
    # private
    # class variable, class property
    # any property ---> needed to be added to describe a common
    # property for all instance from this class
    __mood = "Happy"

    # constructor, cannot construct muliple constructors
    def __init__(self, name: str, sal: int = 8, age=None,
                 address="Cairo"):
        # instance variable ---> all instance variables are public
        self.name = name  # public member
        self.__salary = sal  # private
        self._age = age  # protected
        self.address = address

    # instance method --> related to caller instance
    def sayhello(self, test=None):
        print("hiii")
        print(f"hello {self.name}, your salary = {self.__salary} , {test}")
