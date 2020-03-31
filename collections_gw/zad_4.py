'''
Napisz program wypisujący wszystkie liczby od 0 do 100,
podzielne przez 3 lub podzielne przez 5.
Wypisz także jak dużo takich liczb wystąpiło w tym przedziale.
Liczby podzielne przez 3 lub 5:
0
3
5
...
96
99
100
W przedziale 0-100 jest 48 liczb podzielnych przez 3 lub 5
'''

ile_liczb = 0

for i in range (101):
    if i % 3 == 0 or i % 5 == 0:
        ile_liczb +=1
        print(i, end=" ")


print(f'\nPodzielnych przez 5 lub prze 3 jest: {ile_liczb}')


