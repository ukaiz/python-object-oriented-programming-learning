# Python Object Oriented Programming by Joe Marini course example
# Using Abstract Base Classes to implement interfaces

from abc import ABC, abstractmethod


class GraphicShape(ABC):
    def __init__(self):
        super().__init__()

    @abstractmethod
    def calcArea(self):
        pass

class interface(ABC):
    @abstractmethod
    def toJSON():
        pass


class Circle(GraphicShape, interface):
    def __init__(self, radius):
        self.radius = radius

    def calcArea(self):
        return 3.14 * (self.radius ** 2)
    def toJSON():
        pass
c = Circle(10)
print(c.calcArea())
