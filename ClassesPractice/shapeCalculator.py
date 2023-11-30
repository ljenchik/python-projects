import math
class Shape:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f"This shape is {self.name}"

    def area(self):
        pass

class Rectangle(Shape):
    def __init__(self, name, width, height):
        super().__init__(name)
        self.width = width
        self.height = height

    def area(self):
        return f"Area of the {self.name} with width {self.width} and height {self.height} " \
               f"is {self.width * self.height}"

class Square(Shape):
    def __init__(self, name, side):
        super().__init__(name)
        self.side = side

    def area(self):
        return f"Area of the {self.name} with side {self.side} is {self.width * self.height}"

class Circle(Shape):
    def __init__(self, name, radius):
        super().__init__(name)
        self.radius = radius

    def area(self):
        return f"Area of the {self.name} with radius {self.radius} is {math.pi * self.radius ** 2}"


class Triangular(Shape):
    def __init__(self, name, side, height):
        super().__init__(name)
        self.side = side
        self.height = height

    def area(self):
        return f"Area of the {self.name} with side {self.side} and height {self.height} is {self.side * self.height / 2}"


shape = Shape("trapesium")
print(shape)
print(shape.area())

rectangle = Rectangle("rectangle", 12, 3)
print(rectangle)
print(rectangle.area())

circle = Circle("circle", 12)
print(circle)
print(circle.area())
