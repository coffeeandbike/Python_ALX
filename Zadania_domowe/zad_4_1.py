"""
Zadanie 4.1 | Ogłoszenia
​
Zaproponuj klasę, w której obiektach będzie się zapisywać ogłoszenia
(takie jak w serwisie internetowym z ogłoszeniami).
​
Najlepiej, aby klasa `Ogloszenie` opisywała rzeczy, które posiada każde ogłoszenie,
m.in. tytuł, opis, cenę, dane kontaktowe sprzedawcy.

"""


class Announcements():
    def __init__(self, title: str, description: str, price: float, seller: dict):
        """
        making class which will store announcement
        """
        self.title = title
        self.description = description
        self.price = price
        self.seller = seller
