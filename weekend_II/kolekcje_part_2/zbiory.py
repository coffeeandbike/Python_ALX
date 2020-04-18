
# ZBIORY

zbior = {10, 20, 30, 40, 50}

print(zbior)

#zbior nie jest indeksowalny, nie mozna uzywac operstorow wycinania
# takiego czegos nie zrobimy:
#print(zbior[0])

for element in zbior:
    print(element)

zbior.add(55)
print(zbior)

zbior.remove(55)

#jak probujemy usunac element ktorego nie ma w zbiorze dostaniemy wyjatek

# opracje teoriomnogosciowe
# uzywajac operatora
# Albo uzywajac metody

a = {1,2,3,5}

b = {1,2,3}

#suma:

print(a | b)

c = a | b
d = a.union(b) #sumowanie zbiorow
print(d)

# czesc wpolna - iloczyn:

c = a & b
c = a.intersection(b)
print(c)

# roznica:

c = a - b
c = a.difference(b)
print(c)

# roznica symetryczna - odejmujemy czesc wspolna:

c = a ^ b
c = a.symmetric_difference(b)
print(c)

# czy maja czesc wspolna, czyli czy sa rozlaczne:

print(a.isdisjoint(b))

# czy  b jest podzbiorem a:

print(b <= a)

# czy  a jest nadzbiorem b:

print(a >= b)

#modyfikacja istniejacych zbiorow:

a = {1, 2, 3}
b = {1,2,3,4,5}

#dokladamy elementy z b do a

#a |= b
a.update(b)

#zostawiamy w zbiorze czesc wspolna

a = {1, 2, 3}
b = {1,2,3,4,5}
#a &= b
#lub
a.intersection_update(b)

#usuwamy ze zbioru a rzeczy ktore sa w b

a = {1, 2, 3}
b = {1,2,3,4,5}

# a -= b
#lub :
a.difference_update(b)

#zostawiamy tylko to co nie jest czescia wspolna

a = {1, 2, 3}
b = {1,2,4,5}

a.symmetric_difference_update(b)
print(a)