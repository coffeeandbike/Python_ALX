'''
### Zadanie 3.3 | Operacje na listach
​
Stwórz następujące funkcje. Każda z nich będzie przyjmowała listę liczb
i na tej podstawie wykona odpowiednie operacje i zwróci odpowiedni wynik.
​
```
lista_liczb = [10, 20, 30, 40]
wynik = suma(lista_liczb)
```
​
- `suma(liczby)` - zwraca sumę liczb z listy `liczby` - postaraj się nie używać funkcji `sum` wbudowanej w pythona
- `srednia(liczby)` - zwraca średnią wartość z listy `liczby`
- `max(liczby)` – zwraca największą wartość z listy `liczby` - postaraj się nie używać funkcji `max` wbudowanej w pythona
- `roznica_min_max(liczby)` – różnica pomiędzy największą a najmniejszą liczbą w liście; `0` jeśli tablica jest pusta
- `wypisz_wieksze(liczby, x)` – wypisuje (`print()`) wszystkie te liczby z listy `liczby`, które są większe od `x`
- `pierwsza_wieksza(liczby, x)` – zwraca (`return`) pierwszą znalezioną w `liczby` liczbę większą od `x`; zwraca `None`, jeśli takiej liczby tam nie ma
- `suma_wiekszych(liczby, x)` – zwraca (`return`) sumę liczb z listy `liczby`, które są większe niż `x`
- `ile_wiekszych(liczby, x)` – liczy ile elementów listy `liczby` jest większych od liczby `x`
- `wypisz_podzielne(liczby, x)` – wypisuje (`print`) wszystkie te liczby z listy `liczby`, które są podzielne przez `x`
- `pierwsza_podzielna(liczby, x)` – zwraca (`return`) pierwszą znalezioną w `liczby` liczbę podzielną przez `x`; zwraca `None`, jeśli takiej liczby tam nie ma
- `znajdz_wspolny(liczby1, liczby2)` – zwraca element (liczbę), który występuje zarówno w liście `liczby1`, jak i `liczby2`; zwraca `None`, jeśli takiego elementu nie ma
Collapse
'''
import pytest


