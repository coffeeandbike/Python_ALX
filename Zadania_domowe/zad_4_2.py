"""
Lista ogłoszeń
​
Napisz programy, w których tworzysz listę ogłoszeń samochodowych, a następnie wyszukujesz ogłoszenia na podstawie ich parametrów.
​
Na przykład ogłoszenia o cenach z określonego przedziału.
​
Użyj funkcji `lambda`, określających, które ogłoszenia powinny zostać wyszukane.
Użyj poznanych kolekcji do trzymania ogłoszeń. Możesz zastosować metodę `filter` do wyszukiwania odpowiednich ogłoszeń.
"""

board = []

filtered_board = []

look_for = None


class AnnouncementsBoard():

    def __init__(self, category: int, title: str, description: str, price: float, seller_name: str, seller_phone: str, address: str):
        """
        making class which will store announcements board
        """
        self.category = category
        self.title = title
        self.description = description
        self.price = price
        self.seller_name = seller_name
        self.seller_phone = seller_phone
        self.address = address

    def __str__(self) -> str:
        return f' Category: {self.category}\n' \
               f' Title: {self.title}\n' \
               f' Description: {self.description}\n ' \
               f' Seller: {self.seller_name}\n' \
               f' Address: {self.address}\n' \
               f' Seller phone: {self.seller_phone}\n' \
               f' Price: {self.price}'

    def announcement_add(self) -> dict:
        self.notice = {}

        """
        add announcement to 'notice' dictionary
        
        :return: dic
        """

        self.notice.update({'Category': self.category, 'Title': self.title, 'Description': self.description,
                            'Seller name': self.seller_name, 'Address': self.address, 'Seller phone': self.seller_phone,
                            'Price': self.price})
        return self.notice

    def announcement_search(self,) -> list:
        pass



ogloszenie1 = AnnouncementsBoard(1, 'Rower', 'Bardzo dobry rower', 2000.0, 'Jan Nowak', '111 222 333', 'Pcim Sredni')

ogloszenie2 = AnnouncementsBoard(2, 'Kawa', 'niedobra kawa', 20.0, 'Janina Jakas', '123 456 798', 'Wroclaw')

board.append(ogloszenie1.announcement_add())

board.append(ogloszenie2.announcement_add())

print()
print()

print(board)

print(ogloszenie2)
