 
import math
import unittest
class Point:
    """Klasa reprezentująca punkty na płaszczyźnie."""

    def __init__(self, x, y):  # konstuktor
        self.x = x
        self.y = y

    def __str__(self):        # zwraca string "(x, y)"
        x = self.x
        y = self.y
        return "({0},{1})".format(x,y)

    def __repr__(self):       # zwraca string "Point(x, y)"
        return "Point({0},{1})".format(self.x,self.y)
    
    def __eq__(self, other):  # obsługa point1 == point2
        return (self.x==other.x and self.y==other.y)

    def __ne__(self, other):        # obsługa point1 != point2
        return not self == other

    # Punkty jako wektory 2D.
    def __add__(self, other):   # v1 + v2
        x = self.x + other.x
        y = self.y + other.y
        v3 = Point(x,y)
        return v3
    def __sub__(self, other):   # v1 - v2
        x = self.x - other.x
        y = self.y - other.y
        v3 = Point(x,y)
        return v3

    def __mul__(self, other):   # v1 * v2, iloczyn skalarny
        return (self.x*other.x)+(self.y*other.y)
    def cross(self, other):         # v1 x v2, iloczyn wektorowy 2D
        return self.x * other.y - self.y * other.x

    def length(self):           # długość wektora
        return math.sqrt(pow(self.x,2) + pow(self.y,2))
        
        