lista_liczb = [-10, -9, -8, -7, -6, -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

lista_liczb_2 = [-5, -3, -1, 1, 3, 5, 7, 9]

liczba_x = 6


# definicja funkcji suma_liczb
def suma_liczb(lista_liczb: list) -> float:
    suma = 0

    for liczba in lista_liczb:
        suma += liczba

    return suma


# definicja funkcji srednia
def srednia_liczb(lista_liczb: list) -> float:
    suma = 0

    for liczba in lista_liczb:
        suma += liczba

    srednia = suma / len(lista_liczb)

    return srednia


# definicja funkcji max_liczba
def max_liczba(lista_liczb: list) -> float:
    max = None

    for liczba in lista_liczb:

        if max is None or liczba > max:
            max = liczba

    return max


# definicja funkcji rozniaca_max_min
def roznica_max_min(lista_liczb: list) -> float:
    max = None
    min = None

    for liczba in lista_liczb:
        if max is None or liczba > max:
            max = liczba
        if min is None or liczba < min:
            min = liczba

    roznica = max - min

    return roznica


# definicja funkcji liczby_wieksze_od_x
def liczby_wieksze_od_x(lista_liczb: list, liczba_x: float) -> list:
    wieksze_od_x = []
    for liczba in lista_liczb:
        while liczba > liczba_x:
            wieksze_od_x.append(liczba)
            break

    if not wieksze_od_x:
        raise ValueError
    else:
        return wieksze_od_x


# definicja funkcji pierwsza_liczba_wieksza_od_x:
def pierwsza_liczba_wieksza_od_x(lista_liczb: list, liczba_x: float) -> float or None:
    wieksze_od_x = []
    for liczba in lista_liczb:
        while liczba > liczba_x:
            wieksze_od_x.append(liczba)
            break
    wieksze_od_x.sort()

    if wieksze_od_x:
        return wieksze_od_x[0]
    else:
        return None


# definicja funkcji suma_liczb_wiekszych_od_x:
def suma_liczb_wiekszych_od_x(lista_liczb: list, liczba_x: float) -> float:
    wieksze_od_x = []

    for liczba in lista_liczb:
        while liczba > liczba_x:
            wieksze_od_x.append(liczba)
            break

    if not wieksze_od_x:
        return 0
    else:
        return sum(wieksze_od_x)


# definicja funkcji ile_liczb_wiekszych_od_x:
def ile_liczb_wiekszych_od_x(lista_liczb: list, liczba_x: float) -> float or str:
    wieksze_od_x = []

    for liczba in lista_liczb:
        while liczba > liczba_x:
            wieksze_od_x.append(liczba)
            break

    if not wieksze_od_x:
        return "Brak wiekszych liczb"
    else:
        return len(wieksze_od_x)


# definicja funkcji liczby_podzieline_przez_x:
def liczby_podzielne_przez_x(lista_liczb: list, liczba_x: float) -> float or str:
    podzielne_przez_x = []

    if liczba_x == 0:
        raise ZeroDivisionError
    else:
        for liczba in lista_liczb:
            if liczba % liczba_x == 0:
                podzielne_przez_x.append(liczba)

    if not podzielne_przez_x:
        return "Brak podzielnych liczb"
    else:
        return podzielne_przez_x


# definicja funkcji liczby_podzieline_przez_x:
def pierwsza_liczba_podzielna_przez_x(lista_liczb: list, liczba_x: float) -> list or None:
    podzielne_przez_x = []

    if liczba_x == 0:
        raise ZeroDivisionError
    else:
        for liczba in lista_liczb:
            if liczba % liczba_x == 0:
                podzielne_przez_x.append(liczba)


    if not podzielne_przez_x:
        return None
    else:
        return podzielne_przez_x[0]

# definicja funkcji wspolne liczby z list:
def wspolne_liczby_z_list(lista_liczb: list, lista_liczb_2: list) -> set or None:
    zbior_lista_liczb = set(lista_liczb)
    znior_lista_liczb_2 = set(lista_liczb_2)

    set_wspolne_liczby = zbior_lista_liczb & znior_lista_liczb_2

    if set_wspolne_liczby:
        return set_wspolne_liczby
    else:
        return None


######## PREZENTACJA WYNIKOW ####################################################################


print(f'Suma liczb z listy wynosi: {suma_liczb(lista_liczb)}')

print(f'Srednia liczb z listy wynosi: {srednia_liczb(lista_liczb)}')

print(f'Najwieksza liczba z listy to: {max_liczba(lista_liczb)}')

print(f'Roznica miedzy najwieksza i najmniejsza liczba z listy to: {roznica_max_min(lista_liczb)}')

# wynik dzialania funkcji liczba_wieksza_od_x:
try:
    print(f'Lista liczby wiekszych od {liczba_x} to: {liczby_wieksze_od_x(lista_liczb, liczba_x)}')
except ValueError:
    print(f"Niestey lista liczb wiekszych od {liczba_x} jest pusta")

print(f'Pierwsza wieksza liczba od {liczba_x} to: {pierwsza_liczba_wieksza_od_x(lista_liczb, liczba_x)}')

# wynik dzialania funkcji suma_liczb_wiekszych_od_x:
print(f'Suma liczb wiekszych od {liczba_x} to: {suma_liczb_wiekszych_od_x(lista_liczb, liczba_x)}')

# wynik dzialania funkcji ile_liczb_wiekszych_od_x:
print(f'Ilosc liczb wiekszych od {liczba_x} to: {ile_liczb_wiekszych_od_x(lista_liczb, liczba_x)}')

# wynik dzialania funkcji liczby_podzielne_przez_x
try:
    print(f'Lista liczb podzielnych przez {liczba_x} to: {liczby_podzielne_przez_x(lista_liczb, liczba_x)}')
except ZeroDivisionError:
    print("Nie dziel cholero przez 0 !!!!")

# wynik dzialania funkcji pierwsza_podzielna_przez_x:
print(f'Pierwsza liczba podzielna przez {liczba_x} to: {pierwsza_liczba_podzielna_przez_x(lista_liczb, liczba_x)}')

# wynik dzialania funkcji wspolne_liczby_z_list:
print(f"Zbior wspolnych liczb z listy: {lista_liczb} \n oraz z listy {lista_liczb_2} \n to: {wspolne_liczby_z_list(lista_liczb, lista_liczb_2)}")


######## TESTY ###############################

def test_suma_liczb():
    assert suma_liczb([10,20,30,40]) == 100
    assert suma_liczb([0]) ==0
    assert suma_liczb([-10,10]) == 0

def test_srednia_liczb():
    assert srednia_liczb([1,2,3,4,5,6,7,8,9]) == 5.0
    assert srednia_liczb([-5,-4,-3,-2,-1,0,1,2,3,4,5]) == 0
    assert srednia_liczb([0,0,0,0,0]) == 0
    assert srednia_liczb([-5,-15, -10]) == -10

def test_max_liczba():
    assert max_liczba([-1500,-100,-1]) == -1
    assert max_liczba([0,0,0,0]) == 0
    assert max_liczba([-1,0,0.001]) == 0.001
    assert max_liczba([-1000,1000, 1001]) == 1001

def test_roznica_max_min():
    assert roznica_max_min([0,0,0,0,0]) == 0
    assert roznica_max_min([-1000,2,3,5000]) == 6000
    assert roznica_max_min([0.001, 0.005, 0.009]) == 0.008

def test_liczby_wieksze_od_x():
    assert liczby_wieksze_od_x([1,2,3,4,5,6,7,8], 6) == [7,8]
    with pytest.raises(ValueError):
        liczby_wieksze_od_x([1,2,3,4,5,6,7,8], 9)
    assert  liczby_wieksze_od_x([-10, 0, 5, 10, 20], -11) == [-10, 0, 5, 10, 20]

def test_pierwsza_wieksza_od_x():
    assert pierwsza_liczba_wieksza_od_x([1,2,3,4,5,6,7,8], 6) == 7
    assert pierwsza_liczba_wieksza_od_x([1,2,3,4,5,6,7,8], 1) == 2
    assert pierwsza_liczba_wieksza_od_x([-999, -800,0, 100], 101) == None

def test_suma_wiekszych_od_x():
    assert suma_liczb_wiekszych_od_x([1,2,3,4,5,6,7,8], 6) == 15
    assert suma_liczb_wiekszych_od_x([1,2,3,4,5,6,7,8], 9) == 0
    assert suma_liczb_wiekszych_od_x([-100,-50, -20, -10], -90) == -80

def test_ile_wiekszych_liczb_od_x():
    assert ile_liczb_wiekszych_od_x([1,2,3,4,5,6,7,8,9], 10) == "Brak wiekszych liczb"
    assert ile_liczb_wiekszych_od_x([1,2,3,4,5,6,7,8,9], 0) == 9
    assert ile_liczb_wiekszych_od_x([-1000,-900, -500, 333], -999) == 3

def test_liczby_podzielne_przez_x():
    with pytest.raises(ZeroDivisionError):
        liczby_podzielne_przez_x([9,8,7,6,5,4], 0)
    assert liczby_podzielne_przez_x([10, 20, 30, 40, 50, 60], 10) == [10, 20, 30, 40, 50, 60]
    assert liczby_podzielne_przez_x([10, 20, 30, 40, 50, 60], 22) == "Brak podzielnych liczb"
    assert liczby_podzielne_przez_x([-64, 50, -40, 0, 4, 8, 5, 88], 8) == [-64, -40, 0, 8, 88]
    assert liczby_podzielne_przez_x([0,0,0,0,0,0], 999) == [0,0,0,0,0,0]

def test_pierwsza_podzielna_przez_x():
    with pytest.raises(ZeroDivisionError):
        pierwsza_liczba_podzielna_przez_x([9,8,7,6,5,4], 0)
    assert pierwsza_liczba_podzielna_przez_x([10, 20, 30, 40, 50, 60], 10) == 10
    assert pierwsza_liczba_podzielna_przez_x([10, 20, 30, 40, 50, 60], 22) == None
    assert pierwsza_liczba_podzielna_przez_x([64, -64, 50, -40, 0, 4, 8, 5, 88], 8) == 64
    assert pierwsza_liczba_podzielna_przez_x([0,0,0,0,0,0], 999) == 0

def test_wspolne_liczby():
    assert wspolne_liczby_z_list([6,7,8,9,10], [1,2,3,4,5]) == None
    assert wspolne_liczby_z_list([-100, -1000, 2, 55], [33, 2, 999, -100]) == {2, -100}