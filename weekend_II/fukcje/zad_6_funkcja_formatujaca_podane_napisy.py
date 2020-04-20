'''
Zaimplementuj funkcję formatującą podane napisy.
Przykład użycia:
#>>> formatuj(
        'koszt $cena PLN',
        'kwota $cena brutto',
        cena=10,
)
'koszt 10 PLN\nkwota 10 brutto'
'''

# 1 zdefiniowac fukcje ktora ma args i kwargs

# 2 w definicji funkcji zrobic zmienna(liste) do trzymania przetworzonych napisow

# iteruje po napisach (*args)

# iteruje po wszstkich **kwargsach

# TESTY

def formatowaczka(*args, **kwargs):

    wynik = []

    for napis in args:
        for nazwa, wartosc in kwargs.items():
            napis = napis.replace(f'${nazwa}', str(wartosc))

        wynik.append(napis)

    return '\n'.join(wynik)

sformatowany_napis = formatowaczka('koszt $cena PLN', 'kwota $cena brutto', cena=10)
#                                      *args               *args            **kwargs

print(sformatowany_napis)

sformatowany_napis2 = formatowaczka('koszt $cena PLN', 'kwota $cena brutto', 'ilosc $ilosc kg', cena=10, ilosc=5)
#                                      *args               *args            **kwargs

print(sformatowany_napis2)

# Testy
# - nie ma podstawienia Hello World! -> Hello World!
# - dwa napisy ale bez podstawienia
#       'Hello World!', 'Hello Python' -> 'Hello World!\nHello Python'
# - 'Czesc $imie $nazwisko', imie="Jan", naziwsko="Kowalski" -> 'Czesc Jan Kowalski'
# - jak zmienna nie uzyta 'Hello World', imie="Jan" -> 'Hello World'
# - jak nie ma zmiennej 'Hello $imie' -> 'Hello $imie'

def test_testy_formatowaczki():
    assert formatowaczka('Hello World!') == "Hello World!"
    assert formatowaczka('Hello World!', 'Hello Python') == 'Hello World!\nHello Python'
    assert formatowaczka('Czesc $imie $nazwisko', imie="Jan", nazwisko="Kowalski") == 'Czesc Jan Kowalski'
    assert formatowaczka('Hello World', imie="Jan") == 'Hello World'
    assert formatowaczka('Hello $imie') == 'Hello $imie'