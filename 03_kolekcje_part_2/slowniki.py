


slownik = {
    "jasiu": 15,
    "stasiu": 22,
    "dupa": "blada",
    True: 'd',
    2.5: 'dd',
    None: 'fhekfh',
    (1,2): 'fgggg',
    'rr': (1,2,3,4,'trurur'),
    #[2,3]: 'gghh', kluczem w slowniku nie moze byc lista gdyz nie jest hashowalna
}

print(slownik['stasiu'])

slownik["jasiu"] = 30

print(slownik["jasiu"])

print(slownik.get("stasiu"))
print(slownik.get("dupa", 33))
print(slownik[None])
print(slownik[(1,2)])
print((1,2).__hash__())
print('dupa' in slownik) #czy w slowniku wystepuje klucz dupa

del(slownik['jasiu'])

for klucz in slownik:
    print(f"w={klucz}")

for klucz in slownik:
    print(f"w={klucz}, {slownik[klucz]}")

for klucz, wartosc in slownik.items(): #metoda items
    print(f"k={klucz}, w={wartosc}")

print()
print(slownik.keys()) #przechodzimy tak naprawde po elementach listy

print(slownik.values()) #metoda values

print(slownik.items()) #metoda items zwraca nam liste tupli jak zawartosc slownika


