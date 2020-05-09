"""
Napisz program obliczający koszt przejazdu z miasta A do B na podstawie podanej przez użytkownika liczby kilometrów, ceny paliwa oraz spalania. Zapytaj użytkownika także o nazwy miejscowości.
Przykładowe komunikaty programu:
Miasto A: Warszawa
Miasto B: Gdańsk
Dystans Warszawa-Gdańsk: 420
Cena paliwa: 4.55
Spalanie na 100 km: 5.5
Koszt przejazdu Warszawa-Gdańsk to 105 PLN
"""

# input wczytywanie danych z konsoli

miasto_a = input("Podaj miasto poczatkowe: ")
miasto_b = input("Podaj miasto koncowe: ")

# int(x) przerabia int na inta
# float(x) przerabia x na float

dystans = int(input(f"Podaj dystans z {miasto_a} do {miasto_b}"))
cena = float(input("Cena za litr paliwa: "))
spalanie = float(input("Spalanie na 100km: "))

koszt = dystans / 100 * spalanie * cena
print(f"Koszt przejazdu z {miasto_a} do {miasto_b} to {koszt:.2f} zł")


