

mm  = ["google","gmail", "facebook"]


class Car:
    pass

class Emp:
    def __init__(self, car:Car):
        if isinstance(car, Car):
            self.car = car
