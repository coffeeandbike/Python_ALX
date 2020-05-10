'''
Napisz program obliczający średnią wartość temperatury w danym tygodniu na podstawie temperatur wprowadzonych przez użytkownika
'''

LICZBA_POMIAROW = 7
suma = 0
i = 1
while i <= LICZBA_POMIAROW:
    temperatura = float(input("Podaj odczyt temperatury: "))
    suma += temperatura
    i += 1

print(f"Srednia pomiarow to: {suma/LICZBA_POMIAROW:.2f}")





