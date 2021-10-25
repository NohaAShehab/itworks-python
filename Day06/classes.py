class Employee:
    # class variables
    mood = "Happy"

    def __init__(self, name, age, sal, commission):
        # instance variables
        self.name = name
        self.age = age
        self._sal = sal  # protected
        self.__commission = commission  # private

    def getSal(self):
        return self._sal

    def getCommission(self):
        return self.__commission

    # instance method  ---> related to the call instance
    def speak(self):
        print(f"I am {self.name}, I {self.age} years old ")
        return self  # object

    # classmethod ---> related to the class than object
    # No need to create instance to use this method
    # cls ---> refer to the caller class
    # class method ---> shared with all instance from class
    @classmethod  # decorator
    # applied on all the instances of the class
    # even the caller of the method via instance or class
    def setMood(cls, mood):
        Employee.mood = mood

    # class factory
    # factory method , method return class object
    # like constructor --> overloading
    @classmethod
    def empFactory(cls, name):
        # call the constructor of the current class
        # instance creator
        return cls(name, None, None, None)

    @staticmethod
    def calSal(sal, commission):
        return sal + (sal * commission)

    # static method  --> bounded to the class rather than the object
    # not need to create instance object --> to call it , not depened the object state
    # doesn't know anything about class structure or object
    # when to use
    # 1- group utility functions for the class
    # 2- creating new utility function for the class
    # static method takes date replace space with "/" with -
    # 25/10/2021, 25-10-2021
    @staticmethod
    def dashDate(date):
        return date.replace("/", "-")

    # adding and setting new instance variable
    def setbirthdate(self, bdate):
        self.bdate = bdate
