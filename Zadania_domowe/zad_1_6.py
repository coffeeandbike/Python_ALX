'''## Zadanie 1.6 | Bilety (ok. 1 godz.)
​
Założenia:
	- 0-6   - wiek przedszkolny - cena biletu: 0
	- 7-17  - wiek szkolny      - cena biletu: 2.28
	- 18-64 - wiek dorosły      - cena biletu: 3.80
	- +65   - wiek emerytalny   - cena biletu: 1.90
​
Napisz program, który przyjmuje dwie informacje: jaki jest wiek osoby kupującej bilety i ile biletów chce kupić. 
​
Na tej podstawie i powyższych założeń policz ile zapłaci za bilety, które chce kupić. Wczytywanie danych i ich wyświetlenie zrealizuj za pomocą konsoli. 
'''

header = "Ticket' price calculator"

header_2 = "Program will calculate total ticket's price"

print(f'{header:*^40}')
print()
print(f'{header_2}')
print()

while True:

    age = int(input('Please, enter your age: '))

    tickets = int(input('How many tickets are you going to buy ? '))

    tax_0_6 = 0
    tax_7_17 = 2.28
    tax_18_64 = 3.8
    tax_65_plus = 1.9

    price_7_17 = tax_7_17 * tickets
    price_18_64 = tax_18_64 * tickets
    price_65_plus = tax_65_plus * tickets

    if age <= 6:
        print ("Tax for your age is 0, so enjoy your journey for free.")
        next = input("Please enter 'next' for caltulating next ticket or any letter for exit: ")
        if next == "next":
            continue
        else:
            break

    if age >= 7 and age <= 17:
        print (f"Total price for your tickets will be {price_7_17:.2f} PLN")
        next = input("Please enter 'next' for caltulating next ticket or any letter for exit: ")
        if next == "next":
            continue
        else:
            break
            
    if age >= 18 and age <= 64:
        print (f"Total price for your tickets will be {price_18_64:.2f} PLN")
        next = input("Please enter 'next' for caltulating next ticket or any letter for exit: ")
        if next == "next":
            continue
        else:
            break
            
    if age >= 65:
        print (f"Total price for your tickets will be {price_65_plus:.2f} PLN")
        next = input("Please enter 'next' for caltulating next ticket or any letter for exit: ")
        if next == "next":
            continue
        else:
            break