import unittest
import math
from points import Point

class Circle:
    """Klasa reprezentująca okręgi na płaszczyźnie."""

    def __init__(self, x, y, radius):
        if radius < 0:
            raise ValueError("promień ujemny")
        self.pt = Point(x, y)
        self.radius = radius

    def __repr__(self):       # "Circle(x, y, radius)"
        return "Circle({0},{1},{2})".format(self.pt.x,self.pt.y,self.radius)
    def __eq__(self, other):
        return self.pt == other.pt and self.radius == other.radius

    def __ne__(self, other):
        return not self == other

    def area(self):            # pole powierzchni
        if self.radius < 0:
            raise ValueError("promień ujemny")
        return math.pi * self.radius**2
    def move(self, x, y):     # przesuniecie o (x, y)
        if self.radius < 0:
            raise ValueError("promień ujemny")
        return(Circle(self.pt.x+x,self.pt.y+y,self.radius))
    def cover(self, other):    # najmniejszy okrąg pokrywający oba
        range = math.sqrt((self.pt.x-other.pt.x)**2 + (self.pt.y-other.pt.y)**2)
        if(self.radius > other.radius):
            odleglosc = range + self.radius
            punkt = Point(other.pt.x,other.pt.y)
        else:
            odleglosc = range + other.radius
            punkt = Point(self.pt.x,self.pt.y)
        return Circle(punkt.x,punkt.y,odleglosc)
# Kod testujący moduł.

class TestCircle(unittest.TestCase):

    def setUp(self):
        self.A = Circle(2,2,4)
        self.B = Circle(6,5,5)
    def test_print(self):
        self.assertEqual(Circle.__repr__(self.A), 'Circle(2,2,4)')
    def test_cmp(self):
        self.assertFalse(Circle.__eq__(self.A,self.B))
        self.assertTrue(Circle.__ne__(self.A,self.B))
    def test_area(self):
        self.assertEqual(Circle.area(self.A), 16*math.pi)
    def test_move(self):
        self.assertEqual(Circle.move(self.A,2,2), Circle(4,4,4))
    def test_cover(self):
        self.assertEqual(Circle.cover(self.A,self.B), Circle(2,2,10))

    def tearDown(self): pass
if __name__ == '__main__':
    unittest.main()     # wszystkie testy
