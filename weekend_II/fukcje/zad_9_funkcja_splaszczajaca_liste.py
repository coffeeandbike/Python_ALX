'''
Zaimplementuj funkcję spłaszczającą podaną listę.
Przykład użycia:
 splaszcz([1, 2, 3, [4, 5, [6]], 7])
[1, 2, 3, 4, 5, 6, 7]
'''

#posluzymy sie rekurencja

# tworzymy pusta liste ktora bedziemy uzupelniac elementami

# przechodzi petla for przez wszystkie elementy z listy

# sprawdzaie typu metodą isinstance()

# dodawanie do listy elementow z innej listy operatorem +=

# Scenariusz
# 1. Tworzymy pusta lista, ktora bedziemy uzupelniac elementami (np. wynik = [])
# 2. Przechodzimy (for) przez wszystkie elementy z listy
#   - jezeli element ktory przetwarzamy jest listą
#       uruchamiam dla tego elementu funkcje spaszcz i rezultat dodaje do zmienneh wynik (+=)
#   - jezeli element ktory przetwarzamy NIE jest listą:
#       to go po prostu dodajemy do listy wynik (append())

import pytest

lista_wejsciowa = [1, 2, 3, [4, 5, [6]], 7]

#plaska_lista = []

def splaszcz(lista_wejsciowa):
    plaska_lista = []

    if isinstance(lista_wejsciowa, list):

        for element in lista_wejsciowa:
            if isinstance(element, list):
                plaska_lista += splaszcz(element)

            else:
                plaska_lista.append(element)

        return plaska_lista

    else:
        raise TypeError("Dane wejsciowe nie sa lista")

splaszcz(lista_wejsciowa)

print(splaszcz(lista_wejsciowa))

def test_dobre_dane():
    assert splaszcz([1, 2, 3]) == [1, 2, 3]
    assert splaszcz([1, 2, 3, [4, 5, [6]], 7]) == [1, 2, 3, 4, 5, 6, 7]

def test_nie_lista():
    with pytest.raises(TypeError):
        splaszcz("dupa")