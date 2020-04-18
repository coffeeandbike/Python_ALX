
# list comprehension

wynik = [] #pusta lista

for wartosc in range (0,10):
    wynik.append(wartosc)

#wyrazenie listowe:

wynik_2 = [wartosc for watosc in range(0,10)]
print(wynik_2)

#celem wyrazenia listowego jest zrobienie listy

wynik_3 = [wartosc**2 for wartosc in range(0,20)]
print(wynik_3)

##########

dane =[10,20,30,40,50,60,70,80,90,100]

dane_polowkowe = [liczba/2 for liczba in dane]
print(dane_polowkowe)

# sa rowniez wyrazenie slownikowe i wyrazenia zbiorow

# nie ma wyrazen listowych dla tupli

pensje = [1000,3000,2500,1500,5000] #kwoty brutto

pensje_bez_podatku = [round(pensja * 0.81, 2) for pensja in pensje ] #zaokraglamy do dwoch miejsc

print(pensje_bez_podatku)

#liczymy premie od pensji
#jesli pensja do 2 tys premia 10% jak wiecej to nie ma premii

premie = []
for pensja in pensje:
    if pensja <= 2000:
        premie.append(0.1) #wkladamy do listy wartosci premii
    else:
        premie.append(0.0)
print(premie)

#to samo za pomoca wyrazenia listowego

premie =[0.1 if pensja <= 2000 else 0.0 for pensja in pensje]
print(premie)

#łączenie dwoch list:
#funkcja zip

print(list(zip(pensje_bez_podatku, premie)))

wartosc_premii =[pensja * premie for pensja, premie in pensje]

print(wartosc_premii)