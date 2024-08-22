from abc import ABC, abstractmethod


class GraphicShape(ABC):
    def __init__(self):
        super().__init__()

    @abstractmethod
    def calcArea(self):
        pass


class JSONify(ABC):
    @abstractmethod
    def toJSON(self):
        pass


class Circle(GraphicShape, JSONify):
    def __init__(self, radius):
        self.radius = radius

    def calcArea(self):
        return 3.14 * self.radius * self.radius

    def toJSON(self):
        return f"{{'Circle': {str(self.calcArea())}}}"


class Square(GraphicShape):
    def __init__(self, side):
        self.side = side

    def calcArea(self):
        return self.side * self.side


# g = GraphicShape()

c = Circle(5)
print(c.calcArea())
print(c.toJSON())
s = Square(3)
print(s.calcArea())
