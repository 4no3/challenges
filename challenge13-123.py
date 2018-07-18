class Shape:    # 親クラスは子よりも先に定義する必要がある
    def __init__(self):
        pass

    def what_am_i(self):
        return "I am a shape"


class Rectangle(Shape):
    def __init__(self, w, l):
        self.width = w
        self.len = l

    def calculate_perimeter(self):
        return self.width * 2 + self.len * 2


class Square(Shape):
    def __init__(self, l):
        self.len = l

    def calculate_perimeter(self):
        return self.len * 4

    def change_size(self, x):
        self.len += x


Rectangle = Rectangle(10, 20)
print(Rectangle.calculate_perimeter())
print(Rectangle.what_am_i())

Square = Square(100)
print(Square.calculate_perimeter())
Square.change_size(-8)
print(Square.len)
print(Square.what_am_i())
