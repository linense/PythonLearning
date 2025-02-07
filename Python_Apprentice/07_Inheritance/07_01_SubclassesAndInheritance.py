import math

class Shape:
    def __init__(self, shape_type, color='Red'):
        self.__type = shape_type
        self.__color = color

    def get_type(self):
        print("Type: ", self.__type)
        return self.__type
    
    def get_color(self):
        print("Color: ", self.__color)
        return self.__color

    def get_area(self):
        pass

    def get_perimeter(self):
        pass

class Circle(Shape):    # Circle inherits from Shape
    def __init__(self, radius):
        Shape.__init__(self, 'circle')
        self.__radius = radius
    
    def get_area(self):
        print("Area: ", math.pi * self.__radius * self.__radius)
        return math.pi * self.__radius * self.__radius

    def get_perimeter(self):
        print("Perimeter:" , 2 * math.pi * self.__radius)
        return 2 * math.pi * self.__radius

class Square(Shape):    # Square inherits from Shape
    def __init__(self, color='White'):
        Shape.__init__(self, 'square', color)

square = Square()
square.get_type()
square.get_color()

circle = Circle(10)
circle.get_type()
circle.get_area()
circle.get_perimeter()
