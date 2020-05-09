"""
Napisz program sprawdzający czy podana przez użytkownika liczba:
- jest nieparzysta, podzielna przez 3 i większa od 10
- lub jest to liczba 7.
"""

liczba = int(input("Podaj liczbe: "))

wynik = (liczba % 2 != 0 and liczba % 3 == 0 and liczba > 10) or liczba == 7
print(f"Wynik sprawdenia: {wynik}")