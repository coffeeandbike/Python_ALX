"""
Zaimplementuj klasę PremiumEmployee, która będzie klasą pochodną Employee.
Klasa ta powinna umożliwiać dodatkowo przyznawanie bonusów pracownikowi.
> employee = PremiumEmployee('Jan', 'Nowak', 100.0)
> employee.register_time(5)
> employee.give_bonus(1000.0)
> employee.pay_salary()
1500.0

https://yuml.me/preview/e6de225e
"""
import pytest
from OOP.zad_3_ver4 import Employee

class PremiumEmployee(Employee):
    def __init__(self, first_name: str, last_name: str, rate: float):
        super().__init__(first_name, last_name, rate) #uruchamiamy init z klasy Employee
        self.bonus = 0.0

    def give_bonus(self, bonus_amount: float):
        self.bonus += bonus_amount

    def pay_salary(self) -> float:
        salary = super().pay_salary() #przykrywany metode pay_salary "rodzica" plus robimy to co ponizej
        salary += self.bonus
        self.bonus = 0.0
        return salary


def test_czy_dziedziczenie_dziala():
    jas = PremiumEmployee('Jas', 'Kowalski', 50)
    jas.register_time(3)
    assert jas.pay_salary() == 150