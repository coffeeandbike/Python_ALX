'''
Stwórz następujące funkcje. Niech każda z nich przyjmuje w argument do przeliczenia i zwraca przeliczoną wartość.
​
1. `stopy_na_metry` - przelicza odległość wyrażoną w stopach na metry,
2. `max` - zwraca większą z dwóch liczb - postaraj się nie używać funkcji `max` wbudowanej w pythona
3. `srednia` - oblicza średnią z dwóch liczb,
4. `pole_kola` - oblicza pole koła o podanym promieniu (jeden parametr)
podpowiedź: wartość PI jest dostępna jako `Math.PI`
5. `bmi` - oblicza współczynnik BMI dla podanych dwóch parametrów: wzrostu w metrach i wagi w kg.
6. `pole_trojkata` - z trzema parametrami - oblicza pole trójkąta o podanych bokach z wzoru Herona.
7. `kilometry_na_mile` - przelicza odległość wyrażoną w kilometrach na mile
8. `mile_na_kilometry` - przelicza odległość wyrażoną w milach na kilometry
​
Dla wybranych napisz też interaktywne programy, które pytają użytkownika o dane i wypisują wynik.
'''
import math

import pytest

#argument funkcji stopy_na_metry
# stopy = float(input("Podaj iosc sto do przeliczenia na metry: "))
stopy = 10

#argument funkcji wieksza_liczba
liczba1 = 10
liczba2 = 9

#argument funkcji pole kola
promien = 2

#argumenty do funkcji BMI
waga = 50
wzrost = 150

#argumenty do funkcji pole trojkata
bok_a = 1
bok_b = 0.5
bok_c = -1


######## definicje funkcji #################

def stopy_na_metry(stopy: float) -> float:
    metry = round(stopy / 3.2808, 4)
    return metry


def wieksza_liczba(liczba1: float, liczba2: float) -> float:
    if liczba1 > liczba2:
        return liczba1
    elif liczba2 > liczba1:
        return liczba2

    elif liczba1 == liczba2:
        try:
            return print(f'{liczba1} i {liczba2} sa rowne')
        except:
            ValueError("Podales dwie takie same liczby")


def srednia_dwoch_liczb(liczba1: float, liczba2: float) -> float:
    srednia = (liczba1 + liczba2) / 2
    return srednia


def funkcja_pole_kola(promien: float) -> float:
    if promien >= 0:
        pole_kola = round(math.pi * (promien ** 2), 4)
        return pole_kola
    if promien < 0:
        try:
            print(f"Promien musi by dodatni a podales {promien}")
        except:
            raise ValueError("Podales ujemny promien")

def oblicz_bmi(waga: float, wzrost: float) -> float:

    if wzrost > 0:
        bmi = waga / ((wzrost/100) **2)
        return round(bmi, 3)
    if wzrost == 0:
        try:
            print(f"Wzrost musi by dodatni a podales {wzrost}")
        except:
            raise ValueError("Podales rowny zero wzrost")



def pole_trojkata(bok_a: float, bok_b: float, bok_c: float) -> float:

    p = (bok_a + bok_b + bok_c) / 2



    try:

        if p - bok_c == 0:
            return 0.0

        if p - bok_c > 0:
            pole = math.sqrt(p * (p - bok_a) * (p - bok_b) * (p - bok_c))
            return round(pole, 3)

    except:
        if p - bok_c < 0:
            raise ValueError("Podales dlugosci bokow z ktorych nie mozna zbudowac trojkata")






print(f" Stopy w ilosci {stopy} przeliczone na metry to {stopy_na_metry(stopy)} m")


print(f"Wieksza liczba z dwoch ktore podales to {wieksza_liczba(liczba1, liczba2)}")

print(f"Srednia z dwoch ktore podales to {srednia_dwoch_liczb(liczba1, liczba2)}")

print(f"Pole kola o promieniu {promien} cm wynosi {funkcja_pole_kola(promien)} cm2")

print(f"Twoje MBI wynosi {oblicz_bmi(waga, wzrost)}")

#if not isinstance(pole_trojkata(bok_a, bok_b, bok_c), ValueError):
print(f"Pole trokata o bokach {bok_a}, {bok_b}, {bok_c} wynosi {pole_trojkata(bok_a, bok_b, bok_c)} cm2")



# TESTY
def test_stopy_na_metry():
    assert stopy_na_metry(0) == 0
    assert stopy_na_metry(1) == 0.3048
    assert stopy_na_metry(101) == 30.7852


def test_wieksza_Liczna():
    assert wieksza_liczba(1, 0) == 1
    assert wieksza_liczba(-100, -101) == -100
    assert wieksza_liczba(20, 21) == 21
    assert wieksza_liczba(20, 20) == None


def test_srednia_z_dwoch_liczb():
    assert srednia_dwoch_liczb(0, 0) == 0
    assert srednia_dwoch_liczb(1, 2) == 1.5
    assert srednia_dwoch_liczb(-5, 5) == 0
    assert srednia_dwoch_liczb(1200, 600) == 900


def test_pole_kola():
    assert funkcja_pole_kola(1) == 3.1416
    assert funkcja_pole_kola(10) == 314.1593
    assert funkcja_pole_kola(3.33) == 34.8368
    assert funkcja_pole_kola(-1) == None

def test_oblicz_bmi():
    assert oblicz_bmi(60, 170) == 20.761
    assert oblicz_bmi(60, 0) == None

def test_pole_trojkata():
    assert pole_trojkata(1,1,2) == 0
    assert pole_trojkata(1,0.5,0.4) == None
    assert pole_trojkata(10, 10, 10) == 43.301



