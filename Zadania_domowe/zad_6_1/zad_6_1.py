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

with open('zawodnicy.csv', 'r') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        print(row)


