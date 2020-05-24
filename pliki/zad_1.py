"""
Napisz program wypisujący na konsolę zawartość wskazanego pliku wraz z numerami linii.
Obsłuż sytuację, gdy użytkownik nie poda nazwy pliku lub poda błędną nazwę.
Przykład użycia:
$ python test.txt
1: pierwsza linia pliku
2: druga linia pliku
"""

import sys

try:
    file_name = sys.argv[1]

    with open(file_name) as file:
        data = file.read()

        line_number = 1
        for line in data.split('\n'):
            print(f'{line_number}: {line}')
            line_number += 1

except FileNotFoundError:
    print(f'Nie znaleziono pliku {file_name}')
    exit(1)

except IndexError:
    print(f'usage: python zad_1.py file.txt')
    exit(1)