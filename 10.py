import abc
class Shape(object):
    __metaclass__ = abc.ABCMeta
    @abc.abstractmethod
    def calc_perimeter(self, input):
        """Method documentation"""
        return

class Triangle(Shape):
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
    def calc_perimeter(self):
        perim = self.a + self.b + self.c
        print("Consider me implemented", perim)
        return perim

class Rectangle(Shape):
    def __init__(self, a, b):
        self.a = a
        self.b = b
    def calc_perimeter(self):
        perim = self.a + self.b
        print("Consider me implemented", perim)
        return perim

class Square(Rectangle):

    def __init__(self, a, b=None):
        super().__init__(a, b=None)
        self.a = a
        if b is None:
            return a

my_rectangle = Rectangle(10,5)
my_rectangle.calc_perimeter()

my_square = Square(10)
#my_square.a = Square(10)

my_square.calc_perimeter()