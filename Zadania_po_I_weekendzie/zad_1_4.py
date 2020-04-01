'''
Zadanie 1.4 | Opłata hotelowa (ok 1,5 godz.)
​
Potem napisz taki program: użytkownik podaje swój wiek i ile nocy spędzi w hotelu, a program wylicza,
ile trzeba zapłacić. Zasady są takie:
​
- nieletni (poniżej 18 roku życia) płacą 100 zł za noc
- dorośli (ci, którzy mają przynajmniej 18 lat ale mniej niż 65 lat) płacą:
	- 200 zł za noc, jeśli nocują jedną noc
	- 180 zł za noc, jeśli nocują przynajmniej dwie ale mniej niż pięć nocy
	- 150 zł za noc, jeśli nocują pięć lub więcej nocy
- emeryci (ci, którzy mają przynajmniej 65 lat), płacą jak dorośli, ale z 10% zniżki
​
Przykładowo: jeśli użytkownik ma 70 lat i spędzi w hotelu dziesięć nocy, zapłaci 150 zł za noc z 10% zniżki,
czyli 150-15 zł za noc, czyli 135 zł za noc, czyli 1350 zł.
'''

younger_rate = 100
adult_1_night_rate = 200
adult_2_5_nights_rate = 180
adult_5_plus_nights_rate = 150

header = "Accomodation pricing calculator"
explanation = """Program will calculate total cost of your acoomodation"""

print(f'{header:*^40}')
print()
print(f'{explanation}')





