# Zadanie 4.8
# Zaimplementuj metodę statyczną tworzącą koszyk na podstawie listy podanych produktów.
# Każdy z nich powinien zostać dodany do koszyka tylko raz.
# Przykład użycia:
# backset = Basket.with_products([prod_1, prod_2])


class Basket:

    @staticmethod
    def add_products(product_list: list) -> list:
        """
        This method allows adding unique product to the basket only one time
        :param product_list:
        :return: list with products in the basket
        """
        basket_with_products: list = []

        for product in product_list:
            if product in basket_with_products:
                return basket_with_products
            elif product not in basket_with_products:
                basket_with_products.append(product)

        return basket_with_products



koszyk = Basket.add_products(['p1','p2', 'p3', 'p4','p1','p2'])
print(koszyk)
print('='* 50)
koszyk2 = Basket.add_products(['rower', 'kawa', 'mieszkanie', 'rower','kiepski rower','kawa'])
print(koszyk2)
