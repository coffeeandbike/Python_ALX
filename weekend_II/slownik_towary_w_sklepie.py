'''
Napisz program wyliczający kwotę należną za zakupiony towar na podstawie podanej przez użytkownika wagi i nazwy produktu.
Do przechowywania informacji o cenie za kilogram danego produktu użyj słownika. Wypisz wszystkie dostępne produkty w sklepie.
'''

# 1 robimy slownik z produktami

# 2 wyswietlam slownik

# 3 pytam o produkt ktory chce kupic i sprawdzam czy jest w produktach

# 4 wczutujemy ile kg chce kupic

# 5 liczymy naleznosc

produkty = {
    'ziemniaki': 1.5,
    'pomidory': 6,
    'marchew': 1.2,
    'seler': 2.2,
    'pietruszka': 3.0,
}

for produkt, cena in produkty.items():
    print(f'{produkt} - {cena:.2f} zł/kg')

co_kupic = input("Jaki towar chcesz kupic ? ")

if co_kupic not in produkty:
    print("Nie ma takiego produktu, ciao")
    exit(1)

if co_kupic in produkty:
    ilosc = float(input(f"Ile kg {co_kupic} chcesz kupic ?"))
    naleznosc = ilosc * produkty[co_kupic]
    print(f"Za {ilosc} kg {co_kupic} zaplacisz {naleznosc:.2f} zł")
