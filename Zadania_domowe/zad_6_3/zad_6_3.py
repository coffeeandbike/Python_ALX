"""
Zadanie 6.3 | Policz wszystkie słowa (trudne) (2 godz.)
​
Podstawowa funkcjonalność:
Napisz program, który czyta plik tekstowy i wylicza oraz wypisuje bez powtórzeń wszystkie słowa występujące w
pliku wraz z informacją ile razy dane słowo występuje. Na przykład w ten sposób:
​
```
Zosia -> 34
Asesor -> 35
dwóch -> 35
Tadeusz -> 107
```
​
Ewentualne uproszczenie (w razie problemów z wypisywaniem): wypisz tylko jedno najczęściej występujące słowo.
​
Dalsze rozszerzenia (opcjonalnie):
- posortuj wypisywane słowa
- oprócz liczby poszczególnych słów policz i wypisz także liczbę wszystkich słów, łączną liczbę wszystkich znaków
"""

import string

file = open("pan-tadeusz.txt", "r")

dict = dict()

for row in file:

    row = row.strip()

    row = row.lower()

    row = row.translate(row.maketrans("", "", string.punctuation))

    words = row.split(" ")


    for word in words:


        if word in dict:
            dict[word] = dict[word] + 1
        else:
            dict[word] = 1


print(f'In this txt file is {len(dict)} words')
print()
for key in list(dict.keys()):
    print(key, ":", dict[key])
