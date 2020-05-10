"""
Zaimplementuj klasę ElectricCar odwzorowującą zachowanie samochodu elektrycznego.
Klasa powinna umożliwiać pokonanie zadanego dystansu, który nie może przekroczyć maksymalnego zasięgu
zdefiniowanego dla samochodu. Samochód powinien mieć także możliwość naładowania baterii.
car = ElectricCar(100)
car.drive(70)
70
car.drive(50)
30
car.drive(50)
0
car.charge()
car.drive(50)
50
"""

'''
https://yuml.me/diagram/nofunky;scale:180/class/edit/%5BElectricCar%7Cmax_range:%20int;%20battery_level:%20int%7C__init__(max_range:%20int);%20charge();%20drive(distance:%20int):%20int%5D
'''

import pytest

class ElectricCar:
    def __init__(self, max_range: int):
        self.max_range = max_range
        self.battery_level = max_range

    def drive(self, distance: int) -> int:
        """
        if distance <= self.battery_level:
            self.battery_level -= distance
            return distance
        else:
            tmp = self.battery_level
            self.battery_level -= self.battery_level
            return tmp
        """
        real_distance = min(distance, self.battery_level)
        self.battery_level -= real_distance
        return real_distance


    def charge(self):
        self.battery_level = self.max_range


def test_zasieg():
    bmw = ElectricCar(100)
    assert bmw.drive(100) == 100

def test_poza_zasiegiem():
    bmw = ElectricCar(100)
    assert bmw.drive(150) == 100

def test_ladowanie():
    bmw = ElectricCar(100)
    assert bmw.drive(70) == 70
    bmw.charge()
    assert bmw.drive(100) == 100

def test_kilka_przejazdow():
    bmw = ElectricCar(100)
    assert bmw.drive(70) == 70
    assert bmw.drive(20) == 20
    assert bmw.drive(30) == 10

def test_ladowania_kilka_razy():
    bmw = ElectricCar(100)
    bmw.charge()
    bmw.charge()
    bmw.charge()
    assert bmw.drive(100) == 100

