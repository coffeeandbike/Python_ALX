'''Zadanie 2.4 | Zgadnij liczbę z zakresu
​
Program losuje liczbę z zakresu od 0 do 999. Użytkownik ma zgadnąć tę liczbę nie widząc jej.
Kiedy użytkownik poda nieprawidłowy wynik, program podpowiada pisząc czy podana liczba była za duża, czy za mała.
Gdy użytkownik poda właściwą liczbę, program wypisuje gratulacje jednocześnie informując, w której próbie udało się zgadnąć liczbę.
'''

from random import randint
import time

title = "Guess the number"
header ="Your task is to guess the number from range 0-999"
print(f'{title:*^40}\n')
print(f'{header:<}')

print("the program randomly draws a number, wait a moment")

print(f"....")
time.sleep(1)
print(".........")
time.sleep(1)
print("................\n")

hidden_number = randint(0,999)

print("The hidden number has been drawn")

while True:
    your_number = int(input("Please try guess the number: "))

    if your_number > hidden_number:
        print("Your number is greater than number to guess")
        continue

    if your_number < hidden_number:
        print("Your number is smaller than number to guess")
        continue

    if your_number == hidden_number:
        print("You are great, you guessed the hidden number")
        time.sleep(1)
        print("This is the End")
        break






