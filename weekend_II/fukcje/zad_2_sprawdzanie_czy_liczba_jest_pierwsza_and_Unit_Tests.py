'''
Napisz funkcję sprawdzającą, czy dana liczba jest liczbą pierwszą. Przykład użycia:
 czy_jest_pierwsza(10)
False
 czy_jest_pierwsza(17)
True
'''

#liczba naturalna wieksza od 1
# bedzie intem
# ma dwa dzielniki - 1 i samego siebie

def czy_pierwsza(liczba):

    if liczba <= 1:
        return False

    for i in range (2, liczba):
        if liczba % i == 0:
            return False

    return True # jesli powyzsze dwa warunki sie nie spelnily to liczba jest liczna pierwsza

#liczba = int(input("Podaj liczbe do sprawdzeia "))

liczba = 7
print(czy_pierwsza(liczba))



#UNIT TEST
def test_czy_jest_pierwsza():
    liczba = 5
    wynik = czy_pierwsza(liczba)
    #asercja ang. assert - jest to uzanie jakiegos zdania za prawdziwe
    assert wynik == True
    assert czy_pierwsza(2)
    assert czy_pierwsza(7)

# liczby pierwsze 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97 itd

#przpadki graniczne

# -100, - 10, -1, 0,1, 6, 12

def test_liczby_nie_pierwsze_ujemne(): #musi byc def_test zeby to bylo rozpoznane jako unit test
    for liczba in range (-100, 0, 5):
        assert czy_pierwsza(liczba) == False

def test_liczby_nie_pierwsze_dodatnie():
    liczby_nie_pierwsze_dodatnie = [1,4,6,8,9,10,12,20,21,35,55,62]
    for liczba in liczby_nie_pierwsze_dodatnie:
        assert  czy_pierwsza(liczba) == False
