'''
Napisz program zliczający liczbę znaków w podanym przez użytkownika napisie pomiędzy nawiasami <>.
Nawiasy mogą wystąpić tylko raz.
Ala ma <kota>, a kot ma Alę
'''

# 1 sprawdzam liczbe < i > - powinno byc po 1
# 2 jak jest wiecej niz po 1 to koniec programy

# 3 w petli sprawdzam czy:
# mam zliczzac
# mam przestac zliczac
# czy zlicznie jest wlaczone i wtedy zliczam

napis = input("Podaj napis: ")

# uzyjemy tu metody count ktora zlicza wystapienia danego czegos
if napis.count('<') != 1 or napis.count('>') != 1:
    print("Nieprawidlowa ilosc nawiasiow !!!")
    exit() #konczymy program


liczba_znakow = napis.index('<') - napis.index('>') - 1

print(f"W napisie '{napis}' znaleziono '{liczba_znakow}' znakow miedzy nawiasami <>")
