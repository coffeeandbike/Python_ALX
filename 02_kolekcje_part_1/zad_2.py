'''
Napisz program obliczający średnią wartość z podanych przez użytkownika liczb.
Do przechowywania liczb użyj listy.
Pozwól na wprowadzenie maksymalnie 10 liczb. Skorzystaj z funkcji wbudowanej sum().
'''

ilosc_liczb = 1

lista_liczb = []

while ilosc_liczb <= 10:
    liczba = int(input("Podaj liczbe: "))
    lista_liczb.append(liczba)
    print(lista_liczb)
    ilosc_liczb += 1

suma = sum(lista_liczb)
print(f"Średnia z wprowadzonych liczb to: {suma/ilosc_liczb:.2f}")