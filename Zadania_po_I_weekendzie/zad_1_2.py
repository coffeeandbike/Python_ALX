'''
Napisz taki program: użytkownik ma podać, w jaki dzień tygodnia oddał buty do szewca
(poniedziałek to dzień 1, wtorek to dzień 2 itp.). Ma też podać, ile dni będzie trwała naprawa.
​
Program ma wypisać, w jaki dzień tygodnia buty będą gotowe do odbioru.
Jeśli tak będzie ci wygodniej, możesz założyć, że naprawa butów nigdy nie będzie trwała dłużej niż siedem dni.
'''

szyld = "POGOTOWIE SZEWSKIE 7 DNI W TYGODNIU"
powitanie = "SUPER PROGRAM - KIEDY BUTY"
print(f'{szyld:*^50}\n')
print(f'{powitanie:_^50}')
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
ilosc_dni_w_tygodniu = ilosc_dni_naprawy % 7
dzien_tygodnia = dzien_oddania + ilosc_dni_w_tygodniu

print()
#print(ilosc_tygodni)
#print(ilosc_dni_w_tygodniu)

#print(dzien_tygodnia)

if dzien_tygodnia == 1 or dzien_tygodnia == 8:
    print(f"""Twoje buty beda gotowe w poniedzialek od rana
            za {ilosc_tygodni} tygodni/e""")

elif dzien_tygodnia == 2 or dzien_tygodnia == 9:
    print(f"""Twoje buty beda gotowe we wtorek od rana
            za {ilosc_tygodni} tygodni/e""")

elif dzien_tygodnia == 3 or dzien_tygodnia == 10:
    print(f"""Twoje buty beda gotowe w srode od rana
            za {ilosc_tygodni} tygodni/e""")

elif dzien_tygodnia == 4 or dzien_tygodnia == 11:
    print(f"""Twoje buty beda gotowe w czwartek od rana
            za {ilosc_tygodni} tygodni/e""")

elif dzien_tygodnia == 5 or dzien_tygodnia == 12:
    print(f"""Twoje buty beda gotowe w piatek od rana
            za {ilosc_tygodni} tygodni/e""")

elif dzien_tygodnia == 6 or dzien_tygodnia == 13:
    print(f"""Twoje buty beda gotowe w sobote od rana
            za {ilosc_tygodni} tygodni/e""")

elif dzien_tygodnia == 7 or dzien_tygodnia == 14:
    print(f"""Twoje buty beda gotowe w niedziele od rana
            za {ilosc_tygodni} tygodni/e""")

else:
    print("Podales bledne dane")
print()

pozegnanie = "ZAPRASZAMY PO ODBIOR, DO WIDZENIA"
print(f'{pozegnanie:_^40}')

