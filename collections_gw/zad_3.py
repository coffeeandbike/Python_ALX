'''
Napisz program zliczający wystąpienia liczb dodatnich i ujemnych w zadanej liście liczb całkowitych.
'''

lista_liczb = [-5, -10, 3, 6, -50, 0, 22, 33, -52]

ilosc_dodatnich = 0
ilosc_ujemnych = 0
ilosc_zer = 0

for liczba in lista_liczb:
    if liczba > 0:
        ilosc_dodatnich += 1

    elif liczba < 0:
        ilosc_ujemnych +=1

    elif liczba == 0:
        ilosc_zer +=1

print(f'ilosc licz dodatnich: {ilosc_dodatnich}')
print(f'ilosc licz ujemnych: {ilosc_ujemnych}')
print(f'ilosc zer: {ilosc_zer}')