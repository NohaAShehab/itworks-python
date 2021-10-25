class Shape:

    def __init__(self, width=0, height=0):
        self.width = width  # I need to modify the input user entered
        # self.height = height
        self.height = height

    # class has property with name width
    # apply conditions on the input

    @property  # width is defined as property
    def width(self):
        return self.__width  # helper variable

    @width.setter  # python decorator ---> object from decorator class
    def width(self, v):
        if v < 0:
            v = abs(v)
        self.__width = v

    @property
    def height(self):
        return self.__abc

    @height.setter
    def height(self, height):
        if height < 0:
            height = abs(height)
        self.__abc = height


s = Shape(-40, -50)
print("hiii")

s.width = -1000
s.height = 9000

print(s)
