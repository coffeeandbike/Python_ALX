"""
Zaimplementuj mechanizm automatycznego generowania kolejnych ID dla produktów.
Informację o kolejnym ID przechowuj jako pole klasowe (class attribute).

Przykład użycia:
> product_1 = Product('Woda', 1.99)
> product_1.id
1
> product_2 = Product('Chleb', 2.50)
> product_2.id
2
"""


class Product:
    PRODUCT_ID: int = 1  # class attribute with product ID

    def __init__(self, name: str, price: float):
        """
        During initialization object, product ID will increment + 1
        :type name: object
        :param name:
        :param price:
        """
        self.name = name
        self.price = price
        self.__class__.PRODUCT_ID += 1

    def product_info(self) -> str:
        return f'Produkt "{self.name}", cena: {self.price:.2f} PLN, ID: {self.PRODUCT_ID}'

    def __str__(self) -> str:
        return self.product_info()


p1 = Product('Woda', 10.99)
print(p1)
p2 = Product('Rower', 200)
print(p2)
p3 = Product("Bulbulator", 1999)
print(p3)
