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


while True:

    header = "Accomodation pricing calculator"
    header_2 = """Program will calculate total cost of your acoomodation"""

    print(f'{header:*^40}')
    print()
    print(f'{header_2}')
    print()
    age = int(input('Please, enter your age: '))

    nights = int(input('How many nights are you going to spend with us ? '))



    younger_price = 100 * nights
    adult_1_night_price = 200 * nights
    adult_2_5_nights_price = 180 * nights
    adult_5_plus_nights_price = 150 * nights
    senior_1_price = adult_1_night_price * 0.9
    senior_2_5_nights_price = adult_2_5_nights_price * 0.9
    senior_5_plus_nights_price = adult_5_plus_nights_price * 0.9


    if nights == 1:
        if age < 18:
            print(f'Total price for your accomodation will be {younger_price} PLN')
            break
        elif 18 <= age < 65:
            print(f'Total price for your accomodation will be {adult_1_night_price} PLN')
            break
        elif age > 65:
            print(f'Total price for your accomodation will be {senior_1_price} PLN')
            break
        else:
            print('Something went wrong, try again')
            continue

    elif 2 <= nights < 5:
        if age < 18:
            print(f'Total price for your accomodation will be {younger_price} PLN')
            break
        elif 18 <= age < 65:
            print(f'Total price for your accomodation will be {adult_2_5_nights_price} PLN')
            break
        elif age > 65:
            print(f'Total price for your accomodation will be {senior_2_5_nights_price} PLN')
            break
        else:
            print('Something went wrong, try again')
            continue

    elif nights >= 5:
        if age < 18:
            print(f'Total price for your accomodation will be {younger_price} PLN')
            break
        elif 18 <= age < 65:
            print(f'Total price for your accomodation will be {adult_5_plus_nights_price} PLN')
            break
        elif age > 65:
            print(f'Total price for your accomodation will be {senior_5_plus_nights_price} PLN')
            break
        else:
            print('Something went wrong, try again')
            continue

    else:
        print('Please try again, you entered wrong data')
        continue



