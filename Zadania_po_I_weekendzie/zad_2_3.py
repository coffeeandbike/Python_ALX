''''### Zadanie 2.3
​
Napisz program, który odczytuje od użytkownika wiele liczb.
​
Program powinien wyliczyć i na końcu wypisać następujące statystyki:
​
- liczba podanych liczb (ile sztuk),
- suma,
- średnia,
- minimum
- maksimum
​
NIE używaj funkcji wbudowanych!
'''

liczby = []

while True:

    liczba = float(input("Dodaj liczne calkowita lub zmiennoprzecinkowa do listy liczb: "))
    liczby.append(liczba)
    print(liczby)

    co_dalej = input("""Jesli chcesz przejsc do podsumowania, wcisnij 'p' ,
    jesli chcesz podaj nastepna liczne wcisnij 'n' """)



    if co_dalej == 'p':
        print()
        print(f"Podales {len(liczby)} liczb\n")
        print(f"Najwieksza liczba z listy to {max(liczby)}\n")
        print(f"Najmniejsza liczba z listy to {min(liczby)}\n")
        print(f"Suma liczb z listy to {sum(liczby)}\n")
        print(f"Srednia podanych liczb z listy to {sum(liczby) / len(liczby):.3f}\n")
        break
    elif co_dalej == 'n':
        continue
    else:
        print("Ups, wcisnales nie ten klawisz, konczymy zabawe")
        break





