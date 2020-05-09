"""
Napisz klasę Osoba, która ma:
- atrybuty imie, nazwisko, wiek
- metode przedstaw_sie, ktora ma wypisac imie, nazwisko i wiek na konsole

Stworz dwie osoby:
- Jan Kowalski, 21 lat
- Ala Nowa, 30 lat

i niech się przedstawią
"""


class Osoba:
    def __init__(self, imie, nazwisko, wiek):
        self.imie = imie #atrybut
        self.nazwisko = nazwisko #atrybut
        self.wiek = wiek #atrybut

    def przedstaw_sie(self) -> object: #metoda przedstaw_sie
        print(f"Hej, mam na imie {self.imie} moje nazwisko to {self.nazwisko} i mam {self.wiek} lat.")


osoba_1 = Osoba("Jan", "Kowalski", 40) #tworzymy obiekt osoba_1

osoba_2 = Osoba("Ala", "Nowa", 18)

osoba_1.przedstaw_sie() #na obiekcie osoba_1 uruchamiamy metode przedstaw_sie
osoba_2.przedstaw_sie()
