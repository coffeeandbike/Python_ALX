'''
Napisz program wypisujący na konsolę tabliczkę mnożenia dla liczb od 0 do 9 w postaci tabelki.
'''

#gorny naglowek
print(" "*3, end="")

for i in range (0,10):
    print(f'{i:3}', end="")
print("\n")

#glowna tabliczna mozenia
for i in range (0,10):

    #boczna kolumna:
    print(f'{i:<3}', end="") # < wyrownanie do lewej strony

    for x in range (0,10):
        print(f'{i * x:3}', end="") #kazdy print zajmuje 3 pozycje

    print() #pusty print

# w domu przerobic na wersje od 0 do 100