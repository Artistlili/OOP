import math

class shape:
    def __init__ (self):
        self.__area = 0
    
    def area(self):
        print (f"Area: {self.__area}")

class circle(shape):
    def __init__ (self, radius):
        super().__init__()
        self.__radius = radius
    
    def area(self):
        self.__area = math.pi * (self.__radius ** 2)
        print (f"Area: {self.__area}")

class rectangle(shape):
    def __init__ (self, length, width):
        super().__init__()
        self.__length = length
        self.__width = width
    
    def area(self):
        self.__area = self.__length * self.__width
        print (f"Area: {self.__area}")

class square(shape):
    def __init__ (self, side):
        super().__init__()
        self.__side = side
    
    def area(self):
        self.__area = self.__side ** 2
        print (f"Area: {self.__area}")

c = circle(2)
c.area()
r = rectangle(3,4)
r.area()
s = square(5)
s.area()