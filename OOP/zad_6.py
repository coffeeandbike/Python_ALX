'''
Zaimplementuj klasę Vector dostarczającą funkcjonalność wektora swobodnego na dwuwymiarowej płaszczyźnie.
Wektory powinny mieć możliwość dodawania, odejmowania, mnożenia (przez liczbę), porównywania (po długości)
oraz powinny posiadać czytelną reprezentację napisową.
Przykład użycia:
vector_1 = Vector(x=1, y=2)
vector_2 = Vector(x=1, y=2)
vector_3 = vector_1 + vector_2
'''

import math

class Vector:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def __str__(self) -> str: #Vector [x=3, y = 5]
        return f'Vector [x={self.x}, y={self.y}]'

    # dodawanie dwoch wektorow x2+x2, y1+y2
    def __add__(self, other):
        if not isinstance(other, Vector):
            raise TypeError ("Second vector has to be a vector")
        return Vector(self.x + other.x, self.y + other.y)

    #odejmowanie x1-x2, y1-y2
    def __sub__(self, other):

        if not isinstance(other, Vector):
            raise TypeError ("Second vector has to be a vector")

        return Vector(self.x - other.x, self.y - other.y)



    # v3 = x1*other, y2*other
    def __mul__(self, other): # mnozenie przez liczbe other moze byc int lub float
        if not isinstance(self, Vector):
            raise TypeError ("Vector has is not a vector")

        return Vector(self.x * other, self.y * other)

    # liczenie dlugosci wektora

    def len(self):

        return math.sqrt(self.x ** 2 + self.y ** 2)

        # porownywanie
    def __eq__(self, other):
        if not isinstance(other, Vector):
            raise TypeError ("Vector has is not a vector")

        return self.len == other.len

    def __ne__(self, other):
        return self.len() != other.len()

    # czy dluzszy
    def __gt__(self, other):
        return self.len() > other.len()

    #
    def __ge__(self, other):
        return self.len() >= other.len()

    # czy krotszy <
    def __lt__(self, other):
        return self.len() < other.len()

    # <=
    def __le__(self, other):
        return self.len() <= other.len()



def test_wypisywania():
    v = Vector(x=3, y=2)
    assert str(v) == 'Vector [x=3, y=2]'

def test_dodawania():
    v1 = Vector(x=1, y=3)
    v2 = Vector(x=3, y=2)
    v3 = v1 + v2
    assert v3.x == 4 and v3.y == 5

def test_dejmowania():
    v1 = Vector(x=1, y=3)
    v2 = Vector(x=3, y=2)
    v3 = v1 - v2
    assert v3.x == -2 and v3.y == 1

def test_mnozenia():
    v1 = Vector(x=1, y=3)
    v3 = v1 * 2
    assert v3.x == 2 and v3.y == 6

def test_porownania():
    v1 = Vector(x=1, y=3)
    v2 = Vector(x=3, y=2)
    assert v1 < v2



def test_dlugisci_wektora():
    v1 = Vector(x=3, y=4)
    assert v1.len() == 5
