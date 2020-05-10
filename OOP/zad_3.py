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

class Employee:
    def __init__(self, first_name: str, last_name: str, rate: float):
        self.first_name = first_name
        self.last_name = last_name
        self.rate = rate
        self.work_time = 0.0

    def register_time(self, hours: float):
        self.work_time += hours

    def pay_salary(self) -> float:
        salary = self.work_time * self.rate
        self.work_time = 0.0
        return salary


emp = Employee('jan', 'kowalski', 100)
emp.register_time(5)
emp.register_time(3)
print(emp.pay_salary())
print(emp.pay_salary())
emp.register_time(4)
print(emp.pay_salary())
print(emp.pay_salary())
