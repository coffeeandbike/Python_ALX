"""
Zaimplementuj klasę Basket umożliwiającą dodawanie produktów w określonej liczbie do koszyka.
Zaimplementuj metodę obliczającą całkowitą wartość koszyka oraz wypisującą informację o zawartości koszyka.
Dodanie dwa razy tego samego produktu do koszyka powinno stworzyć tylko jedną pozycję.

Przykład użycia:
> basket = Basket()
> product = Product(1, 'Woda', 10.00)
> basket.add_product(product, 5)
> basket.count_total_price()
50.0
> basket.generate_report()
'Produkty w koszyku:\n
- Woda (1), cena: 10.00 x 5\n
W sumie: 50.00'
"""

import pytest
from collections import defaultdict


# https://yuml.me/preview/cbaf4a3e

class Product:
    def __init__(self, id: int, name: str, price: float):
        self.id = id
        self.name = name
        self.price = price

    def get_info(self) -> str:
        return f'Produkt "{self.name}", ID: "{self.id}", cena: "{self.price:.2f}" PLN'

    def __str__(self) -> str:
        return self.get_info()


class Basket:
    def __init__(self):
        self._items = defaultdict(int)# pusty slownik domyslny z itemami w koszyku

    def add_product(self, product: Product, quantity: int):
        if not isinstance(product, Product):  # jest produkt nie jest klasy Produkt
            raise TypeError("Product has to be an instance of class Product")
        # klucz -> wartosc
        # co bedzie kluczem ? nazwa produktu, id ?
        # kluczem moze byc OBIEKT
        if quantity <= 0:
            raise ValueError("Quantity must be positive")

        self._items[product] += quantity

    def count_total_price(self) -> float:

        # przerobic to na jedna linijke:
        kwoty = [product.price * quantity
            for product, quantity in self._items.items()
        ]
        suma_kwot = sum(kwoty)
        return suma_kwot

    def generate_report(self):
        '''
        Produkty w koszyku:
        - Woda(1), cena: 10.00 x5\n
        W sumie: 50.00
        '''
        print("Produkty w koszyku: ")
        for product, quantity in self._items.items():
            print(f'{product} x {quantity}')
        print(f'W sumie: {self.count_total_price()}')




    def product_count(self) -> int:
        return len(self._items)  # zwracamy dlugosc slownika items

    @property
    def is_empty(self) -> bool:
        if len(self._items) > 0:
            return False
        else:
            return True


b = Basket()
p = Product(1, 'woda', 11.22)
b.add_product(p, 4)
b.generate_report()


'''
Scenariusz testow:
1: dodanie jednego produktu
    - dodajemy produkt do koszyka i patrzymy czy jest w koszyku
    
2: dodanie dwa razy tego samego produktu

3: dodanie dwoch roznych produktow i sprawdzenie ceny

4: test wkladania do koszyka NIE produktu - powinien zostac  rzucony wyjatek TypeError

5: dodanie do koszyka produktu z ujemna iloscia sztuk - ValueError
'''


def test_add_one_product():
    b = Basket()
    p = Product(1, 'Rower', 2000)
    b.add_product(p, 1)
    assert b.product_count() == 1
    assert b.count_total_price() == 2000


def test_add_one_product_twice():
    b = Basket()
    p = Product(1, 'Rower', 2000)
    b.add_product(p, 1)
    b.add_product(p, 1)
    assert b.product_count() == 1
    assert b.count_total_price() == 4000


def test_add_two_products():
    b = Basket()
    p1 = Product(1, 'Rower', 2000)
    p2 = Product(1, 'Samochod', 20000)
    b.add_product(p1, 1)
    b.add_product(p2, 1)
    assert b.product_count() == 2
    assert b.count_total_price() == 22000


def test_add_not_product():
    b = Basket()
    p = "Nie wiem co"
    b.add_product(p ,1)
    with pytest.raises(TypeError):
        b.product_count(p, 1)


def test_add_negative_quantity():
    b = Basket()
    p = Product(1, 'Rower', 2000)
    b.add_product(p, -2)
    with pytest.raises(ValueError):
        b.product_count(p)

def test_empty_basket():
    b = Basket()
    assert  b.is_empty is True
