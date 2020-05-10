'''
Napisz program zliczający liczbę wystąpień każdego znaku w podanym przez użytkownika napisie.
'''

# pusty slownik w ktorym bedziemy zliczac litery

# wczutujemy napis

# przechodzimy przez wszystkie znaki

    # jesli nie ma danego znaku w slowniku to dodajemy wartosc
    #jesli jest to zwekszamy wartosc o 1

#slownik:
    #klucz - litera
    #wartosc - ilosc wystapien

znaki_w_napisie = {

}

napis = input("Podaj napis: ")

for znak in napis.lower():
    if znak not in znaki_w_napisie:
        znaki_w_napisie[znak] = 0

    znaki_w_napisie[znak] += 1

for znak, ilosc in znaki_w_napisie.items():
    print(f'{znak} wysyapil {ilosc} razy')

print(sorted(znaki_w_napisie)) # daje nam liste posortowanych kluczy

for znak in sorted(znaki_w_napisie):
    print(f"{znak} - {znaki_w_napisie[znak]}")
