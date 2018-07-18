class Hexagon():
    def __init__(self, line):
        self.line = line

    def calculate_perimeter(self):
        return self.line * 6

hexa = Hexagon(2)
print(hexa.calculate_perimeter())
