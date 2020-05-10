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

'''

WAŻNE !!!!!!!!
Jesli chcesz wykonac unit testy, wykomentuj sekcje 'POBIERANIE DANYCH OD UZYTKOWNIKA'
oraz wpis w sekscji 'DEFINICJE ZMIENNYCH' jakies wartosci

'''
import math

import pytest

##### DEFINICJE ZMIENNYCH ########

# argument funkcji stopy_na_metry
stopy = None

# argument funkcji wieksza_liczba
liczba1 = None
liczba2 = None

# argument funkcji pole kola
promien = None

# argumenty do funkcji BMI
waga = None
wzrost = None

# argumenty do funkcji pole trojkata
bok_a = None
bok_b = None
bok_c = None

# argument funkcji km_na_mile
kilometry = None

# argument funkcji mile na kilometry
mile = None


########### POBIERANIE DANYCH OD UZYTKOWNIKA ###########

# input od uzytkownika - stopy
while True:
    stopy = float(input("Podaj ilosc stop do przeliczenia na metry: "))

    if stopy <= 0:
        print("Podaj wartosc wieksza  0")
        continue
    else:
        break


# input od uzytkownika  - liczby do porownania i do sredniej
liczba1 = float(input("Podaj pierwsza z dwoch liczb po porownania i obliczenia sredniej: "))
liczba2 = float(input("Podaj druga z dwoch liczb po porownania i obliczenia sredniej: "))


# input od uzytkownika - promien kola
while True:
    promien = float(input("Podaj promien kola do obliczenia pola: "))

    if promien <= 0:
        print("Promien musi byc wiekszy od 0, podaj jeszcze raz")
        continue
    else:
        break


# input od uzytkownika - waga i wzrost do BMI
while True:

    wzrost = float(input("Podaj wzrost w cm do obliczenia BMI: "))
    if wzrost > 0:
        break
    else:
        print("Podaj wartosc wieksza  0")
        continue
while True:
    waga = float(input("Podaj wage w kg do obliczenia BMI: "))
    if wzrost > 0:
        break
    else:
        print("Podaj wartosc wieksza  0")
        continue


# input od uzytkownika - boki trojkata
while True:
    #bok A
    bok_a = float(input("Podaj dlugosc boku A w cm do obliczenia pola trojkata: "))
    if bok_a > 0:
        break
    else:
        print("Podaj wartosc wieksza  0")
        continue
while True:
    #bok B
    bok_b = float(input("Podaj dlugosc boku A w cm do obliczenia pola trojkata: "))
    if bok_b > 0:
        break
    else:
        print("Podaj wartosc wieksza  0")
        continue
while True:
    # bok C
    bok_c = float(input("Podaj dlugosc boku A w cm do obliczenia pola trojkata: "))
    if bok_c > 0:
        break
    else:
        print("Podaj wartosc wieksza  0")
        continue

# input od uzytkownika - kilometry na mile
while True:
    kilometry = float(input("Podaj ilosc kilometrow do przeliczenia na mile: "))

    if kilometry <= 0:
        print("Podaj wartosc wieksza  0")
        continue
    else:
        break

# input od uzytkownika - mile na kilometry
while True:
    mile = float(input("Podaj ilosc mil do przeliczenia na kilometry: "))

    if mile <= 0:
        print("Podaj wartosc wieksza  0")
        continue
    else:
        break




######## DEFINICJE FUNKCJI #################

def stopy_na_metry(stopy: float) -> float:
    metry = round(stopy / 3.2808, 4)
    return metry


def wieksza_liczba(liczba1: float, liczba2: float) -> float:
    if liczba1 > liczba2:
        return liczba1
    if liczba2 > liczba1:
        return liczba2

    if liczba1 == liczba2:
        return liczba1 + liczba2


def srednia_dwoch_liczb(liczba1: float, liczba2: float) -> float:
    srednia = (liczba1 + liczba2) / 2
    return srednia


def funkcja_pole_kola(promien: float) -> float:
    if promien >= 0:
        pole_kola = round(math.pi * (promien ** 2), 4)
        return pole_kola

    if promien < 0:
        return


def oblicz_bmi(waga: float, wzrost: float) -> float:
    if wzrost > 0:
        bmi = waga / ((wzrost / 100) ** 2)
        return round(bmi, 3)
    if wzrost <= 0:
        try:
            bmi = waga / ((wzrost / 100) ** 2)
        except:
            raise ValueError("Podales rowny zero wzrost")


