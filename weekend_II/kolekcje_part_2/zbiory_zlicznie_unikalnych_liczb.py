'''
Napisz program zliczający liczbę unikalnych liczb wprowadzonych przez użytkownika.
Sprawdź jak dużo z tych liczb jest liczbami parzystymi w zakresie 0-100 - w tym celu skorzystaj z operatora iloczynu.
'''

# 1 ile unikalnych liczb wprowadzil uzytkownik

# w petli while wczytujemy dane do zbioru

# po petli pokazujemy ile unikalnych liczn podal uzytkowanik

#ile wprowadzonych liczb bylo parzystych
# czli trzeba zrobic zbior liczb parzystych w petli for in range (0,100, 2)

#robimy iloczyn na dwoch zbiorach zeby pokaza ktore prowdadzone byly parzyste

# UWAGA:
# zbior = {} tworzy pusty slownik !!!!!

wprowadzone_liczby = set()

while True:
    liczba = (input("Podaj liczbe: "))
    if liczba == 'koniec':
        break
    else:
        wprowadzone_liczby.add(float(liczba))

print(f"Unikalne liczby to: {wprowadzone_liczby}\n")
print(f"Ilosc unikalnych liczb to: {len(wprowadzone_liczby)}")

liczby_parzyste = set()

for i in range (0, 101, 2):
    liczby_parzyste.add(i)

print(f'Liczby parzyste to {wprowadzone_liczby & liczby_parzyste}\n')
print(f'ilosc liczb parzystych podanych przez Ciebie to {len(liczby_parzyste & wprowadzone_liczby)}')



