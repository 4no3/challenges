#コンポジション
class Dog:
    def __init__(self, name, bread, owner):
        self.name = name
        self.bread = bread
        self.owner = owner

class Person:
    def __init__(self, name):
        self.name = name

mick = Person("Mick Jagger")
stan = Dog("Stanley", "Bulldog", mick)
print(stan.owner.name)


'''
#継承
class Shape:
    def __init__(self, w, l):
        self.width = w
        self.len = l

    def print_size(self):
        print("{} by {}".format(self.width, self.len))

class Square(Shape):
    def area(self):
        return self.width * self.len

    def print_size(self):
        print("I am {} by {}".format(self.width, self.len))

my_shape = Shape(20, 30)
my_shape.print_size()

a_square = Square(20, 20)
a_square.print_size()
print(a_square.area())
'''

'''
# カプセル化
class Rectangle:
    def __init__(self, w, l):
        self.width = w
        self.len = l

    def area(self):
        return self.width * self.len

class Data:
    def __init__(self):
        self.nums = [1,2,3,4,5]

    def change_data(self, index, n):
        self.nums[index] = n

class PublicPrivateExample:
    def __init__(self):
        self.public = "safe"
        self._unsafe = "unsafe"

    def public_method(self):
        pass

    def _unsafe_method(self):
        pass
'''

