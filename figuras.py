class Square:
    def __init__(self, side:float = 0.0):
        self.side = side

    def area(self):
        return self.side * self.side

x = Square(5)
print(x.area())