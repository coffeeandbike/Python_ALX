'''
Stwórz klasę `Zbiornik`. Niech ta klasa ma tylko jeden atrybut: `ilosc_wody` (z początkową wartością 0).
​
Niech ta klasa ma metody `dolej` i `odlej`. 
Obie metody niech przyjmują argument `ile` i niech odpowiednio dodają lub odejmują tę liczbę do atrybutu `ilosc_wody`. 
Niech nie da się odlać więcej wody, niż jest w zbiorniku.
​
Niech obiekt klasy `Zbiornik` po skonwertowaniu na napis dawał napis `zbiornik z (ileś tam) litrami wody`.
​
Przerób klasę `Zbiornik` tak, żeby miała też drugi atrybut - `temperatura`. 
Metoda dolej oprócz argumentu `ile` powinna też przyjmować argument `temperatura` oznaczający temperaturę dolewanej wody. 
Dolanie wody do zbiornika powinno powodować zmianę temperatury wody w zbiorniku (zgodnie ze zwykłymi prawami fizyki).
'''


class Tank:
    def __init__(self, water_amount):
        self.water_amount = water_amount

    def increare_water(self, how_much):
        self.water_amount = self.water_amount + how_much
        return self.water_amount

    def decrease_water(self, how_much):
        self.water_amount = self.water_amount - how_much
        if self.water_amount <= 0:
            self.water_amount = 0
            return self.water_amount

    def how_much_water(self):
        if self.water_amount > 0:
            return f"W zbiorniku jest {self.water_amount} litrow wody."
        elif self.water_amount <= 0:
            return "Brak wody"

    def __str__(self):
        return self.get_info()