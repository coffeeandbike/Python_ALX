'''
Zadanie 4.3 | Pociąg
​
Stwórz klasę `Pociag`. Klasa niech ma dwa atrybuty: predkość (początkowa wartość to 10) i ilosc_paliwa (początkowa wartość to 1000).
​
Dodaj do klasy `Pociag` metode `opis`. Ta metoda niech zwraca napis o treści "Moja predkość to (ileś tam).
Mam jeszcze (ileś tam) litrów paliwa." Dodatkowo zaimplementuj metodę `__str__`.
​
Dodaj metode `przyspiesz`. Ta metoda niech przyjmuje jeden argument mówiący, o ile ma zwiekszyć się prędkość.
Ta metoda niech zwiększa predkość pociągu o tyle, ile jest powiedziane w argumencie.
I niech zmniejsza ilość paliwa o: `(nowa predkosc - stara_predkosc) * (stara predkosc / 100)`.
​
Niech nie da się jednorazowo zwiększyć prędkości o więcej niż 75% (
jeśli ktoś spróbuje tak zwiększyć prędkość, prędkość niech pozostaje po prostu bez zmian).
Niech nie da sie zwiększyć prędkości, jeśli pociąg nie ma juz paliwa (jeśli ktoś spróbuje zwiększyć prędkość,
 kiedy nie ma paliwa, prędkość niech pozostaje po prostu bez zmian).
​
Przetestuj swoje rozwiązanie i napisz testy, w których:
- zwiększysz prędkość pociągu o 5 km/h i wypisze jego opis
- zwiększysz prędkość pociągu o 20 km/h i wypisze jego opis
- zwiększysz prędkość pociągu o 8 km/h i wypisze jego opis
- zwiększysz prędkość pociągu o 10 km/h i wypisze jego opis
'''
from typing import List

import pytest


class Train:
    def __init__(self, speed: float, fuel: float):
        self.speed = speed
        self.fuel = fuel



    def acceerate (self, how_fast: float):
        """
        Method for accelerating the train
        :param how_fast: 
        :return: speed after accelerating
        """
        train_parameters: list = []

        # if accelerate more that 75% current speed
        if how_fast > 0.75 * self.speed:
            self.speed = self.speed
            #self.fuel = (new_speed - self.speed) * (self.speed / 100)
            train_parameters.append(self.speed)
            train_parameters.append(self.fuel)
            return train_parameters

        else:
            # if there is no fuel
            if self.fuel <= 0:
                self.speed = self.speed
                self.fuel = 0.0
                train_parameters.append(self.speed)
                train_parameters.append(self.fuel)
                return train_parameters

            # if accelerate less that 75% current speed and fuel is > 0
            else:
                old_speed = self.speed
                new_speed = old_speed + how_fast
                self.fuel -= (new_speed - old_speed) * (old_speed / 100)
                self.speed = new_speed
                train_parameters.append(self.speed)
                train_parameters.append(self.fuel)
                return train_parameters

    def train_status(self) -> str:
        return f"Current train speed is {self.speed}\nCurrent fuel state is {self.fuel}"

    def __str__(self) -> str:
        return self.train_status()


#ciuchcia1 = Train(10, 1000)



# TESTS

def test_accelerate_once():
    ciuchcia1 = Train(10, 1000)
    assert ciuchcia1.acceerate(5) == [15, 999.5]
    assert ciuchcia1.train_status() == f"Current train speed is 15\nCurrent fuel state is 999.5"

def test_accelerate_too_much():
    ciuchcia1 = Train(10, 1000)
    assert ciuchcia1.acceerate(8) == [10, 1000]
    assert ciuchcia1.train_status() == f"Current train speed is 10\nCurrent fuel state is 1000"

def test_accelerate_few_times():
    ciuchcia1 = Train(10, 1000)
    ciuchcia1.acceerate(5)
    assert ciuchcia1.train_status() == f"Current train speed is 15\nCurrent fuel state is 999.5"
    ciuchcia1.acceerate(20)
    assert ciuchcia1.train_status() == f"Current train speed is 15\nCurrent fuel state is 999.5"
    ciuchcia1.acceerate(8)
    assert ciuchcia1.train_status() == f"Current train speed is 23\nCurrent fuel state is 998.3"
    ciuchcia1.acceerate(10)
    assert ciuchcia1.train_status() == f"Current train speed is 33\nCurrent fuel state is 996.0"

def test_accelerate_without_fuel():
    ciuchcia1 = Train(10, 0)
    assert ciuchcia1.acceerate(5) == [10, 0]
    assert ciuchcia1.train_status() == f"Current train speed is 10\nCurrent fuel state is 0.0"
