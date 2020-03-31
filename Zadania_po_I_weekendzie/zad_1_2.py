'''
Napisz taki program: użytkownik ma podać, w jaki dzień tygodnia oddał buty do szewca
(poniedziałek to dzień 1, wtorek to dzień 2 itp.). Ma też podać, ile dni będzie trwała naprawa.
​
Program ma wypisać, w jaki dzień tygodnia buty będą gotowe do odbioru.
Jeśli tak będzie ci wygodniej, możesz założyć, że naprawa butów nigdy nie będzie trwała dłużej niż siedem dni.
'''

powitanie = "SUPER PROGRAM - KIEDY BUTY"
print(f'{powitanie:_^40}')
print()
print("""Program obliczy, w ktory dzien tygodnia
Twoje buty beda do odbioru, jesli podasz w nastepujace sposob
dzien oddania butow do naprawy:
Poniedzialek - 1
Wtorek - 2
Sroda - 3
Czwartek -4
Piatek -5
Sobota - 6
Niedziela -7""")

dzien_oddania = int(input('Podaj w jaki dzien oddales buty do szewca: '))


ilosc_dni_naprawy = int(input('Ile dni bedzie trwala naprawa ? '))

ilosc_tygodni = int(abs(ilosc_dni_naprawy / 7))
ilosc_dni_w_tygodniu = (ilosc_dni_naprawy % 7)


print()
if ilosc_tygodni >= 1:
    if ((dzien_oddania + 7) % 7) == 1:
        print(f'Twoje buty beda gotowe w poniedzialek za {ilosc_tygodni} tygodni/e')
    elif ((dzien_oddania + 7) % 7) == 2:
        print(f'Twoje buty beda gotowe we wtorek za {ilosc_tygodni} tygodni/e')
    elif ((dzien_oddania + 7) % 7) == 3:
        print(f'Twoje buty beda gotowe w srode za {ilosc_tygodni} tygodni/e')
    elif ((dzien_oddania + 7) % 7) == 4:
        print(f'Twoje buty beda gotowe w czwartek za {ilosc_tygodni} tygodni/e')
    elif ((dzien_oddania + 7) % 7) == 5:
        print(f'Twoje buty beda gotowe w piatek za {ilosc_tygodni} tygodni/e')
    elif ((dzien_oddania + 7) % 7) == 6:
        print(f'Twoje buty beda gotowe w sobote za {ilosc_tygodni} tygodni/e')
    elif ((dzien_oddania + 7) % 7) == 0:
        print(f'Twoje buty beda gotowe w niedziele za {ilosc_tygodni} tygodni/e')


if ilosc_tygodni == 0:
    if (dzien_oddania + ilosc_dni_naprawy) % 7 == 2:
        print('Twoje buty beda gotowe w najblizszy wtorek')
    elif (dzien_oddania + ilosc_dni_naprawy) == 3 or 10:
        print('Twoje buty beda gotowe w najblizsza srode')
    elif (dzien_oddania + ilosc_dni_naprawy) == 4 or 11:
        print('Twoje buty beda gotowe w najblizszy czwartek')
    elif (dzien_oddania + ilosc_dni_naprawy) == 5 or 12:
        print('Twoje buty beda gotowe w najblizszy piatek')
    elif (dzien_oddania + ilosc_dni_naprawy) == 6 or 13:
        print('Twoje buty beda gotowe w najblizsza sobote')
    elif (dzien_oddania + ilosc_dni_naprawy) == 7 or 14:
        print('Twoje buty beda gotowe w najblizsza niedziele')
    elif (dzien_oddania + ilosc_dni_naprawy) == 8:
        print('Twoje buty beda gotowe w najblizszy poniedzialek')
print()

pozegnanie = "ZAPRASZAMY PO ODBIOR, DO WIDZENIA"
print(f'{pozegnanie:_^40}')