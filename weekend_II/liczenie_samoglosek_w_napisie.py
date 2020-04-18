#Napisz program zliczający liczbę wystąpień samogłosek (a, e, i, o, u, y) w podanym przez użytkownika napisie.

#1 pobieramy napis od uzytkownika

# 2 przechodzimy po kazdej literze napisu (for)

# 3 sprawdzamy czy znak znajduje sie w samogloskach ? jak ta zliczamy


samogloski = ('a','e','i','o','u')

licznik = 0

napis = input("Wpisz napis w ktorym chcesz policzyc samogloski: ")
'''
for litera in napis:
    if litera == 'a' or litera == 'e' or litera == 'i' or litera == 'o' or litera == 'u':
        licznik += 1

print(f"Ilosc samoglowek to {licznik}")
'''
# wersja 2:

#Jak poradzic sobie ze zliczniem duzych liter ? uyc metody lower

for litera in napis:
    if litera.lower() in samogloski: #jesli litera jest w tupli samogloski
        licznik += 1

print(f"Ilosc samoglowek to {licznik}")


