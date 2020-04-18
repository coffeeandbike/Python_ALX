'''
W sesji interaktywnego środowiska stwórz następujące struktury danych korzystając ze skróconej wersji zapisu:
- listę zawierającą liczby zmiennoprzecinkowe od 0.0 do 1.0 z krokiem 0.1
- zbiór tupli zawierających 3 elementy - daną liczbę, jej kwadrat i jej sześcian - w przedziale od -10 do 10
- słownik mapujący napisy na ich długość powstały ze zbioru napisów
'''

#1
a = [x/10 for x in range(0,11)] #range nie dziala na ulamkach !!!!!!
print(a)

#2

b = {(x, x ** 2, x ** 3) for x in range(-10,11)}
print(b)

#3

c = {'dupa', "lupa", 'kupa', 'b', 'zasranykaczor'}

slownik_c = {
napis: len(napis)
for napis in c
}
print(slownik_c) #wyrazenie slownikowe



