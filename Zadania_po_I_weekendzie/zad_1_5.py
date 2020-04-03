'''
### Zadanie 1.5 | Pole trójkąta (ok. 1 godz.)
​
Program, który odczytuje trzy liczby, sprawdza czy liczby te mogą stanowić boki trójkąta
(np. z 2, 2 i 5 nie da się ułożyć trójkąta, prawa?), a jeśli mogą, oblicza pole powierzchni trójkąta o takich bokach.
​
Wykorzystaj trzeci wzór z [listy](https://www.matemaks.pl/wzory-na-pole-trojkata.html).
​
Tutaj użyj jednego z poznanych sposobów komunikacji z użytkownikiem. Pierwiastek kwadratowy to:
​
```
import math
​
x = math.sqrt(10)
'''

from math import sqrt

print("Triangle checker")
print()
print("""This app will check whether from entered side's lengths
 it's possible to build a triangle""")
print()
while True:
    a = float(input('Please enter side A in cm: '))

    b = float(input('Please enter side B in cm: '))

    c = float(input('Please enter side C in cm: '))
    print()
    ab = a + b
    ac = a + c
    bc = b + c

    if ab > c and ac > b and bc > a:
        p = (a + b + c) / 2
        field = sqrt(p * (p - a) * (p - b) * (p - c))
        print('Traingle is possible to build and his field is:')
        print(f'{field:.2f} cm2')
        print()
        next = input("Please enter 'next' if you can try build next triangle or any letter for exit: ")
        if next == 'next':
            continue
        else:
            break
    else:
        print("Sorry, bat I can't create a triangle from the sides you entered")
        next = input("Please enter 'next' if you can try build next triangle or any letter for exit: ")
        if next == 'next':
            continue
        else:
            break





