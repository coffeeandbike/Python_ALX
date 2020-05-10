'''
Napisz program, który prosi użytkownika (przez `input()`), żeby podał, ile kosztuje kilo ziemniaków.
Niech program policzy i wyświetli, ile trzeba będzie zapłacić za pięć kilo ziemniaków.
'''

cena_za_kg = float(input('Podaje cene za 1 kg ziemniakow: '))

ilosc_kg = 5

print(f'Za {ilosc_kg} kg ziemniakow trzeba bedzie zaplacic {cena_za_kg * ilosc_kg:.2f} PLN')
