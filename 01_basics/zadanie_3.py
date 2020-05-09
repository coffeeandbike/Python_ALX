'''
Napisz program wypisujący na konsolę Twoje imię i wzrost. Do przechowywania informacji o Twoim imieniu i wzroście użyj zmiennych.
Przykładowy komunikat programu:
Imię: Jan
Wzrost: 180
'''

imie = "Grzegorz"
wzrost = 175

print("Imie: ",imie)
print("Wzrost: ", wzrost) #funkcja print sama przerobi wzrost na stringa
print("Wzrost: " + str(wzrost))
#funcja str przerabia to co jej podamy na napis
#do funkcj print moge przekazz wiecej argumentow oddzielejac je przecinkiem