''''### Zadanie 2.3
​
Napisz program, który odczytuje od użytkownika wiele liczb.
​
Program powinien wyliczyć i na końcu wypisać następujące statystyki:
​
- liczba podanych liczb (ile sztuk),
- suma,
- średnia,
- minimum
- maksimum
​
NIE używaj funkcji wbudowanych!
'''

min = None
max = None
suma = 0
roznica = 0
licznik = 1
licznik_liczb = 0
srednia = 0
start = 0


while True:

    wejscie = input("''Podaj liczne calkowita lub wpisz 'koniec' zeby zakonczyc"
                    "i wyswietlic podsumowanie: """)

    if wejscie == 'koniec':
        break

    #liczba = int(wejscie)

    if wejscie.isdecimal() is False:  # sprawdzamy czy dane wejsciowe sa liczba dziesietna
        print("Niepoprawne dane")
        continue  # wracamy do poczatku petli

    elif wejscie.isdecimal() is True:

        liczba = int(wejscie)

        if min is None or liczba < min:
            min = liczba


        if max is None or liczba > max:
            max = liczba


        if licznik == 1:
            roznica = start + liczba

        if licznik > 1:
            roznica -= liczba

        suma += liczba
        srednia = suma / licznik
        licznik += 1
        licznik_liczb += 1


if min is None or max is None:
    print ("Nie podales zadnej liczby - uruchom program ponownie")

else:
    print(f"Znalezione minimum to: {min}")
    print(f"Znalezione maximum to: {max}")
    print(f"Suma liczb to: {suma}")
    print(f"Roznica liczb to: {roznica}")
    print(f"Średnia liczb to: {srednia}")
    print(f"Ilosc podanych liczb to: {licznik_liczb}")