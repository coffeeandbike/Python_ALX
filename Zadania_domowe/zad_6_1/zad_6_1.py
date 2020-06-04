"""
Plik CSV z danymi: http://pgradzinski.students.alx.pl/kpython/zawodnicy.csv
​
Korzystając z pliku CSV z danymi skoczków narciarskich napisz programy, które wczytują ten plik i:
​
1. wypisuje najwyższego, najniższego, najcięższego i najlżejszego skoczka;
gdyby kilku miało taką samą wagę lub wzrost, to wystarczy wypisać jednego z nich.

2. liczy ile łącznie ważą reprezentanci Polski (np. żeby sprawdzić czy zmieszczą się w windzie na skocznię ;)).
Pozwól użytkownikowi podać kraj (niekoniecznie musi być Polska).

3. (trudniejsze) dla wszystkich krajów oblicza ilu jest zawodników z tego kraju; tzn. ma się wypisać,
być może w innej kolejności:
​
```
AUT – 2
FIN – 3
GER – 5
NOR – 3
POL – 3
USA – 1
```
"""

import csv

from collections import Counter

with open('zawodnicy.csv', 'r') as file:
    """
    Reading csv file
    """
    #reader = csv.reader(csvfile)
    csvreader = csv.reader(file, delimiter=';')
    competitors = []
    for row in csvreader:
        competitors.append(row)


def min_weight(competitors):
    """

    :param competitors:
    :return: competitors with min weight
    """

    competitors_weights = []
    for competitor in competitors:
        competitor[-1] = int(competitor[-1])
        competitors_weights.append(competitor[-1])

    #print(competitors_weights)
    min_weight = min(competitors_weights)

    print("The lightest competitors:")
    for competitor in competitors:
        competitor[-1] = int(competitor[-1])
        if competitor[-1] == min_weight:
            print(f'{competitor[0]} {competitor[1]} - {min_weight} kg')

def max_weight(competitors):
    """

    :param competitors:
    :return: competitors with max weight
    """

    competitors_weights = []
    for competitor in competitors:
        competitor[-1] = int(competitor[-1])
        competitors_weights.append(competitor[-1])

    max_weight = max(competitors_weights)

    print("The heaviest competitors:")
    for competitor in competitors:
        if competitor[-1] == max_weight:
            print(f'{competitor[0]} {competitor[1]} - {max_weight} kg')


def min_height(competitors):
    """

    :param competitors:
    :return: competitors with min height
    """

    competitors_heights = []
    for competitor in competitors:
        competitor[-2] = int(competitor[-2])
        competitors_heights.append(competitor[-2])

    #print(competitors_weights)
    min_height = min(competitors_heights)

    print("The lowest competitors:")
    for competitor in competitors:
        if competitor[-2] == min_height:
            print(f'{competitor[0]} {competitor[1]} - {min_height} kg')

def max_height(competitors):
    """

    :param competitors:
    :return: competitors with max height
    """

    competitors_heights = []
    for competitor in competitors:
        competitor[-2] = int(competitor[-2])
        competitors_heights.append(competitor[-2])

    #print(competitors_weights)
    max_height = max(competitors_heights)

    print("The highest competitors:")
    for competitor in competitors:
        if competitor[-2] == max_height:
            print(f'{competitor[0]} {competitor[1]} - {max_height} kg')

def how_many_from_country(competitors):
    """

    :param competitors:
    :return: how many competitors in national team
    """
    countries = []

    print("Number of competitors in national teams:")

    for competitor in competitors:
        countries.append(competitor[2])
    c = Counter(countries)
    for country in c:
        print(f'{country} - {c[country]}')



min_weight(competitors)
print()
max_weight(competitors)
print()
min_height(competitors)
print()
max_height(competitors)
print()
how_many_from_country(competitors)
