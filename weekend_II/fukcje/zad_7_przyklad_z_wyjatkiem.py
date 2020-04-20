from weekend_II.fukcje.zad_7_funkcja_do_liczenia_silni import silnia

print("Przed liczeniem silni")


try:

    wynik = silnia(-10) #dostaniemy wyjatek
    print(wynik)

except ValueError:
    print("Podales liczbe ujemna !!!")

print("po policzeniu silni")