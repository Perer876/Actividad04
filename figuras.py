from math import pi

class Square:
    def __init__(self, side:float = 0.0):
        self.side = side

    def area(self):
        return self.side * self.side

class Triangle:
    def __init__(self, base:float = 0.0, altitude:float = 0.0):
        self.base = base
        self.altitude = altitude

    def area(self):
        return (self.base * self.altitude)/2

class Circle:
    def __init__(self, radio:float = 0.0):
        self.radio = radio

    def area(self):
        return self.radio * self.radio * pi

x = Circle(10)
print(x.area())
