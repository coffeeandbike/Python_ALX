'''
Napisz grę polegającą na poszukiwaniu skarbu na dwuwymiarowej planszy o rozmiarach 10 na 10.
Użytkownik może wprowadzać komendy zmieniające położenie postaci.
Po każdym ruchu użytkownik powinien otrzymywać informację o tym, czy zmierza dobrym kierunku.
Wyjście poza planszę oznacza koniec gry.
Po znalezieniu skarbu wypisz liczbę ruchów wykorzystanych przez użytkownika na dojście do celu.
Dodatkowo:
- po wykonaniu większej liczby kroków niż dwukrotność minimalnej liczby kroków umieść skarb w nowym miejscu,
- z prawdopodobieństwem 1/5 nie podawaj graczowi wskazówki po wykonaniu kroku.
'''

"""
1 etap
#pozycje skarbu i gracza
nieskonczona petla while w ktorej:
    zapytac o kierunek ruchu (w,s,a,d)
    pokazujemy pozycje gracza
"""

from math import sqrt #importujemy pierwiastek z modulu matematycznego
from random import randint #generator licz losowych

liczba_krokow = 0

skarb_x = randint(0,10)
skarb_y = randint(0,10)

gracz_x = randint(0,10)
gracz_y = randint(0,10)

min_liczba_krokow = abs(skarb_x - gracz_x) + abs(skarb_y - gracz_y)


while True:
    odleglosc_przed = sqrt((skarb_x - gracz_x)**2 + (skarb_y - gracz_y)**2)

    print(f"Twoja pozaycja to: {gracz_x:2},{gracz_y:2}")

    kierunek = input("Podaje kierunek ruchu (W,S,A,D): ")

    if kierunek == 'w':
        gracz_y += 1

    elif kierunek == 's':
        gracz_y -= 1

    elif kierunek == 'a':
        gracz_x -= 1

    elif kierunek == 'd':
        gracz_x += 1

    else:
        print("Podales niepoprawny kierunek")
        continue

    liczba_krokow += 1

    if gracz_y < 0 or gracz_y > 10 or gracz_x < 0 or gracz_x > 10:
        print("Jestes poza plansza - KONIEC GRY")
        break

    if gracz_x == skarb_x and gracz_y == skarb_y:
        print("Brawo, znalazles skarb")
        break

    odleglosc_po = sqrt((skarb_x - gracz_x) ** 2 + (skarb_y - gracz_y) ** 2)

    if randint(1,5) != 5:
        if odleglosc_po < odleglosc_przed:
            print("Cieplo")
        else:
            print("Zimno")

    if liczba_krokow > min_liczba_krokow*2:
        skarb_x = randint(0,10)
        skarb_y = randint(0,10)
        min_liczba_krokow = abs(skarb_x - gracz_x) + abs(skarb_y - gracz_y)
        liczba_krokow = 0
        print("Slaby z Ciebie poszukiwacz, skarb zostal ukryty gdzie indziej, szukamy od nowa")
        continue




'''
Etap trzeci liczba krokow
zdefiniowac zmienna przed petla ktora zwiekszamy po kazdym kroku
jesli gracz wejdzie na skarb wyswietlamy ilosc krokow ktore wykonal
'''

'''
etap 4 podpowiedz cieplo zimno
dobliczyc odleglosc miedzy pozycja skarbu i gracza
po wukonaniu ruchu liczymy odleglosc
'''

'''
etap 5 nie wysiwtlaj podpowiedzi cieplo zimno z prawdopodobienstwem 1/5
uzywamy randint(1,5) i jezeli wylosuje 5 to nie wyswietlaj podpowiedzi

etap 6 przeniesienie skarbu w inne miejsce
przed petla while liczymy mininalna odlglows miedzy graczem i skarbem
po wykoaniu ruchu sprawdzamy czli liczba wykonanych krokow jest wieksza niz dwukrotnosc minimalnej liczby krokow
jesli tak to liczymy na nowo minimalna liczbe krokow
losujemy nowa pozycje skarbu
zerujemy liczbe wykonnych krokow
'''