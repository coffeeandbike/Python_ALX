'''
### Zadanie 3.2 | Miesiące
​
Zapytaj użytkownika o nazwę miesiąca i na tej podstawie wypisz mu ile dni na dany miesiąc.
​
Logikę obliczania liczby dni wydziel do osobnej funkcji.
​
**Wersja A**
Nie przyjmuj się lutym - zwracaj zawsze jedną wartość.
​
**Wersja B (trudniejsza)**
Jeżeli użytkownik poda luty - zapytaj go o rok. Na tej podstawie policz czy w tym roku luty był przestępny czy nie.
'''

import pytest

while True:
    # definicja zmiennej do unit testow:
    #miesiac = 'Grudzien'

    # input od uzytkownika
    miesiac = input("Wpisz miesiac ktorego dlugosc chcesz uzyskac, nie uzywaj polskich znakow: ")

    miesiac_lower = miesiac.lower()

    # definicja funkcji obliczajacej dlugosc miesiaca
    def oblicz_dlugosc_misiaca(miesiac_lower: str) -> int:
        if miesiac_lower == 'styczen' or miesiac_lower == 'marzec' or miesiac_lower == 'maj' or miesiac_lower == 'lipiec' or miesiac_lower == 'sierpien' or miesiac_lower == 'pazdziernik' or miesiac_lower == 'grudzien':
            return 31

        elif miesiac_lower == 'kwiecien' or miesiac_lower == 'czerwiec' or miesiac_lower == 'wrzesien' or miesiac_lower == 'listopad':
            return 30

        elif miesiac_lower == 'luty':
            rok = int(input("Podaj rok, gdyz Luty co cztery lata ma 29 dni: "))
            if rok % 4 == 0:
                return 29
            elif rok % 4 != 0:
                return 28

        else:
            raise NameError


    try:
        #tworzenie zmiennej z wynikiem dzialania funkcji
        dlugosc_miesiaca = oblicz_dlugosc_misiaca(miesiac_lower)

        #prezentacja wyniku
        print(f"Dlugosc miesiaca: {miesiac} to {dlugosc_miesiaca} dni\n KONIEC")
        break

    # obsluga wyjatku
    except NameError:
        print('Podales zla nazwe miesiaca, sprobuj ponownie')
        continue

# testy
def test_dlugosc_miesiaca():
    assert oblicz_dlugosc_misiaca('styczen') == 31
    assert oblicz_dlugosc_misiaca('lipiec') == 31
    assert oblicz_dlugosc_misiaca('lipiec') == 31
    assert oblicz_dlugosc_misiaca('kwiecien') == 30
    assert oblicz_dlugosc_misiaca('grudzien') == 31
    with pytest.raises(NameError):
        oblicz_dlugosc_misiaca('dupa')
    with pytest.raises(NameError):
        oblicz_dlugosc_misiaca('stycze')
    with pytest.raises(NameError):
        oblicz_dlugosc_misiaca('grudzie')
    with pytest.raises(NameError):
        oblicz_dlugosc_misiaca('kiecien')





