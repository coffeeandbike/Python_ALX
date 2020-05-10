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
    def __init__(self, title: str, description: str, price: float, seller_name: str, seller_phone):
        """
        making class which will store announcement
        """
        self.title = title
        self.description = description
        self.price = price
        self.seller_name = seller_name
        self.seller_phone = seller_phone

    def __str__(self) -> str:
        return f' Tytul ogloszenia: {self.title}\n Opis: {self.description}\n Sprzedajacy: {self.seller_name}\n' \
               f' Kontakt do Sprzedajacego: {self.seller_phone}\n Cena: {self.price}'

ogloszenie = Announcements("Rower", 'Bardzo dobry rower', 2000.0, 'Jan Nowak', '111 222 333')


print(ogloszenie)
