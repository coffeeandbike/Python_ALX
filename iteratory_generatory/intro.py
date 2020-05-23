# Iteratory
import random

lista = [10, 20, 30, 40, 50]

iterator = iter(lista)
print(iterator)

print( next(iterator) )
print( next(iterator) )
print( next(iterator) )
print( next(iterator) )
print( next(iterator) ) # 50
# print( next(iterator) ) # przeszlismy przez wszystkie elementy z kontenera, dlatego dostajemy wyjatek StopIteration

print('='*60)


class Losowacz:
    def __init__(self, ile_liczb, od, do):
        self.ile_liczb = ile_liczb
        self.od = od
        self.do = do

    def __iter__(self):
        print("uruchomiono __iter__")
        self.ile_wylosowano = 0
        return self

    def __next__(self):
        print("uruchomiono __next__")

        if self.ile_wylosowano >= self.ile_liczb:
            raise StopIteration

        self.ile_wylosowano += 1

        return random.randint(self.od, self.do)


losowanie = Losowacz(5, 0, 100)
iterator = iter(losowanie)

try:
    print( next(iterator) )
    # ... tutaj moze sie dziac cokolwiek
    print( next(iterator) )
    print( next(iterator) )
    print( next(iterator) )
    print( next(iterator) )

    print( next(iterator) ) # StopIteration

except StopIteration:
    print("Koniec iteratora")

print("="*60)

losowacz2 = Losowacz(3, -10, 10)
for liczba in losowacz2:
    print(liczba)












