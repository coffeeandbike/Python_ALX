# === OOP ===

# nazewnictwo klas to UpperCamelCase

class Towar: pass  # definicja klasy


a = Towar()

print(a)

a.cena = 10.00  # atrybut
a.nazwa = "Ksiazka o niczym"  # atrybut

print(a.nazwa)


class Towar:
    def __init__(self, nazwa, cena):  # funkcja init
        self.nazwa = nazwa
        self.cena = cena

    def opisz(self): #tworzenie metody opisz
        print(f"Towar {self.nazwa} kosztuje {self.cena}")


a = Towar("Ksiazka o niczym", 33.0)
print(a.nazwa)
print(a.cena)

b = Towar("rower", 1000)
print(b.nazwa)
print(b.cena)

a.opisz()
b.opisz()
