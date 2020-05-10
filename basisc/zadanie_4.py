'''
Napisz program wyliczający kwotę należną za zakupiony towar na podstawie ceny za kilogram oraz liczby zakupionych kilogramów.
Do przechowywania informacji o cenie oraz liczbie kilogramów użyj zmiennych. Wypisz wszystkie informacje na konsolę.
Przykładowy komunikat programu:
Cena za kg: 10.0
Waga: 2.5
Należność: 25.0
'''

cena_za_kg = 5.0

ilosc_kg = 4.5

naleznosc = cena_za_kg * ilosc_kg

# 1 sposob
print("Cena za kg to: ", cena_za_kg, "PLN")
print("Ilosc zakupionych towarow: ", ilosc_kg, "kg")
print("Naleznosc za zakupy to: ", naleznosc, "PLN")

#2 sposob ale nie preferowany
print("Cena za kg to: "+ str(cena_za_kg) + "PLN")
print("Ilosc zakupionych towarow: " + str(ilosc_kg) + "kg")
print("Naleznosc za zakupy to: " + str(naleznosc) + "PLN")

# f-string czyli formatowany string - mechanizm ktory pozwala wrzucac zawartosc zmiennych do napisu
print(f"Cena za kg: {cena_za_kg:.2f} zł") #.2f z dokladoscia do dwoch miejsc po przecinku i typ zmiennej f float
print(f"Ilosc: {ilosc_kg} kg")
print(f"Cena za zakupy:  {naleznosc:<10.2f} zł") # naleznosc ma zajac 10 miejsc z dokladnoscia do dwoch miejsc po przeciku
                                                #wyrownane do lewe strony
print(f"Cena za zakupy:  {naleznosc:_^10.2f} zł")