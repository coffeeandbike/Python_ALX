'''
### Zadanie 1.8 | Kalkulator lat psich (ok. 0,5 godz.)
​
Zakładamy, że 1 ludzki rok, to 5 lat psich.
​
Za pomocą konsoli wczytaj imię i wiek psa.
​
Wypisz komunikat ile pies miałby lat gdyby był człowiekiem.
​
Przykład:
Podaj imię psa - Burek
Podaj wiek psa - 3
​
Gdyby Burek był człowiekiem, miałby 15 lat.
'''

header = "Dog's age calculator"


print(f'{header:-^40}')
print()

while True:

    your_dog = []

    dog_name = input("Please enter your dog's name: ")

    dog_age = float(input("Enter your dog's age: "))

    your_dog.insert(0, dog_name)
    your_dog.insert(1, dog_age)

    print()
    print(f"If your dog {your_dog[0]} were a human, he would be {your_dog[1] * 5} years old")

    next = input("If you can calculate next dog age, please enter 'n'  \n"
                         "If you would like to exit, enter another letter: ")

    if next == 'n':
        continue
    else:
        break
