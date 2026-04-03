class Shape:
    def __init__(self, area):
        self.area = area

class Rectangle(Shape):
    def __init__(self, length, width, area):
        self.length = length
        self.width = width
        area = length * width
    def show_area(area):
        print(area + "square units")

class Circle(Shape):
    def __init__(self, radius, area):
        self.radius = radius
        area = 3.14 * radius * radius
    def show_area(area):
        print(area + "square units")

r = Rectangle("10", "5")
r.show_area()

c = Circle("7")
c.show_area()
