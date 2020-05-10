
'''
Zadanie 2.1 | Zagadka matematyczna
​
Program losuje dwie liczby z zakresu od 0 do 99 (patrz poniżej). Podaje te dwie liczby i pyta jaka jest ich suma
(nie podaje jej). Użytkownik ma odgadnąć (no, policzyć w głowie) wynik. Program pyta o wynik wielokrotnie, tak długo,
aż użytkownik poda prawidłowy wynik.
'''

from random import randint

print('Zagadka matematyczna')

liczba_1 = randint(0,99)
liczba_2 = randint(0,99)

print(f"""Wylosowałem dwie liczby,
oto one:
    liczba nr 1 to {liczba_1}
    liczna nr 2 to {liczba_2}
Twoim zadaniem jest podać ich sumę.
    """)

while True:

    suma = int(input('Podaj wyliczoną przez Ciebie sumę: '))
    if suma == liczba_1 + liczba_2:
        print('Brawo, jesteś genialny !!!\nKONIEC')
        break

    else:
        print(f"""Niestety, podales bledna sume, sprobuj jeszcze raz
                liczba nr 1 to {liczba_1}
                liczna nr 2 to {liczba_2}
                """)
        continue
