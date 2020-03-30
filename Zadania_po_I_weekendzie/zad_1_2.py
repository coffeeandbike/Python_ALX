'''
Potem napisz program, który prosi użytkownika (przez `input()`), żeby podał,
 ile kosztuje kilo ziemniaków i ile kilo chce kupić. Niech program policzy i wyświetli,
 ile trzeba będzie zapłacić za te ziemniaki.
'''

cena_za_kg = float(input('Ile kosztuje 1 kg ziemniakow ? '))

ile_chcesz_kupic = float(input('Ile kg ziemniakow chcesz kupic ? '))

cena_za_kupione_ziemniaki = cena_za_kg * ile_chcesz_kupic

print(f'Za {ile_chcesz_kupic} kg ziemniakow bedziesz musial/a zaplacic:\n {cena_za_kupione_ziemniaki:<.2f} PLN')

