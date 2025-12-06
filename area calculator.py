
class Shape:
    def __init__(self, name):
        self.name = name

    def area(self):
        pass

    def perimeter(self):
        pass

    def display(self):
        print(f"Shape: {self.name}")
        print(f"Area: {self.area()}")
        print(f"Perimeter: {self.perimeter()}")
        print("-" * 20)



class Rectangle(Shape):
    def __init__(self, width, height):
        super().__init__("Rectangle")
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)



class Square(Rectangle):
    def __init__(self, side):
        super().__init__(side, side)
        self.name = "Square"  



r = Rectangle(4, 6)
r.display()

s = Square(5)
s.display()
