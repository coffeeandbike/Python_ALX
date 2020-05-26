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
        return self.how_much_water()




class Tank2:
    """
    class with water temperature calculating
    """
    def __init__(self, liters: float, temperature: float):
        self.liters = liters
        self.temperature = temperature
        t3 = 0

    def increare_water(self, how_much: float, t2: float):
        self.liters = self.liters + how_much
        t3: float = ((self.temperature * self.liters) + (t2 * how_much)) / (self.liters + how_much)
        self.temperature = t3
        water_params = []
        water_params.append(self.liters)
        water_params.append(self.temperature)
        return water_params


    def decrease_water(self, how_much: float):
        self.temperature = self.temperature
        self.liters = self.liters - how_much
        if self.liters <= 0:
            self.liters = 0
        water_params = []
        water_params.append(self.liters)
        water_params.append(self.temperature)
        return water_params


    def water_info(self):
        if self.liters > 0:
            return f"W zbiorniku jest {self.liters} litrow wody o temperaturze {self.temperature:.2f}"
        elif self.liters <= 0:
            return "Brak wody"

    def __str__(self):
        return self.water_info()


boiler = Tank2(100, 50)

boiler.increare_water(10, 50)

print(boiler)

boiler.decrease_water(40)

print(boiler)

boiler.decrease_water(80)

print(boiler)

boiler.increare_water(100, 70)
boiler.increare_water(20, 100)

print(boiler)

boiler.increare_water(1, 70)
print(boiler)