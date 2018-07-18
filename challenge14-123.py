class Square:
    square_list = []

    def __init__(self, l):
        self.len = l
        self.square_list.append(self.len)

    def __repr__(self):
        return "{} by {} by {} by {}".format(self.len, self.len, self.len, self.len)


class TwoParameter:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        print(self.x is self.y)


square1 = Square(10)
square2 = Square(20)
square3 = Square(30)
print(Square.square_list)

print(square1)
print(square2)
print(square3)

two_param = TwoParameter(10, 10)
