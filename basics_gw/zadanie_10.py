"""
Napisz program, który na podstawie dwóch podanych liczb obliczy wynik zadanej operacji (dodawanie, odejmowanie, mnożenie, dzielenie). W przypadku podania nieprawidłowej operacji program ma wyświetlić odpowiedni komunikat o błędzie.
Przykładowy komunikat programu:
Podaj pierwszą liczbę: 10
Podaj drugą liczbę: 5
Podaj rodzaj operacji: +
Wynik: 15
"""

liczba_1 = float(input("Podaj pierwsza liczne zmiennoprzecinkowa: "))
liczba_2 = float(input("Podaj druga liczne zmiennoprzecinkowa: "))
print("""Mozliwe dzialania:
+ dodawanie
- odejmowanie
* mnozenie
/ dzielenie
** potegowanie""")
operacja = str(input("Podaj dzialanie jakie chcesz wykonac:" ))
'''
if operacja == "+":
    print(f"Wynik dodawania to: {liczba_1 + liczba_2}")
elif operacja == "-":
    print(f"Wynik odejmowania to: {liczba_1 - liczba_2}")
elif operacja == "*":
    print(f"Wynik mnozenia to: {liczba_1 * liczba_2}")
elif operacja == "/":
    print(f"Wynik dzielenia to: {liczba_1 / liczba_2}")
elif operacja == "**":
    print(f"Wynik potegowania to: {liczba_1 ** liczba_2}")
else:
    print("Podales niewlasciwe dzialanie")

#albo tak:
if operacja == "+":
    print(f"{liczba_1}{operacja}{liczba_2}: {liczba_1 + liczba_2}")
elif operacja == "-":
    print(f"{liczba_1}{operacja}{liczba_2}: {liczba_1 - liczba_2}")
elif operacja == "*":
    print(f"{liczba_1}{operacja}{liczba_2}: {liczba_1 * liczba_2}")
elif operacja == "/":
    print(f"{liczba_1}{operacja}{liczba_2}: {liczba_1 / liczba_2}")
elif operacja == "**":
    print(f"{liczba_1}{operacja}{liczba_2}: {liczba_1 ** liczba_2}")
else:
    print("Podales niewlasciwe dzialanie")
'''
#albo tak:

if operacja == "+":
    wynik = liczba_1 + liczba_2
elif operacja == "-":
    wynik = liczba_1 - liczba_2
elif operacja == "*":
    wynik = liczba_1 * liczba_2
elif operacja == "/":
    wynik = liczba_1 / liczba_2
elif operacja == "**":
    wynik = liczba_1 ** liczba_2
else:
    wynik = None

if wynik != None:
    print(f"{liczba_1}{operacja}{liczba_2}={wynik}")
else:
    print("Podales nieoblugiwany operator")
    exit() #uruchomienie tej instrukcji powoduje zakonczenie programu