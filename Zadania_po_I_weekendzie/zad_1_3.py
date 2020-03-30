'''
Potem napisz program, który prosi użytkownika (przez `input()`), żeby podał, ile kosztuje kilo ziemniaków,
ile kilo ziemniaków chce kupić, ile kosztuje kilo bananów i ile kilo bananów chce kupić.
Niech program policzy i wyświetli, ile trzeba będzie zapłacić za te ziemniaki i banany razem.
I niech program sprawdzi i powie, za co trzeba będzie zapłacić więcej - za banany czy za ziemniaki.
'''

cena_za_kg_ziemniakow = float(input("Podaj cene za 1 kg ziemniakow: "))

ile_ziemniakow = float(input("Ile kg ziemnakow chcesz kupic ? "))

cena_za_kg_bananow = float(input("Podaj cene za 1 kg bananow: "))

ile_bananow = float(input("Ile kg bananow chcesz kupic ? "))

cena_za_ziemniaki = cena_za_kg_ziemniakow * ile_ziemniakow

cena_za_banany = ile_bananow * cena_za_kg_bananow

print(f'W sumie za zakupy trzeba bedzie zaplacic {cena_za_banany + cena_za_ziemniaki:.2f}')

if cena_za_banany > cena_za_ziemniaki:
    print("Wiecej zaplacisz za banany")
elif cena_za_ziemniaki > cena_za_banany:
    print("Wiecej zaplacisz za ziemniaki")
else:
    print("Za ziemniaki i banany zaplacisz po tyle samo")



