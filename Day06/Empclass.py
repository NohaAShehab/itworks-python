from inheritance import Person, Test, B


# multiple inherince
class Emp(Person, Test):
    #
    def __init__(self, name, age, address, salary, test="Hi"):
        # super().__init__(name)  # name, age=None, address =None, sal=
        Person.__init__(self,name)
        Test.__init__(self)
        B.__init__(self)
        print("Creating new Employee object")
        self.salary = salary
        # access protected members from the child class
        self._age = age
        self._test = test
        # private
        self.__address = address

    # overriding
    def speak(self):
        super().speak()
        return f"{self.name}, .....{self._test}"

    # class method
    @classmethod
    def sleep(cls):
        super().sleep()
        print("yeeeeeeeeeeeeeees")

    @staticmethod
    def dashDate(date):
        print(super().dashDate(date))
        return "Welcome"
