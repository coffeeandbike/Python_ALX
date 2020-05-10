"""
Zaimplementuj klasę Employee umożliwiającą rejestrowanie czasu pracy
oraz wypłacanie pensji na podstawie zadanej stawki godzinowej.
Jeżeli pracownik będzie pracował więcej niż 8 godzin (podczas pojedynczej rejestracji czasu)
to kolejne godziny policz jako nadgodziny (z podwójną stawką godzinową).
Przykład użycia:
employee = Employee('Jan', 'Nowak', 100.0)
employee.register_time(5)
employee.pay_salary()
500.0
employee.pay_salary() 0.0
employee.register_time(10)
employee.pay_salary() 1200.0
"""

import pytest

class Employee:
    def __init__(self, first_name: str, last_name: str, rate: float):
        self.first_name = first_name
        self.last_name = last_name
        self.rate = rate
        self.salary = 0.0

    def register_time(self, hours: float):
        if not 0 <= hours <= 24:
            raise ValueError("Incorrect hours value: 0-24")

        if hours <= 8:
            self.salary += hours * self.rate
        else:
            self.salary += 8 * self.rate
            self.salary += 2 * self.rate * (hours -8)


    def pay_salary(self) -> float:
        tmp = self.salary
        self.salary = 0.0
        return tmp




def test_zarejestruj_zwykle_godziny():
    emp = Employee('jan', 'kowalski', 100)
    emp.register_time(5)
    assert emp.pay_salary() == 500


def test_dwie_wyplaty():
    emp = Employee('jan', 'kowalski', 100)
    emp.register_time(5)
    assert emp.pay_salary() == 500
    assert emp.pay_salary() == 0


def test_nadgodziny():
    emp = Employee('jan', 'kowalski', 100)
    emp.register_time(10)
    assert emp.pay_salary() == (8 * 100.0 + 2 * 200)

def test_dwa_dni_pracy():
    emp = Employee('jan', 'kowalski', 100)
    emp.register_time(5)
    emp.register_time(10)
    assert emp.pay_salary() == 1700

def test_ujemne_godziny():
    emp = Employee('jan', 'kowalski', 100)
    with pytest.raises(ValueError):
        emp.register_time(-2)
