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



# GENERATORY

def prosty_generator():
    yield 1
    yield 2
    yield 3

g = prosty_generator()
print(type(g))
print( next(g))
print( next(g))
print( next(g))
#print( next(g)) # dostaniemy wyjatkiem StopIteration
print('=' * 20)
for x in prosty_generator():
    print(x)

# yield podobnie jak return zwaraca cos ale nie powoduje wyjscia z funkcji - zatrzymuje sie

print('=' * 20)

# generator function
def silnia(limit):
    wynik = 1
    for i in range (1, limit + 1):
        wynik *= i
        yield wynik

silnnia_generator = silnia(5)

print(next(silnnia_generator))
print(next(silnnia_generator))
print(next(silnnia_generator))
print(next(silnnia_generator))
print(next(silnnia_generator))

print('=' * 20)

for liczba in silnia(5):
    print(liczba)

print(list(silnia(10))) # printujemy liste na podstawie generatora
print(set(silnia(10)))
print(tuple(silnia(10)))


def kwadraty(limit):
    for i in range (1, limit + 1):
        yield 1 ** 2

print('=' * 20)
# generator expression
szesciany = (x ** 3 for x in range(1, 10))

# nie da sie uzyc dwa razy generator expression
for liczba in szesciany:
    print(liczba)









