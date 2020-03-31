"""
Napisz program sprawdzający czy podana przez użytkownika liczba jest:
- większa od 10
- mniejsza równa 15
- podzielna przez 2 (użyj operatora modulo)
Przykładowy komunikat programu:
Podaj liczbę: 15
Większa od 10: True
Mniejsza równa 15: True
Podzielna przez 2: False
"""

liczba = int(input("Podaj liczbe: "))

print(f"Liczba {liczba} jest wieksza od 10 {liczba > 10}")
print(f"Liczba {liczba} jest wieksza od 10 {liczba == 15}")
print(f"Liczba {liczba} jest wieksza od 10 {liczba % 2 == 0}")