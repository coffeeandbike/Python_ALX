"""
Zaimplementuj klasę Product przechowującą informację o cenie, nazwie oraz ID produktu.
Zaimplementuj metodę wypisującą informację o produkcie na konsolę.

Przykład użycia:
product = Product(1, 'Woda', 10.99)
product.print_info()
Produkt "Woda", id: 1, cena: 10.99 PLN

Scenariusz:
- tworzymy klase
- tworzymy metode __init__
    - uzupelniamy atrybuty
- tworzyme metode print_info()
"""

# stworzenie klasy Produkt
class Produkt:
    def __init__(self, id: float, nazwa: str, cena: float):
        self.id = id
        self.nazwa = nazwa
        self.cena = cena

    def wypisz(self):
        #print(f"Produkt {self.nazwa} ma ID: {self.id} i kosztuje {self.cena:.2f} PLN")
        print(self.get_info) #tak mozna tez to zrobic


    def get_info(self) -> str:
        return f'Produkt "{self.nazwa}", ID: "{self.id}", i kosztuje "{self.cena:.2f}" PLN'

    def __str__(self): #tworzymy dunder metode
        return f" Produkt: {self.nazwa}, cena: {self.cena}"


# tworzymy obiekt o nazwie woda
woda = Produkt(nazwa= "Woda", cena= 10.45, id = 1.0)

# uruchamiamy metode wypisz na obiekcie woda
woda.wypisz()

info = woda.get_info()
print(f'Info o produkcie: {info}')
print(woda)
#woda.get_info

#print(woda)


def test_klasy_produkt():
    pr = Produkt(1.0, woda, 2.0)
    assert pr.id == 1.0
    assert pr.nazwa == woda
    assert pr.cena == 2.0
