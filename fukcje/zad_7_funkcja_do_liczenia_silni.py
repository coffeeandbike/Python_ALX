'''
Zaimplementuj funkcję obliczającą silnie dla zadanej wartości. Przykład użycia:
 silnia(5)
120
'''

# wersja przy uzyciu petli for

#liczba = int(input("Podali liczbe calkowita wieksza lub rowna 0 do policzenia silni: "))
import pytest

liczba = 4

def silnia(liczba: int) -> int :

    if liczba < 0:
        raise ValueError("N nie moze byc mniejsze od 0") #rzucamy wyjatkiem typu ValueError

    wynik = 1

    for i in range (1, liczba +1):
        wynik = i * wynik
    return wynik

policzona_silnia = silnia(liczba)

print(policzona_silnia)

def test_testy_silni():
    assert silnia(11) == 39916800
    assert silnia(6) == 720
    assert silnia(0) == 1
    assert silnia(1) == 1

def test_rozne_wartosci():

    przyklady = [(0, 1), (1, 1), (2, 2), (3, 6), (4, 24), (5, 120), (6, 720), (7, 5040), (8, 40320), (9, 362880),
                 (10, 3628800),
                 (11, 39916800), (12, 479001600), (13, 6227020800), (14, 87178291200), (15, 1307674368000),
                 (16, 20922789888000),
                 (17, 355687428096000), (18, 6402373705728000), (19, 121645100408832000), (20, 2432902008176640000)]

    for liczba, wynik in przyklady:
        assert silnia(liczba) == wynik

def test_wartosci_ujemnej():
    with pytest.raises(ValueError): #pytest ma rzucic wyjatek ValueError
        silnia(-10)