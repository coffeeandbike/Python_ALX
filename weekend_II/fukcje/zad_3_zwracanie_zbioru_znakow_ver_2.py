'''
Napisz funkcję zwracającą zbiór wszystkich znaków występujących w napisie więcej niż zadana liczba razy.
Przykład użycia:
wiecej_niz('ala ma kota a kot ma ale', 3) {'a', ' '}
'''

# definiujemy funkcje

# liczymy ile jest znakow i dodac je do zbioru ktory na koniec zwracamy

#przypadki testowe: pusty napis, dwa dowolne napisy




def wiecej_niz(napis, ile_znakow):
    napis = napis.lower()
    #wynik = set()

    #for znak in napis:
    #   if napis.count(znak) > ile_znakow:
    #      wynik.add(znak)
    wynik = {znak
             for znak in napis
             if napis.count(znak) > ile_znakow}


    return  wynik

napis = input('Podaj napis: ')
ile_znakow = int(input("Podaj ilosc wystapienia znaku: "))

print(wiecej_niz(napis, ile_znakow))

'''
def test_dla_pustego_napisu():
    assert wiecej_niz('', 0) == set()

def test_przyklady():
    assert wiecej_niz('ala ma kota akot ma ale', 3) == {'a', ''}
'''




