"""

Zadanie 2.2 | Choinka
​
Napisz program, który wczytuje liczbę całkowitą, a następnie na konsolę wypisuje w tylu liniach "choinkę" ze znaków `*`.
Np. dla parametru 3 powinno się wypisać:
​

    *
  * * *
* * * * *
"""
while True:

    ilosc_linijek = int(input("Podaj ilosc 'poziomow' choinki do wyswirtlenia: "))
    i = 1
    ilosc_znakow = 1

    najdluzszy_wiersz = (ilosc_linijek * 2) -1


    while i <= ilosc_linijek:
        print(f"{'*' * ilosc_znakow:^{najdluzszy_wiersz}}", end="\n")
        i += 1
        ilosc_znakow += 2

    co_dalej = input("Jesli chcesz narysowac kolejna choinke, wcisnij 'n' ")

    if co_dalej == 'n':
        continue
    else:
        print("KONIEC")
        break
