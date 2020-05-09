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

def suma_mnozenia(a,b):
    wynik_dodawania = a + b
    wynik_mnozenia = a * b
    return wynik_dodawania, wynik_mnozenia

wynik_a, wynik_b = suma_mnozenia(2,7)
print(wynik_a)
print(wynik_b)

#dokumentowanie wlasnego kodu

def iloczyn(a: int, b: int) -> int: # to jest type hinting czyli sugestia jakiego typu powinny byc arumenty i co
                                    #funkcja zwraca
    return a * b

wynik = iloczyn(2,3)
print(wynik)

# WIECEJ O ARGUMENTACH

def opakowywacz(napis, start='>>', end='<<'): #d razu definiujemy argumenty
    return start + napis + end


#wywolania pozycyjne
print(opakowywacz('dupa dupa')) #nie musimy wiec podawc tu wszystkich argumentow bo zdefiniowane sa juz przy definiowaniu

print(opakowywacz('dupa blada', '[[')) # mozemy tez poda tylko jeden arg

#wywolania nazwane

print(opakowywacz(napis='jasny gwin', end='^^'))

print(opakowywacz(end='$$$', start='***', napis='ja cie nie moge')) #mozemy mieszac kolejnoscia podawnaia argumentow

napis = ' dupa \'blada\'' #znak \ sluzy od odbierania znakom specjalnym jego znaczenia
print(napis)

napis2 = "\"\"\"\"\""
print(napis2)

#mozna mieszac arg pozycyjne i nazwane
#wtedy najpierw podajemy arg pozycyjne, potem nazwane

# JAK PRZEKAZYWAC DOWOLNIE WIELE AGRUMENTOW ?

def zliczacz(*args, **kwargs):

    # *arg sluzydo lapania wszystkich arumentow pozycyjnych
    # **kwargs sluzy do lapania wszystkich arumentow nazwanych

    print(args)
    print(kwargs)

zliczacz(1)
zliczacz(1,2,3,4, 'ela', 'dupa') #dostajemy tuple z argumentami

zliczacz(a=2,b=3,c='dupa') #dostaniemy slownik z kwargsami

#mozemy polaczyc argumenty pozycyjne z wartoscia dimyslna np tak:

def foo(a,b, c=15, *args, **kwargs):
    print(a)
    print(b)
    print(c)
    print(*args)
    print(**kwargs)

foo(1,2,3,4,5,6,7, imie='jasiu', wiek=40, wzrost= 150)


# co jest prawda a co falszem ?? #############

zmienna = "ala ma kota" #TRUE

# zmienna - ""              to bedzie falsz
# zmienna = "False"         PRAWDA
# zmienna = 0               false
# zmienna = 10              prawda
# zmienna = []              false dla pustych kolekcji
# zmienna = [0]             true dla kolekcji z czyms
# zmienna = None            false



if zmienna:
    print("prawda")
else:
    print('falsz')


wynik_z_printa = print('ala ma kota')

# print nic sensownego nie zwraca
# w zmiennej wynik_z_printa siedzi None

# funkcja jest typem danych

funkcja1 = lambda x: x ** 3 #pakujemy funkcje lamba do zmiennej funkcja1

wynik = funkcja1(4)
print(wynik)

zmienna2 = funkcja1

wynik = zmienna2(4)
print(wynik)