def pole_trojkata(bok_a: float, bok_b: float, bok_c: float) -> float:
    p = (bok_a + bok_b + bok_c) / 2

    if bok_a > 0 and bok_b > 0 and bok_c > 0:

        if p - bok_c == 0:
            return 0.0

        if p - bok_c > 0:
            pole = math.sqrt(p * (p - bok_a) * (p - bok_b) * (p - bok_c))
            return round(pole, 3)

        if p - bok_c < 0:
            try:
                pass
            except:
                raise ValueError("Podales dlugosci bokow z ktorych nie mozna zbudowac trojkata")

    elif bok_a < 0 or bok_b < 0 or bok_c < 0:
        try:
            pole = math.sqrt(p * (p - bok_a) * (p - bok_b) * (p - bok_c))
        except:
            raise ValueError("Bok nie moze byc mniejszy lub rowny 0 !!!")


def km_na_mile(kilometry: float) -> float:
    przeliczone_kilometry = round(kilometry * 0.62137, 3)
    return przeliczone_kilometry



def mile_na_km(mile: float) -> float:
    przeliczone_mile = round(mile / 0.62137, 3)
    return przeliczone_mile



############# PREZENTACJA WYNIKOW OBLICZEN ###############

# przeliczone stopy na metry
print(f" Stopy w ilosci {stopy} przeliczone na metry to {stopy_na_metry(stopy)} m")

# wieksza liczba
if wieksza_liczba(liczba1, liczba2) == liczba1 or wieksza_liczba(liczba1, liczba2) == liczba2:
    print(f"Wieksza liczba z dwoch ktore podales to {wieksza_liczba(liczba1, liczba2)}")
elif wieksza_liczba(liczba1, liczba2) == liczba1 + liczba2:
    print("Podales dwie takie same liczby, wiec zadna z nich nie jest wieksza !!")

# srednia liczb
print(f"Srednia z dwoch ktore podales to {srednia_dwoch_liczb(liczba1, liczba2)}")

# pole kola
print(f"Pole kola o promieniu {promien} wynoai {funkcja_pole_kola(promien)} cm2")

# BMI
print(f"Twoje MBI wynosi {oblicz_bmi(waga, wzrost)}")

# pole trojkata
if pole_trojkata(bok_a, bok_b, bok_c):
    print(f"Pole trojkata o bokach {bok_a}, {bok_b}, {bok_c} wynosi {pole_trojkata(bok_a, bok_b, bok_c)} cm2")
else:
    print(f"Z bokow o dlugosciach: {bok_a}, {bok_b}, {bok_c} cm, nie mozna zbudowac trojkata")

# km na mile
print(f"{kilometry} km to {km_na_mile(kilometry)} mil")


# mile na km
print(f"{mile} mil to {mile_na_km(mile)} km")



########### TESTY ##################


def test_stopy_na_metry():
    assert stopy_na_metry(0) == 0
    assert stopy_na_metry(1) == 0.3048
    assert stopy_na_metry(101) == 30.7852


def test_wieksza_Liczna():
    assert wieksza_liczba(1, 0) == 1
    assert wieksza_liczba(-100, -101) == -100
    assert wieksza_liczba(20, 21) == 21
    assert wieksza_liczba(20, 20) == 40


def test_srednia_z_dwoch_liczb():
    assert srednia_dwoch_liczb(0, 0) == 0
    assert srednia_dwoch_liczb(1, 2) == 1.5
    assert srednia_dwoch_liczb(-5, 5) == 0
    assert srednia_dwoch_liczb(1200, 600) == 900


def test_pole_kola():
    assert funkcja_pole_kola(1) == 3.1416
    assert funkcja_pole_kola(10) == 314.1593
    assert funkcja_pole_kola(3.33) == 34.8368
    assert funkcja_pole_kola(-10) == None


def test_oblicz_bmi():
    assert oblicz_bmi(60, 170) == 20.761
    with pytest.raises(ValueError):
        oblicz_bmi(60, 0)


def test_pole_trojkata():
    assert pole_trojkata(1, 1, 2) == 0
    assert pole_trojkata(10, 10, 10) == 43.301
    with pytest.raises(ValueError):
        pole_trojkata(1, 0.5, 0.4)
    with pytest.raises(ValueError):
        pole_trojkata(-1, 10, 5)


def test_km_na_mile():
    assert km_na_mile(1) == 0.621
    assert km_na_mile(0) == 0.000
    assert km_na_mile(10) == 6.214


def test_mile_na_km():
    assert mile_na_km(0) == 0.000
    assert mile_na_km(10) == 16.093