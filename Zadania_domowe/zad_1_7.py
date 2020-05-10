'''
### Zadanie 1.7 | Liczenie cen (ok. 0,5 godz.)
​
Przy pomocy `input()` zapytaj użytkownika co chce kupić, jaką ilość towaru chce kupić i jaka jest jego cena.
Wyświetl odpowiedni komunikat.
​
Przykład:
Co chcesz kupić? - ziemniaki
Podaj cenę towaru - 5
Podaj ilość towaru - 10
​
Za ziemniaki, który chcesz kupić, zapłacisz 50 zł
'''

naglowek = "Kalkulator zakupow"
print(f'{naglowek:_^30}')
print()

while True:

    towar = str(input("Jaki towar chcesz kupic ? "))
    cena = float(input("Jaka jest cena za kg/szt ? "))
    ilosc = float(input("Podaj ilosc jaka chcesz kupic - szt lub kg: "))

    zakupy = []

    zakupy.insert(0, towar)
    zakupy.insert(1, cena)
    zakupy.insert(2, ilosc)

    koszt = cena * ilosc

    print(f'Koszt zakupu towaru: {zakupy[0]} w ilosci {zakupy[2]} to: \n {koszt:.2f} PLN')
    print()
    co_dalej = input("Jesli chcesz policzyc koszt kolejengo towaru wpisz 'n'  \n"
                     "Jesli chcesz zakonczyc program wspisz inna litere: ")

    if co_dalej != 'n':
        break
    else:
        continue





