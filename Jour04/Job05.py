from Job04 import Forme
from Job04 import Rectangle
import math
class Cercle(Forme):
    def __init__(self, radius) -> None:
        self.__radius = radius
    
    def getRadius(self):
        return self.__radius
    def setRadius(self, val):
        self.__radius = val
    
    def aire(self):
        return print("Aire du cercle: ",math.pi * (self.__radius ** 2))
    
n = Rectangle(20, 45)
y = Cercle(5)
n.aire()
y.aire()
