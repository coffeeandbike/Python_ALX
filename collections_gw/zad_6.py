'''
Napisz program zamieniający miejscami w zadanej liście liczb element największy z najmniejszym.
'''

liczby = [1,10,30,55,66,11,33,88,2]
#          0  1  2  3  4  5  6  7
#chcemy zamienic miejscami 1 z 88

#potrzebny indeks najmniejszej liczby i najwiekszej liczby
#zamiana miejscami tych elementow

#WERSJA 1
#uzywany petli for do znalezienia indeksow patrz basics zad 14
#zamieniamy wartosci

#WERSJA 2
#uzywajac funkcji min(), max() znajdujemy najwieksza i najmniejsza wartosc
#znajduje indeks tych eementow w liscie
#zamieniam miejscami

wartosc_min = min(liczby)
wartosc_max = max(liczby)

#jak znalezs indeks elementu o zadanej wartosci w liscie?
indeks_wartosci_min = liczby.index(wartosc_min)
indeks_wartosci_max = liczby.index(wartosc_max)

#tak zamieniamy wartosc zmiennych:
# a, b = b, a
