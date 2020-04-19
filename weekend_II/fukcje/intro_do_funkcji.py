# FUNKCJE

# nazwa fukcji(argument1, argument2,....argumentX)
# co funkcja ma robic

# zeby uzyc funkcji musimy ja zdefiniowac

# do definiowana funcji uzywany slowa kluczowego 'def'

# zwyczajowo nazwy funcji sa zapisywane pascal_casem

def hello_world():  # definicja funkcji
    print("Hello world")


hello_world()  # wywolanie funkcji


def powiedz_czesc(imie):  # imie jest argumentem funkcji
    print(f'Czesc {imie} !')


powiedz_czesc('Grzegorz')

moje_imie = 'Janusz'

powiedz_czesc(moje_imie)

nazwisko = 'Nowak '

def suma(a, b):
    return a + b #return powoduje wyjscie z funkcji

suma(20,30)

wynik = suma(4,5)
print(f'wynik to {wynik}')



