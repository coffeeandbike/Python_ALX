'''
Napisz program wyświetlający minimalną oraz maksymalną liczbę z wszystkich liczb wprowadzonych przez użytkownika.
Daj użytkownikowi możliwość zakończenia wprowadzania liczb odpowiednią komendą.
Zadbaj o obsłużenie przypadku gdy użytkownik nie wprowadzi żadnej liczby.
'''

min = None

max = None

first = None

while True:
    dane_wejsciowe = input("Podaj liczbe lub wpisz KONIEC aby zakonczyc: ")

    if dane_wejsciowe == "koniec":
        break

    liczba = int(dane_wejsciowe)

    if dane_wejsciowe.isdecimal() is False: #sprawdzamy czy dane wejsciowe sa liczba dziesietna
        print("Niepoprawna liczba")
        continue #wracamy do poczatku petli

    if min is None or liczba < min:
        min = liczba

    if max is None or liczba > max:
        max = liczba

if min is None or max is None:
    print ("Nie podales zadnej liczby")

else:
    #prezentacja wyniku
    print(f"Znalezione minimum to: {min}")
    print(f"Znalezione maximum to: {max}")
