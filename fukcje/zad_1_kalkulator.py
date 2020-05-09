#KALKULATOR

#pobieramy liczby od uzytkownika

#pytamy o dzialanie

# wykonujemy obliczenia i pokazujemy wynik

def dodawanie(x, y):
    return x + y

def odejmowanie(x, y):
    return x - y

def mnozenie(x, y):
    return x * y

def dzielenie(x, y):
    return x / y

x = float(input('Podaj pierwsza liczbe: '))
print()
y = float(input('Podaj druga liczbe: '))
print()

dzialanie = input("""Wybierz dzialanie:
+ dodawanie
- odejmowanie
* mnozenie
/ dzielenie
""")

if dzialanie == '+':
    print(f'Wynik to {dodawanie(x,y)}')
elif dzialanie == '-':
    print(f'Wynik to {odejmowanie(x,y)}')
elif dzialanie == '*':
    print(f'Wynik to {mnozenie(x,y)}')
elif dzialanie == '/':
    print(f'Wynik to {dzielenie(x,y)}')
else:
    print('wybrales bledne dzialanie')
    exit()




