
class Shape:

    def __init__(self, name):
        self.name = name

    def info(self):
        print(f"This is a {self.name}")

    def area(self):
        pass

    def perimeter(self):
        pass


class Rectangle(Shape):

    def __init__(self, width, height):
        super().__init__("Rectangle")
        self._width = width
        self._height = height

    def area(self):
        return self._width * self._height

    def perimeter(self):
        return 2 * (self._width + self._height)



class Square(Shape):

    def __init__(self, side):
        super().__init__("Square")
        self.__side = side  

    def area(self):
        return self.__side * self.__side

    def perimeter(self):
        return 4 * self.__side



rect = Rectangle(4, 6)
sq = Square(5)


for shape in (rect, sq):
    shape.info()
    print("Area:", shape.area())
    print("Perimeter:", shape.perimeter())
    print()
