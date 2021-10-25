class Person:
    # class variable
    isAlive = True

    def __init__(self, name, age=None, address=None):
        self.name = name
        self._age = age
        self.__address = address

    def speak(self):
        print(f"my name is {self.name}")

    @classmethod  # object from class --> classmethod
    def sleep(cls):
        print("Whoooa")

    @staticmethod
    def dashDate(date):
        return date.replace("/", "-")


class Test:
    def __init__(self, abc=""):
        print("Test constructor is called ")
        self.abc = abc

    def sayHello(self):
        print("hello from test ")


class B:
    y = "happy"

    def __init__(self, x=10):
        self.x = x



class A(B):
    pass

class C(A):
    pass