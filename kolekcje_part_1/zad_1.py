'''
W sesji interaktywnego środowiska interpretera stwórz tuplę zawierającą 10 różnych liczb całkowitych.
Korzystając z operatora dostępu oraz wycinania pobierz:
- drugi element
- przedostatni element
- elementy od trzeciego do siódmego (włącznie) 􏰀 co trzeci element
- co drugi element licząc od końca
'''

tupla = (21,34,45,65,76,43,-50,-10,1,0)

print(tupla[1])

print(tupla[-2])

print(tupla[2:8:3])

print(tupla[::-2])