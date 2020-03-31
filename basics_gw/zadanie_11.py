'''
Napisz program, który na podstawie pozycji gracza (x, y) na planszy w przedziale od 0 do 100 wyświetli jego przybliżone położenie (centrum, prawy górny róg, górna krawędź, . . . ) lub informację o pozycji poza planszą. Przyjmij wartość 10 jako margines krawędzi.
Przykładowy komunikat programu:
Podaj pozycję gracza X: 95
Podaj pozycję gracza Y: 95
Gracz znajduje się w prawym górnym rogu.
'''

position_X: int = int(input("Please, enter your position on X axis in range 0-100: "))
position_Y: int = int(input("Please, enter your position on Y axis in range 0-100: "))
position = (position_X, position_Y)

if position_X >= 0 and position_X <= 10:
    if position_Y <= 10:
        print(f'Your position is: {position} and you are in the letf down corner')
    elif 10 < position_Y < 90:
        print(f'Your position is: {position} and you are in the letf middle field')
    elif 90 <= position_Y <= 100:
        print(f'Your position is: {position} and you are in the letf upper corner')

elif 10 < position_X <= 89:
    if 10 >= position_Y:
        print(f"Your position is: {position} and you are in down middle field")
    elif 10 < position_Y < 90:
        print(f"Your position is: {position} and you are in the middle of the board")
    elif 90 <= position_Y <= 100:
        print(f"Your position is: {position} and you in on middle upper field")

elif 90 <= position_X <= 100:
    if position_Y <= 10:
        print(f"Your position is: {position} and you are in the down right corner")
    elif 10 < position_Y < 90:
        print(f"Your position is: {position} and you are in the middle right field")
    elif 90 <= position_Y <= 100:
        print(f"Your position is: {position} and you are in the right upper corner")

elif position_Y > 100 or position_X > 100:
    print("You are out of the board")




