# KOLEKCJE

# Tupla, krotka (ang. tuple)

a = (1, 2, 3, 4)
#    0 1 2 3
print(a)

# jak sie dostac do elementow tupli:
# numracja elementow w tupli jest od 0

print(a[0])

b = (1, 3.5, "dupa", True) #mozna wsadzic tu zmienne roznego typu

print(b[2])

#mozna trzymac tuple w tupli:

c = ((1,2,3), (True, False), ("Dupa", 3.5, 2))
#     0 1 2     0      1        0      1    2
print(c[0])
print(c[0][1])

print(type(c[1][0]))

#jak zrobimy tak:
d = (100) #to nie jest tupla tylko liczba
e = (100,) # to jest tupla

print(type(d))
print(type(e))

#tworzenie pustej tupli jest stosunkowo malo przydatne
f = tuple()

#dosteo do elementow - operator []

g = ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h')
#     0    1    2    3    4    5    6    7
#    -8   -7   -6   -5   -4    -3    -2  -1
print(g[0]) #pierszy element
print(g[0:3]) #od 0 do 2 włącznie, 3 się nie wlicza, przedzial lewostronie domkniety, prawostronnie otwarty
print(g[1:4]) # b,c,d
print(g[2:]) # od elementu z indeksem 2 do konca
print(g[-7:-2])
print(g[-3:]) #wyciagamy trzy ostatnie elementy
print(g[:-1]) # od poczatku do minus 1
print(g[:]) # cała tupla g

print(g[::2]) # po drugim dwukropku wpisujemy krok z jakim chcemy wyciagac elementy z tupli

print(g[::-1]) # wyciągamy elementy ale od końca tupli

# elementy w tupli są niezmienialne, tupla jest niemutowalna po utworzeniu
# g[0] = "jasny gwint" - to nie zadziala, będzie błąd TypeError

print(len(g)) # sprawdzamy dlugosc tupli
print('e' in g) #czy literka 'e' znajduje sie w tupli

h = (1,2,3)
print(max(h)) # znajdujemy maximum
print(min(h)) # znajdujemy minimum
print(sum(h)) # suma elementow w tupli

j = (5,6,7)

k = h + j # łączymy dwie tuple w jedną
print(k)

l = h + g
print(l)

m = j*2 # powielamy tuple 2 dwa razy
print(m)

# LISTY
a = [10,20,30,40,50,60,70,80,90,100]
print(a)
print(len(a))
# operator wycinania dziala dokladnie tak samo jak na tupli
#lista jest mutowalna
a[0] = 11
print(a)

a.append(110) #dopisujemy na koncu listy a 110
print(a)

a.insert(1,12) # dopisujemy pod indeks 1 element 12
print(a)

a[0:2] = [1,2] #zamieniamy na raz pierwszy i drugi element na nowe
a[0:2] = [-1,-2,-3] # ten trzeci element "wpychamy"

a.extend([11,22,33]) # rozszerzamy liste o trzy elementy dodane na koncu
a[1:1] = [111,222,333] #wpychamy elementy na index 1

del(a[0]) #usuwamy pierwszy element

#sortowanie listy
a.sort() #sortujemy liste ale uwaga - elementy sie uloza w nowy sposob niz przy utworzeniu
print(a)

# PETLA FOR
for i in range (10): #dziesiec przejsc petli od 0 do 9
    print(i) #dodaje znak enter po kazdym princie
    print(i, end=" ")

for i in range (3,10): # od 3 do 9
    print(i, end=" ")


for i in range (3,10,2): # od 3 do 9 co 2
    print(i, end=" ")

#dostep w petli for do indeksu i wartosci danego elementu
liczby = [10,20,30,40,50,60]

for indeks, wartosc in enumerate(liczby): # enumerate daje dostep do indeksu
    print(indeks, wartosc)

#NAPISY