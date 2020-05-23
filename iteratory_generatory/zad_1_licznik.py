'''
Zaimplementuj iterator odliczający od 0 do zadanego limitu.
Przykładowe użycie:
for number in Counter(10):
'''

class Licznik:
    def __init__(self, limit):
        self.limit = limit


    def __iter__(self):
        print("Zaczynamy")
        self.ile_oddano = 0
        return self

    def __next__(self):
        print("Nastepna liczba:")

        if self.ile_oddano >= self.limit:
            raise StopIteration

        wynik = self.ile_oddano
        self.ile_oddano += 1

        return wynik


for liczba in Licznik(20):
    print(liczba)

